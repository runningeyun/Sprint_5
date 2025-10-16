from locators import RegistrationPage, MainPage, LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_login_by_botton_enter_on_registration_page(driver, login):
    driver.get(RegistrationPage.REGISTRATION_PAGE_URL)
    driver.find_element(*RegistrationPage.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(LoginPage.LOGIN_HEADER))
    login()
    assert driver.current_url == MainPage.MAIN_PAGE_URL
