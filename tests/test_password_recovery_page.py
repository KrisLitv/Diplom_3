import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import URLS, MainUrl
from helpers.user_data import Person
from pages.main_page import MainPage
from pages.password_recovery import RecoveryPage
from pages.login_page import LoginPage


class TestRecoveryPage:

    @allure.title('Переход на страницу восстановления пароля через кнопку "Восстановить пароль"')
    def test_follow_to_the_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        assert recovery_page.check_recovery_form() and recovery_page.get_current_url() == (MainUrl.MAIN_URL + URLS.URL_PASSWORD_RECOVERY)

    @allure.title('Ввод электронной почты и нажатие кнопки "Восстановить"')
    def test_input_password_and_click_recovery_btn(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.input_email_to_email_field(Person.create_data_correct_user()["email"])
        recovery_page.click_recovery_btn()
        assert recovery_page.check_save_btn() and recovery_page.get_current_url() == (MainUrl.MAIN_URL + URLS.URL_PASSWORD_RESET)

    @allure.step('Проверка активности поля "Пароль"')
    def check_active_password_field(self, password):
        self.click_on_element(RecoveryPageLocators.SHOW_BTN)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RecoveryPageLocators.PASSWORD_FIELD)
        )
        password_field = self.driver.find_element(*RecoveryPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        return password_field.get_attribute('value') == password

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()


    @allure.title('Проверка подсветки поля "Пароль"')
    def test_checking_the_backlight_of_the_password_field(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        person_data = Person().create_data_correct_user()
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.input_email_to_email_field(person_data.get("email"))
        recovery_page.click_recovery_btn()
        assert recovery_page.check_active_password_field(person_data.get("password"))