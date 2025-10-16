from locators import LoginPage, HeaderLocators, ProfilePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_logout_from_account(driver, login):
    driver.get(LoginPage.LOGIN_URL)
    login()
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ProfilePage.EXIT_BUTTON))
    driver.find_element(*ProfilePage.EXIT_BUTTON).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(LoginPage.LOGIN_HEADER))
    assert driver.current_url == LoginPage.LOGIN_URL
