def get_value(driver, key):
    return driver.execute_script(
        "return window.localStorage.getItem(arguments[0])", key
    )


def set_value(driver, key, value):
    return driver.execute_script(
        "return window.localStorage.setItem(arguments[0], arguments[1])", key, value
    )
