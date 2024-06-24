import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators
from locators.locators import HeaderPageLocators


class HeaderPage(BasePage):

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_constructor_btn(self):
        self.move_to_element_and_click(HeaderPageLocators.CONSTRUCTOR_BTN)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_feed_btn(self):
        self.move_to_element_and_click(HeaderPageLocators.ORDER_FEED_BTN)

    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_profile_area_btn(self):
        self.move_to_element_and_click(HeaderPageLocators.PERSONAL_ACCOUNT_BTN)


class MainPage(BasePage):

    @allure.step('Прокрутка к кнопке "Личный Кабинет" и нажатие на нее')
    def move_to_personal_account_btn_and_click(self):
        self.move_to_element_and_click(MainPageLocators.PERSONAL_ACCOUNT_BTN)

    @allure.step('Проверка формы конструктора')
    def check_constructor_form(self):
        return self.check_element(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Проверка формы ленты заказов')
    def check_orders_feed_form(self):
        return self.check_element(MainPageLocators.ORDER_FEED_FORM)

    @allure.step('Клик по кнопке "Булка"')
    def click_on_bun_btn(self):
        self.click_on_element(MainPageLocators.FLUORESCENT_BUN_BTN)

    @allure.step('Проверка отображения формы "Информации о булке"')
    def check_bun_form(self):
        return self.check_element(MainPageLocators.POPUP_FORM_INGREDIENTS)

    @allure.step('Проверка закрытия формы "Информация о булке"')
    def check_close_bun_form(self):
        return self.check_element_is_not_visible(MainPageLocators.POPUP_FORM_INGREDIENTS)

    @allure.step('Закрытие всплывающей формы с информацией об ингредиенте')
    def close_popup_form(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_POPUP_FORM)

    @allure.step('Добавление булки в корзину')
    def add_bun(self):
        self.wait_for_loading_element(MainPageLocators.FLUORESCENT_BUN_BTN)
        self.drag_and_drop(MainPageLocators.FLUORESCENT_BUN_BTN, MainPageLocators.ORDER_BASKET)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_place_order_button(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_bun()
        self.click_place_order_button()

    @allure.step('Проверка отображения формы "Оформление заказа"')
    def check_order_form(self):
        return self.check_element(MainPageLocators.ORDER_FORM)

    @allure.step('Получение номера оформленного заказа')
    def get_order_number(self):
        return self.get_text_locator(MainPageLocators.ORDER_NUM)

    @allure.step('Ожидание загрузки кнопки "Оформить заказ"')
    def wait_load_main_page(self):
        self.wait_for_loading_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Получение значения счетчика ингредиента')
    def check_counter_ingredient(self):
        return self.get_text_locator(MainPageLocators.COUNTER_INGREDIENT)

