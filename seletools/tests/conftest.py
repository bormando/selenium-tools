import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1024,700")
    dc = DesiredCapabilities.CHROME
    dc["goog:loggingPrefs"] = {"browser": "ALL"}
    browser = webdriver.Chrome(
        ChromeDriverManager().install(), options=options, desired_capabilities=dc
    )
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
