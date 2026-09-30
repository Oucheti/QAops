# Projet d'Automatisation des Tests et Qualité Logiciel

## 1. Présentation du projet

Mettre en place une démarche complète d'automatisation des tests qui couvre plusieurs niveaux:

- Tests fonctionnels UI avec Selenium
- Tests API avec Python/Requests
- Tests API avec Postman/Newman
- Tests de performance avec Apache JMeter
- Génération de rapports avec Allure
- Intégration continue avec Jenkins

L'objectif final est d'intégrer les différents tests dans une chaîne CI/CD afin d'automatiser l'exécution et le suivi de la qualité logicielle.

---

# 2. Objectifs

Les principaux objectifs du projet sont :

- Automatiser les tests de l'interface utilisateur.
- Automatiser les tests des API REST.
- Vérifier les codes HTTP et les réponses JSON.
- Vérifier la structure et le contenu des données.
- Simuler au minimum 50 utilisateurs avec JMeter.
- Mesurer le temps de réponse et le débit.
- Mesurer le taux d'erreurs.
- Générer des rapports de tests avec Allure.
- Intégrer tous les tests dans Jenkins.
- Produire des résultats exploitables pour le rapport de qualité.

---

# 3. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Automatisation des tests |
| Pytest | Framework de tests |
| Selenium | Tests UI |
| Requests | Tests API automatisés |
| Formy Project | Application de démonstration UI |
| Reqres | API REST de test |
| Postman | Tests API |
| Newman | Exécution Postman en ligne de commande |
| Allure | Rapports de tests |
| Apache JMeter | Tests de performance |
| OWASP ZAP | Tests de sécurité |
| Jenkins | CI/CD |
| Git | Gestion du code source |

---

# 4. Architecture du projet

```text
ProjectAutomatisationTests/
│
├── app/
│   ├── app.py
│   ├── index.html
│   └── style.css
│
├── tests/
│   ├── test_formy_ui.py
│   └── test_reqres_api.py
│
├── postman/
│   └── collection.json
│
├── jmeter/
│   ├── test_plan.jmx
│   └── results.jtl
│
├── allure-results/
│
├── allure-report/
│
├── Jenkinsfile
│
├── requirements.txt
│
├── pytest-results.xml
│
├── newman-results.xml
│
├── app.log
│
├── app-error.log
│
└── README.md