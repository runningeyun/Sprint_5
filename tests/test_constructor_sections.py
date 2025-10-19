import pytest
from locators import MainPage, ConstructorLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestConstructorSections:
    """Проверка перехода к разделам "Булки", "Соусы", "Начинки"."""

    @pytest.mark.parametrize(
            'toppings_click, button, ingredient',
            [
                [True, ConstructorLocators.BUNS_BUTTON, ConstructorLocators.FIRST_BUN_INGREDIENT],
                [False, ConstructorLocators.SAUCES_BUTTON, ConstructorLocators.FIRST_SAUCE_INGREDIENT],
                [False, ConstructorLocators.TOPPINGS_BUTTON, ConstructorLocators.FIRST_TOPPING_INGREDIENT]
            ]
        )
    def test_buns_button(self, driver, toppings_click, button, ingredient):
        driver.get(MainPage.MAIN_PAGE_URL)

        # Добавлена проверка на кнопку "Булки"
        # При открытии главной страницы по дефолту эта кнопка уже выбрана и не кликабельна
        # И чтобы получилось проверить эту кнопку необходимо переключиться на другую и затем снова нажать на неё
        if toppings_click:
            driver.find_element(*ConstructorLocators.TOPPINGS_BUTTON).click()
            WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ingredient))
            driver.find_element(*button).click()
        else:
            driver.find_element(*button).click()

        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(ingredient))
        element = driver.find_element(*ingredient)
        assert element.is_displayed()
