from locators import MainPage, ConstructorLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestConstructorSections:
    """Проверка перехода к разделам "Булки", "Соусы", "Начинки"."""

    def test_buns_button(self, driver):
        driver.get(MainPage.MAIN_PAGE_URL)
        driver.find_element(*ConstructorLocators.TOPPINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ConstructorLocators.FIRST_TOPPING_INGREDIENT))
        driver.find_element(*ConstructorLocators.BUNS_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ConstructorLocators.FIRST_BUN_INGREDIENT))
        element = driver.find_element(*ConstructorLocators.FIRST_BUN_INGREDIENT)
        assert element.is_displayed()

    def test_sauces_button(self, driver):
        driver.get(MainPage.MAIN_PAGE_URL)
        driver.find_element(*ConstructorLocators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ConstructorLocators.FIRST_SAUCE_INGREDIENT))
        element = driver.find_element(*ConstructorLocators.FIRST_SAUCE_INGREDIENT)
        assert element.is_displayed()

    def test_toppings_button(self, driver):
        driver.get(MainPage.MAIN_PAGE_URL)
        driver.find_element(*ConstructorLocators.TOPPINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ConstructorLocators.FIRST_TOPPING_INGREDIENT))
        element = driver.find_element(*ConstructorLocators.FIRST_TOPPING_INGREDIENT)
        assert element.is_displayed()
