from locators import ProfilePage, HeaderLocators, LoginPage
from helpers import login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestMoveToPersonalAccount:
    def test_move_to_personal_account(self, driver):
        driver.get(LoginPage.LOGIN_URL)
        login(driver)
        driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ProfilePage.EXIT_BUTTON))
        assert driver.current_url == ProfilePage.PROFILE_URL
