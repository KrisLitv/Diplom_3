from selenium.webdriver.common.by import By

class HeaderPageLocators:
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
    ORDER_FEED_BTN = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")


class MainPageLocators:
    ORDER_FEED_FORM = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")
    CONSTRUCTOR_FORM = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    FLUORESCENT_BUN_BTN = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
    CLOSE_POPUP_FORM = (By.XPATH, '//button[contains(@class,"close")]')
    COUNTER_INGREDIENT = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    ORDER_FORM = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")
    ORDER_BUTTON = By.XPATH, '//button[contains(text(),"Оформить заказ")]'
    ORDER_BASKET = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    ORDER_NUM = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    POPUP_FORM_INGREDIENTS = (By.XPATH, "//h2[text()= 'Детали ингредиента']")


class AuthPageLocators:
    AUTH_FORM = (By.XPATH, ".//div[@class = 'Auth_LOGIN_ENDPOINT__3hAey']")
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    LOGIN_ENDPOINT_ACCOUNT_BTN = (By.XPATH, "//button[text() = 'Войти']")
    REGISTRATION_BTN = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    RECOVER_BTN = (By.XPATH, "//a[text() = 'Восстановить пароль']")


class RecoveryPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    RECOVER_BTN = (By.XPATH, ".//button[text() = 'Восстановить']")
    LOGIN_ENDPOINT_ACCOUNT_BTN = (By.XPATH, ".//a[text() = 'Войти']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Введите новый пароль']")
    CODE_FROM_MAIL = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")
    RECOVERY_TEXT_FORM = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")
    SHOW_BTN = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    INPUT_FIELD_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")


class PersonalAreaLocators:
    PROFILE_FORM = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")
    PROFILE_BTN = (By.XPATH, ".//a[text() = 'Профиль']")
    ORDER_HISTORY_BTN = (By.XPATH, ".//a[text() = 'История заказов']")
    HISTORY_ORDER_FORM = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")
    NUMBER_ORDER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    CANCEL_BTN = (By.XPATH, ".//button[text() = 'Отмена']")
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")
    EXIT_BTN = (By.XPATH, ".//button[text() = 'Выход']")


class OrderFeedLocators:
    TITLE_ORDERS_LIST = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDERS_INFO = (By.XPATH, '//p[text()="Cостав"]')
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_ORDER_IN_JOB = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
    ORDER_INFO_WINDOW = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
    ORDER_HISTORY = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
