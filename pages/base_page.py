from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Получение текущего URL страницы

    def get_current_url(self):
        return self.driver.current_url

    # Ожидание, пока элемент станет кликабельным
    def wait_for_element_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    # Ожидание, пока элемент будет присутствовать в DOM
    def wait_for_loading_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

    # Клик по элементу после ожидания его кликабельности
    def click_on_element(self, locator):
        self.wait_for_element_clickable(locator)
        self.driver.find_element(*locator).click()

    # Ввод текста в поле после ожидания его кликабельности
    def send_keys_to_field(self, locator, text):
        self.wait_for_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    # Получение текста элемента после ожидания его видимости
    def get_text_locator(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    # Получение списка текстов элементов после ожидания их видимости
    def get_text_locators(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    # Проверка отображения элемента на странице
    def check_element(self, locator):
        self.wait_for_loading_element(locator)
        return self.driver.find_element(*locator)

    # Проверка, что элемент не отображается на странице
    def check_element_is_not_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Перетаскивание элемента к целевому элементу
    def drag_and_drop(self, element_one, element_two):
        element = self.driver.find_element(*element_one)
        target = self.driver.find_element(*element_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    # Прокрутка к элементу и клик по нему
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
