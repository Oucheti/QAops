import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


FORMY_URL = "https://formy-project.herokuapp.com"


# ============================================================
# CONFIGURATION SELENIUM
# ============================================================

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


# ============================================================
# TEST 1 : FORMULAIRE
# ============================================================

@allure.feature("Tests UI - Formy")
@allure.story("Formulaire")
@allure.title("Vérifier le formulaire d'inscription")
def test_registration_form(driver):

    with allure.step("Ouvrir la page Formy"):
        driver.get(FORMY_URL + "/form")

    with allure.step("Remplir le prénom"):
        first_name = driver.find_element(By.ID, "first-name")
        first_name.send_keys("Abdelhaq")

    with allure.step("Remplir le nom"):
        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Oucheti")

    with allure.step("Remplir le métier"):
        job_title = driver.find_element(By.ID, "job-title")
        job_title.send_keys("QA Engineer")

    with allure.step("Sélectionner le bouton radio"):
        radio = driver.find_element(By.ID, "radio-button-1")
        radio.click()

        assert radio.is_selected()

    with allure.step("Sélectionner une valeur dans le dropdown"):
        select_element = driver.find_element(By.ID, "select-menu")

        select = Select(select_element)
        select.select_by_visible_text("0-1")

        assert select.first_selected_option.text == "0-1"

    with allure.step("Vérifier les données saisies"):
        assert first_name.get_attribute("value") == "Abdelhaq"
        assert last_name.get_attribute("value") == "Oucheti"
        assert job_title.get_attribute("value") == "QA Engineer"


# ============================================================
# TEST 2 : CHECKBOX
# ============================================================

@allure.feature("Tests UI - Formy")
@allure.story("Checkbox")
@allure.title("Vérifier la sélection d'une checkbox")
def test_checkbox(driver):

    with allure.step("Ouvrir la page Checkbox"):
        driver.get(FORMY_URL + "/checkbox")

    with allure.step("Récupérer la checkbox"):
        checkbox = driver.find_element(By.ID, "checkbox-1")

    with allure.step("Vérifier que la checkbox est visible"):
        assert checkbox.is_displayed()

    with allure.step("Vérifier que la checkbox est activée"):
        assert checkbox.is_enabled()

    with allure.step("Sélectionner la checkbox"):
        checkbox.click()

    with allure.step("Vérifier que la checkbox est sélectionnée"):
        assert checkbox.is_selected()


# ============================================================
# TEST 3 : BUTTONS
# ============================================================

@allure.feature("Tests UI - Formy")
@allure.story("Buttons")
@allure.title("Vérifier les boutons")
def test_buttons(driver):

    with allure.step("Ouvrir la page Buttons"):
        driver.get(FORMY_URL + "/buttons")

    with allure.step("Récupérer le bouton principal"):
        button = driver.find_element(
            By.CSS_SELECTOR,
            ".btn-primary"
        )

    with allure.step("Vérifier que le bouton est visible"):
        assert button.is_displayed()

    with allure.step("Vérifier que le bouton est activé"):
        assert button.is_enabled()

    with allure.step("Cliquer sur le bouton"):
        button.click()


# ============================================================
# TEST 4 : KEYPRESS
# ============================================================

@allure.feature("Tests UI - Formy")
@allure.story("Saisie clavier")
@allure.title("Vérifier la saisie dans un champ")
def test_keypress(driver):

    with allure.step("Ouvrir la page Keypress"):
        driver.get(FORMY_URL + "/keypress")

    with allure.step("Saisir un texte"):
        input_field = driver.find_element(By.ID, "name")
        input_field.send_keys("Hello Selenium")

    with allure.step("Vérifier le texte saisi"):
        assert input_field.get_attribute("value") == "Hello Selenium"


# ============================================================
# TEST 5 : DATEPICKER
# ============================================================

@allure.feature("Tests UI - Formy")
@allure.story("Datepicker")
@allure.title("Vérifier le champ Datepicker")
def test_datepicker(driver):

    with allure.step("Ouvrir la page Datepicker"):
        driver.get(FORMY_URL + "/datepicker")

    with allure.step("Sélectionner le champ date"):
        date_input = driver.find_element(
            By.ID,
            "datepicker"
        )

        date_input.click()

    with allure.step("Saisir la date"):
        date_input.send_keys("09/29/2026")

    with allure.step("Vérifier la date"):
        assert date_input.get_attribute("value") == "09/29/2026"