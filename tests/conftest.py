import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from data.urls import MainUrl
from helpers.user_data import Person
from data.urls import Endpoints
from data.ingredients import Ingredients
from pages.main_page import HeaderPage, MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://stellarburgers.nomoreparties.site/')
    elif request.param == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
        options.add_argument("--width=1200")
        options.add_argument("--height=900")
        options.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(service=service, options=options)
        driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture
def create_new_user():
    payload = Person.create_data_correct_user()
    response = requests.post(MainUrl.MAIN_URL + Endpoints.CREATE_USER_ENDPOINT, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(MainUrl.MAIN_URL + Endpoints.DELETE_USER_ENDPOINT, headers={"Authorization": token})


@pytest.fixture
def login(driver, create_new_user):
    create_user_data = create_new_user[0]
    header_page = HeaderPage(driver)
    login_page = LoginPage(driver)
    header_page.click_profile_area_btn()
    login_page.login(create_user_data["email"], create_user_data["password"])
    main_page = MainPage(driver)
    main_page.wait_load_main_page()


@pytest.fixture
def create_order(create_new_user):
    token = create_new_user[1].json()["accessToken"]
    headers = {'Authorization': token}
    response = requests.post(MainUrl.MAIN_URL + Endpoints.CREATE_ORDER_ENDPOINT, headers=headers,
                             data=Ingredients.correct_ingredients_data)
    return response.json()["order"]["number"]