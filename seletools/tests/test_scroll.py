import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from seletools.actions import scroll_to_top, scroll_to_bottom


@pytest.mark.scroll
class TestScroll:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        driver.get("https://bormando.github.io/seletools-web-app/")

    def test_scroll_to_top_with_obstacle(self, driver):
        button = driver.find_element(By.CSS_SELECTOR, "button")
        navbar = driver.find_element(By.CSS_SELECTOR, ".top")
        scroll_to_top(driver, button, navbar)
        try:
            button.click()
        except WebDriverException:
            assert False, "Button click was interrupted"

    def test_scroll_to_bottom_with_obstacle(self, driver):
        button = driver.find_element(By.CSS_SELECTOR, "button")
        footer = driver.find_element(By.CSS_SELECTOR, ".bottom")
        scroll_to_bottom(driver, button, footer)
        try:
            button.click()
        except WebDriverException:
            assert False, "Button click was interrupted"
