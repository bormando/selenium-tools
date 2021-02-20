import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
