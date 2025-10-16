from locators import RegistrationPage, LoginPage
from data import AccountData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_successful_registration(driver):
    driver.get(RegistrationPage.REGISTRATION_PAGE_URL)
    driver.find_element(*RegistrationPage.REGISTRATION_NAME_INPUT).send_keys(AccountData.new_correct_user['name'])
    driver.find_element(*RegistrationPage.REGISTRATION_EMAIL_INPUT).send_keys(AccountData.new_correct_user['email'])
    driver.find_element(*RegistrationPage.REGISTRATION_PASSWORD_INPUT).send_keys(AccountData.new_correct_user['password'])
    driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(LoginPage.LOGIN_HEADER))

    assert driver.current_url == LoginPage.LOGIN_URL
