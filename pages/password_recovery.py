import allure
from pages.base_page import BasePage
from locators.locators import RecoveryPageLocators


class RecoveryPage(BasePage):

    @allure.step('Проверка отображения формы восстановления пароля')
    def check_recovery_form(self):
        return self.check_element(RecoveryPageLocators.RECOVERY_TEXT_FORM)

    @allure.step('Ввод Email в поле для электронной почты')
    def input_email_to_email_field(self, email):
        self.send_keys_to_field(RecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Нажатие кнопки "Восстановить пароль"')
    def click_recovery_btn(self):
        self.click_on_element(RecoveryPageLocators.RECOVER_BTN)

    @allure.step('Нажатие кнопки "Войти"')
    def click_login_btn(self):
        self.click_on_element(RecoveryPageLocators.LOGIN_ENDPOINT_ACCOUNT_BTN)

    @allure.step('Ввод пароля в поле "Пароль"')
    def input_password_to_password_field(self, password):
        self.send_keys_to_field(RecoveryPageLocators.PASSWORD_INPUT, password)

    @allure.step('Ввод кода подтверждения из письма')
    def send_code_to_code_field(self, code):
        self.send_keys_to_field(RecoveryPageLocators.CODE_FROM_MAIL, code)

    @allure.step('Нажатие кнопки "Сохранить"')
    def click_save_btn(self):
        self.click_on_element(RecoveryPageLocators.SAVE_BTN)

    @allure.step('Проверка активного состояния поля "Пароль"')
    def check_active_password_field(self, password):
        self.input_password_to_password_field(password)
        self.click_on_element(RecoveryPageLocators.SHOW_BTN)
        return self.check_element(RecoveryPageLocators.INPUT_FIELD_ACTIVE)

    @allure.step('Проверка наличия кнопки "Сохранить"')
    def check_save_btn(self):
        return self.check_element(RecoveryPageLocators.SAVE_BTN)
