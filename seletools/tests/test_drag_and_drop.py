from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop


def test_drag_and_drop(driver):
    driver.get("http://the-internet.herokuapp.com/drag_and_drop")
    source = driver.find_element(By.CSS_SELECTOR, "#column-a")
    target = driver.find_element(By.CSS_SELECTOR, "#column-b")
    drag_and_drop(driver, source, target)
    assert source.text == 'B' and target.text == 'A', F"Source text is should be 'B' and target text should be 'A'"
