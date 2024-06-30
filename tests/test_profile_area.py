import allure
from data.urls import URLS, MainUrl
from pages.main_page import HeaderPage
from pages.login_page import LoginPage
from pages.profile_area_page import ProfileAreaPage


class TestProfilelAreaPage:

    @allure.title('Переход в раздел "История заказов"')
    def test_switch_to_feed_orders(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        header.click_profile_area_btn()
        profile_area.click_history_orders_btn()
        assert profile_area.check_profile_area_form() and profile_area.get_current_url() == (MainUrl.MAIN_URL + URLS.URL_ORDER_HISTORY)

    @allure.title('Выход из личного кабинета')
    def test_log_out_profile(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        login_page = LoginPage(driver)
        header.click_profile_area_btn()
        profile_area.click_exit_btn()
        assert login_page.check_authorization_form() and login_page.get_current_url() == (MainUrl.MAIN_URL + URLS.URL_LOGIN)

    @allure.title('Переход в "Личный кабинет"')
    def test_switch_to_profile_area_page(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        header.click_profile_area_btn()
        assert profile_area.check_profile_area_form() and profile_area.get_current_url() == (MainUrl.MAIN_URL + URLS.URL_PROFILE)
