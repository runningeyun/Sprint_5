from locators import RegistrationPage
from data import AccountData


def test_successful_registration(driver):
    driver.get(RegistrationPage.REGISTRATION_PAGE_URL)
    driver.find_element(*RegistrationPage.REGISTRATION_NAME_INPUT).send_keys(AccountData.new_correct_user['name'])
    driver.find_element(*RegistrationPage.REGISTRATION_EMAIL_INPUT).send_keys(AccountData.new_correct_user['email'])
    driver.find_element(*RegistrationPage.REGISTRATION_PASSWORD_INPUT).send_keys('123')
    driver.find_element(*RegistrationPage.REGISTRATION_BUTTON).click()

    assert driver.current_url == RegistrationPage.REGISTRATION_PAGE_URL and driver.find_element(*RegistrationPage.WRONG_PASSWORD)
