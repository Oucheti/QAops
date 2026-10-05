pipeline {
    agent any

    environment {
        REQRES_API_KEY = credentials('reqres-api-key')
        JMETER_HOME = 'C:\Program Files\apache-jmeter-5.6.3'
    }

    stages {

        stage('Install Dependencies') {
            steps {
                powershell '''
                    & "C:\\Users\\dev\\AppData\\Local\\Python\\bin\\python.exe" -m venv venv

                    .\\venv\\Scripts\\python.exe -m pip install --upgrade pip

                    .\\venv\\Scripts\\python.exe -m pip install -r requirements.txt

                    npm install -g newman
                '''
            }
        }

        stage('Start Application') {
            steps {
                powershell '''
                    Write-Host "Demarrage de l'application..."

                    $python = "$PWD\\venv\\Scripts\\python.exe"
                    $app = "$PWD\\app\\app.py"

                    # Lancement via WMI/CIM : le processus est cree par WmiPrvSE.exe,
                    # donc il n'herite PAS du Job Object de Jenkins.
                    # Avec Start-Process, Jenkins attend la fin de TOUS les processus
                    # rattaches a son Job Object, y compris Flask -> le step ne finit jamais.
                    $cmd = "`"$python`" `"$app`" > `"$PWD\\app.log`" 2> `"$PWD\\app-error.log`""
                    $proc = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine = $cmd}

                    if ($proc.ReturnValue -ne 0) {
                        Write-Error "Echec du demarrage de Flask (code $($proc.ReturnValue))"
                        exit 1
                    }

                    $proc.ProcessId | Out-File "$PWD\\flask.pid"
                    Write-Host "Processus Flask demarre (PID: $($proc.ProcessId))."

                    Start-Sleep -Seconds 5

                    Write-Host "Verification HTTP..."
                    $response = Invoke-WebRequest -Uri "http://127.0.0.1:5000/" -UseBasicParsing -TimeoutSec 10
                    Write-Host "HTTP Status : $($response.StatusCode)"
                    Write-Host "Application disponible."
                '''
            }
        }

        stage('Run Python Tests') {
            steps {
                powershell '''
                    .\\venv\\Scripts\\python.exe -m pytest tests\\ --junitxml=pytest-results.xml
                '''
            }

            post {
                always {
                    junit 'pytest-results.xml'
                }
            }
        }

        stage('API Tests with Newman') {
            steps {
                powershell '''
                    newman run postman\\collection.json `
                        --env-var "apiKey=$env:REQRES_API_KEY" `
                        --reporters '"cli,junit"' `
                        --reporter-junit-export newman-results.xml
                '''
            }

            post {
                always {
                    junit 'newman-results.xml'
                }
            }
        }

        stage('Performance Tests - JMeter') {
            steps {
                powershell '''
                    if (Test-Path jmeter\\results.jtl) { Remove-Item jmeter\\results.jtl -Force }

                    & "$env:JMETER_HOME\\bin\\jmeter.bat" -n `
                        -t jmeter\\ProjectQaops.jmx `
                        -l jmeter\\results.jtl `
                        -j jmeter\\jmeter.log

                    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
                '''
            }

            post {
                always {
                    archiveArtifacts artifacts: 'jmeter/results.jtl, jmeter/jmeter.log', allowEmptyArchive: true
                }
            }
        }
}