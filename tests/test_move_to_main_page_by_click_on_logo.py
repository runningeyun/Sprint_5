from locators import MainPage, LoginPage, HeaderLocators, ProfilePage
from helpers import login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestMoveToMainPageByClickOnHeaderLogo:
    def test_move_to_main_page_by_click_on_header_logo(self, driver):
        driver.get(LoginPage.LOGIN_URL)
        login(driver)
        driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ProfilePage.EXIT_BUTTON))

        driver.find_element(*HeaderLocators.HEADER_LOGO).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(MainPage.MAIN_PAGE_HEADER_TEXT))
        assert driver.current_url == MainPage.MAIN_PAGE_URL
