from data.ingredients import Ingredients
from data.urls import MainUrl, Endpoints
import requests
import allure


class Order:

    @allure.step('Генерация нового заказа через API')
    def create_order_with_api(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        requests.post(MainUrl.MAIN_URL + Endpoints.CREATE_ORDER_ENDPOINT, headers=headers,
                      data=Ingredients.correct_ingredients_data)

    @allure.step('Получение заказов через API')
    def get_user_orders_with_api(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        response = requests.get(MainUrl.MAIN_URL + Endpoints.GET_ORDERS_ENDPOINT, headers=headers)
        return response.json()["orders"][0]["number"]
