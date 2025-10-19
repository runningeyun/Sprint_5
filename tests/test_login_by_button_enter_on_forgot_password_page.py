from locators import MainPage, LoginPage, ForgotPasswordPage
from helpers import login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLoginByButtonOnFrogotPasswordPage:
    def test_login_by_button_enter_on_forgot_password_page(self, driver):
        driver.get(ForgotPasswordPage.FORGOT_PASSWORD_URL)
        driver.find_element(*ForgotPasswordPage.FORGOT_PASSWORD_SIGHIN_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(LoginPage.LOGIN_HEADER))
        login(driver)
        assert driver.current_url == MainPage.MAIN_PAGE_URL
