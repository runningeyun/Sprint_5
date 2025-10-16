from locators import ProfilePage, HeaderLocators, LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_move_to_personal_account(driver, login):
    driver.get(LoginPage.LOGIN_URL)
    login()
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ProfilePage.EXIT_BUTTON))
    assert driver.current_url == ProfilePage.PROFILE_URL
