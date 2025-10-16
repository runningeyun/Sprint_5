import pytest
from selenium import webdriver
from data import AccountData
from locators import LoginPage, MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    def _login():
        driver.find_element(*LoginPage.LOGIN_EMAIL_INPUT).send_keys(AccountData.existing_user['email'])
        driver.find_element(*LoginPage.LOGIN_PASSWORD_INPUT).send_keys(AccountData.existing_user['password'])
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(MainPage.MAIN_PAGE_HEADER_TEXT))
        return driver
    return _login
