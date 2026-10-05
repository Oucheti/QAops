import allure


BASE_URL = "https://reqres.in/api"


# ============================================================
# TEST 1 : GET USERS
# ============================================================

@allure.feature("Tests API - Reqres")
@allure.story("GET Users")
@allure.title("Récupérer la liste des utilisateurs")
def test_get_users(api):

    with allure.step("Envoyer une requête GET"):
        response = api.get(
            f"{BASE_URL}/users",
            params={"page": 2}
        )

    with allure.step("Vérifier le statut HTTP"):
        assert response.status_code == 200

    with allure.step("Vérifier que la réponse est en JSON"):
        assert "application/json" in response.headers.get(
            "Content-Type",
            ""
        )

    with allure.step("Récupérer le JSON"):
        data = response.json()

    with allure.step("Vérifier la structure générale"):
        assert isinstance(data, dict)

    with allure.step("Vérifier la présence du champ page"):
        assert "page" in data

    with allure.step("Vérifier la présence du champ data"):
        assert "data" in data

    with allure.step("Vérifier que data est un tableau"):
        assert isinstance(data["data"], list)

    with allure.step("Vérifier le numéro de page"):
        assert data["page"] == 2

    with allure.step("Vérifier la structure d'un utilisateur"):

        if len(data["data"]) > 0:

            user = data["data"][0]

            assert "id" in user
            assert "email" in user
            assert "first_name" in user
            assert "last_name" in user
            assert "avatar" in user


# ============================================================
# TEST 2 : POST USERS
# ============================================================

@allure.feature("Tests API - Reqres")
@allure.story("POST Users")
@allure.title("Créer un utilisateur")
def test_create_user(api):

    payload = {
        "name": "Abdelhaq",
        "job": "QA Engineer"
    }

    with allure.step("Envoyer une requête POST"):
        response = api.post(
            f"{BASE_URL}/users",
            json=payload
        )

    with allure.step("Vérifier le statut HTTP"):
        assert response.status_code == 201

    with allure.step("Vérifier que la réponse est en JSON"):
        assert "application/json" in response.headers.get(
            "Content-Type",
            ""
        )

    with allure.step("Récupérer le JSON"):
        data = response.json()

    with allure.step("Vérifier la structure"):
        assert isinstance(data, dict)

    with allure.step("Vérifier la présence de l'identifiant"):
        assert "id" in data

    with allure.step("Vérifier la présence de createdAt"):
        assert "createdAt" in data

    with allure.step("Vérifier le nom"):
        assert data["name"] == "Abdelhaq"

    with allure.step("Vérifier le job"):
        assert data["job"] == "QA Engineer"


# ============================================================
# TEST 3 : PUT USERS
# ============================================================

@allure.feature("Tests API - Reqres")
@allure.story("PUT Users")
@allure.title("Modifier un utilisateur")
def test_update_user(api):

    payload = {
        "name": "Abdelhaq",
        "job": "Senior QA Engineer"
    }

    with allure.step("Envoyer une requête PUT"):
        response = api.put(
            f"{BASE_URL}/users/2",
            json=payload
        )

    with allure.step("Vérifier le statut HTTP"):
        assert response.status_code == 200

    with allure.step("Vérifier que la réponse est en JSON"):
        assert "application/json" in response.headers.get(
            "Content-Type",
            ""
        )

    with allure.step("Récupérer le JSON"):
        data = response.json()

    with allure.step("Vérifier la structure"):
        assert isinstance(data, dict)

    with allure.step("Vérifier le nom"):
        assert data["name"] == "Abdelhaq"

    with allure.step("Vérifier le job"):
        assert data["job"] == "Senior QA Engineer"

    with allure.step("Vérifier la présence de updatedAt"):
        assert "updatedAt" in data


# ============================================================
# TEST 4 : DELETE USERS
# ============================================================

@allure.feature("Tests API - Reqres")
@allure.story("DELETE Users")
@allure.title("Supprimer un utilisateur")
def test_delete_user(api):

    with allure.step("Envoyer une requête DELETE"):
        response = api.delete(
            f"{BASE_URL}/users/2"
        )

    with allure.step("Vérifier le statut HTTP"):
        assert response.status_code == 204

    with allure.step("Vérifier que la réponse est vide"):
        assert response.text == ""