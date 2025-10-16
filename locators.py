from selenium.webdriver.common.by import By


class RegistrationPage:
    """URL и локаторы для формы регистрации"""

    REGISTRATION_PAGE_URL = 'https://stellarburgers.education-services.ru/register'
    REGISTRATION_NAME_INPUT = (By.XPATH, '//fieldset[1]//input[@name="name"]')  # Поле для ввода имени на странице регистрации
    REGISTRATION_EMAIL_INPUT = (By.XPATH, '//fieldset[2]//input[@name="name"]')  # Поле для ввода email на странице регистрации
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, '//fieldset[3]//input[@name="Пароль"]')  # Поле для ввода пароля на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"
    WRONG_PASSWORD = (By.XPATH, '//p[@class="input__error text_type_main-default"]')  # Надпись под полем "Пароль" при указании некорректного пароля при регистрации
    ENTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')  # Кнопка для перехода на страницу авторизации


class LoginPage:
    """URL и локаторы для страницы входа в аккаунт"""

    LOGIN_URL = 'https://stellarburgers.education-services.ru/login'
    LOGIN_HEADER = (By.XPATH, '//h2[text()="Вход"]')  # Заголовок страницы
    LOGIN_EMAIL_INPUT = (By.XPATH, '//fieldset[1]//input[@name="name"]')  # Поле для ввода имени на странице авторизации
    LOGIN_PASSWORD_INPUT = (By.XPATH, '//fieldset[2]//input[@name="Пароль"]')  # Поле для ввода пароля на странице авторизации
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # Кнопка "Войти"


class MainPage:
    """URL и локаторы главной страницы"""

    MAIN_PAGE_URL = 'https://stellarburgers.education-services.ru/'
    MAIN_PAGE_ENTER_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка для входа в аккаунт на главной странице
    MAIN_PAGE_HEADER_TEXT = (By.XPATH, '//h1[text()="Соберите бургер"]')  # Надпись "Соберите бургер" на главной странице


class ForgotPasswordPage:
    """URL и локаторы страницы восстановления пароля."""

    FORGOT_PASSWORD_URL = 'https://stellarburgers.education-services.ru/forgot-password'
    FORGOT_PASSWORD_SIGHIN_BUTTON = (By.XPATH, '//a[text()="Войти"]')  # Кнопка "Войти" на странице восстановления пароля


class HeaderLocators:
    """Локаторы в шапке страницы"""

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Кнопка "Личный Кабинет"
    HEADER_LOGO = (By.XPATH, '//*[contains(@class, "AppHeader_header__logo")]')  # Логотип "Stellar Burgers"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')  # Кнопка "Конструктор"


class ProfilePage:
    """URL и локаторы в личном кабинете"""

    PROFILE_URL = 'https://stellarburgers.education-services.ru/account/profile'
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # Кнопка выхода из профиля


class ConstructorLocators:
    """Локаторы для ингредиентов"""

    BUNS_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')  # Кнопка "Булки"
    SAUCES_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')  # Кнопка "Соусы"
    TOPPINGS_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')  # Кнопка "Начинки"
    FIRST_BUN_INGREDIENT = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/img')  # Первый ингредиент в разделе "Булки"
    FIRST_SAUCE_INGREDIENT = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]/img')  # Первый ингредиент в разделе "Соусы"
    FIRST_TOPPING_INGREDIENT = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[1]/img')  # Первый ингредиент в разделе "Начинки"
