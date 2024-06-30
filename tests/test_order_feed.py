import allure
import pytest
from pages.main_page import HeaderPage
from pages.order_feed_page import OrderFeedPage
from locators.locators import OrderFeedLocators
from helpers.helpers import Order


class TestOrderFeedPage:

    @allure.title('Проверка модального окна с деталями заказа')
    def test_check_order_info_modal(self, driver):
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        feed_order.click_order_info()
        assert feed_order.check_order_info_modal()

    @allure.title('Проверка появления заказа в Ленте заказов')
    def test_check_user_orders_in_orders_history(self, driver, create_new_user, create_order, login):
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        user_order = str(order.get_user_orders_with_api(create_new_user))
        orders_history_in_feed = feed_order.get_orders_history()
        assert user_order in orders_history_in_feed

    @allure.title('Проверка изменения счетчика заказов')
    @pytest.mark.parametrize('counter',
                             [OrderFeedLocators.DAILY_ORDERS_COUNTER, OrderFeedLocators.TOTAL_ORDERS_COUNTER])
    def test_update_counter_orders(self, driver, create_new_user, login, counter):
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        actual_counter = int(feed_order.check_counter_orders(counter))
        order.create_order_with_api(create_new_user)
        new_counter = int(feed_order.check_counter_orders(counter))
        assert new_counter > actual_counter

    @allure.title('Проверка смены статуса заказа')
    def test_check_user_order_in_progress(self, driver, create_new_user, login):
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        order.create_order_with_api(create_new_user)
        orders_in_progress = feed_order.get_orders_in_progress()
        user_order = str(order.get_user_orders_with_api(create_new_user))
        assert user_order in orders_in_progress