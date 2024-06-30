import allure
from locators.locators import PersonalAreaLocators
from pages.base_page import BasePage


class ProfileAreaPage(BasePage):

    @allure.step('Проверка отображения формы личного кабинета')
    def check_profile_area_form(self):
        return self.check_element(PersonalAreaLocators.PROFILE_FORM)

    @allure.step('Нажать на кнопку "Профиль"')
    def click_profile_btn(self):
        self.click_on_element(PersonalAreaLocators.PROFILE_BTN)

    @allure.step('Нажать на кнопку "История заказов"')
    def click_history_orders_btn(self):
        self.click_on_element(PersonalAreaLocators.ORDER_HISTORY_BTN)

    @allure.step('Проверка отображения формы истории заказов')
    def check_history_form(self):
        return self.check_element(PersonalAreaLocators.HISTORY_ORDER_FORM)

    @allure.step('Нажать на кнопку "Выход"')
    def click_exit_btn(self):
        self.click_on_element(PersonalAreaLocators.EXIT_BTN)

    @allure.step('Нажать на кнопку "Отмена"')
    def click_cansel_btn(self):
        self.click_on_element(PersonalAreaLocators.EXIT_BTN)

    @allure.step('Нажать на кнопку "Сохранить"')
    def click_save_btn(self):
        self.click_on_element(PersonalAreaLocators.SAVE_BTN)

    @allure.step('Получить номер заказа из истории')
    def get_orders_number(self):
        return self.get_text_locator(PersonalAreaLocators.NUMBER_ORDER)