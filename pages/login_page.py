import allure
from pages.base_page import BasePage
from locators.locators import AuthPageLocators


class LoginPage(BasePage):

    @allure.step('Проверка наличия формы авторизации')
    def check_authorization_form(self):
        return self.check_element(AuthPageLocators.AUTH_FORM)

    @allure.step('Ввод email в поле "Email"')
    def input_email_to_email_field(self, email):
        self.send_keys_to_field(AuthPageLocators.EMAIL_INPUT, email)

    @allure.step('Ввод пароля в поле "Пароль"')
    def input_password_to_password_field(self, password):
        self.send_keys_to_field(AuthPageLocators.PASSWORD_INPUT, password)

    @allure.step('Нажатие на кнопку "Войти"')
    def click_login_btn(self):
        self.move_to_element_and_click(AuthPageLocators.LOGIN_ENDPOINT_ACCOUNT_BTN)

    @allure.step('Выполнение авторизации пользователя')
    def login(self, email, password):
        self.input_email_to_email_field(email)
        self.input_password_to_password_field(password)
        self.click_login_btn()

    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_recovery_btn(self):
        self.move_to_element_and_click(AuthPageLocators.RECOVER_BTN)

    @allure.step('Нажатие на кнопку "Зарегистрироваться"')
    def click_register_btn(self):
        self.move_to_element_and_click(AuthPageLocators.REGISTRATION_BTN)
