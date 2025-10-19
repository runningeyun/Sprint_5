from locators import MainPage, LoginPage
from helpers import login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLoginByButtonEnterOnMainPage:
    def test_login_by_button_enter_on_main_page(self, driver):
        driver.get(MainPage.MAIN_PAGE_URL)
        driver.find_element(*MainPage.MAIN_PAGE_ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(LoginPage.LOGIN_HEADER))
        login(driver)
        assert driver.current_url == MainPage.MAIN_PAGE_URL
