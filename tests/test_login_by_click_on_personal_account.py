from locators import MainPage, LoginPage, HeaderLocators
from helpers import login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLoginByClickOnPersonalAccountHeader:
    def test_login_by_click_on_personal_account_header(self, driver):
        driver.get(MainPage.MAIN_PAGE_URL)
        driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(LoginPage.LOGIN_HEADER))
        login(driver)
        assert driver.current_url == MainPage.MAIN_PAGE_URL
