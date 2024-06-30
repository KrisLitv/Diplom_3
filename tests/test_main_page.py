import allure
from data.urls import URLS, MainUrl
from pages.main_page import MainPage, HeaderPage



class TestMainPage:

    @allure.title('Переход на страницу конструктора при клике на «Конструктор»')
    def test_follow_to_constructor_page(self, driver):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        header.click_constructor_btn()
        assert main_page.check_constructor_form() and main_page.get_current_url() == MainUrl.MAIN_URL

    @allure.title('Закрытие всплывающего окна по клику на крестик')
    def test_close_fluorescent_bun_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_btn()
        main_page.close_popup_form()
        assert main_page.check_close_bun_form()

    @allure.title('Увеличение счетчика при добавлении ингредиента в заказ')
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.add_bun()
        assert int(main_page.check_counter_ingredient()) > 0


    @allure.title('Оформление заказа залогиненным пользователем')
    def test_create_order(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_constructor_btn()
        main_page.create_order()
        assert main_page.check_order_form()

    @allure.title('Переход на страницу ленты заказов при клике на «Лента заказов»')
    def test_follow_to_orders_feed_page(self, driver):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_feed_btn()
        assert main_page.check_orders_feed_form() and main_page.get_current_url() == (MainUrl.MAIN_URL + URLS.URL_FEED)

    @allure.title('Появление модального окна с подробностями при клике на ингредиент')
    def test_check_bun_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_btn()
        assert main_page.check_bun_form()

