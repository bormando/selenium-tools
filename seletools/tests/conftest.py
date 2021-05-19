import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1024,700")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
