import os


def drag_and_drop(driver, source, target):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    f = open(os.path.join(__location__, "drag_and_drop.js"), "r")
    javascript = f.read()
    f.close()
    driver.execute_script(javascript, source, target)


def scroll_to_top(driver, element1, element2=None):
    if element2:
        driver.execute_script(
            """
                window.scrollTo(
                    0, 
                    arguments[0].offsetTop - arguments[1].offsetHeight
                )
            """,
            element1,
            element2
        )
    else:
        driver.execute_script("arguments[0].scrollIntoView(true)", element1)


def scroll_to_bottom(driver, element1, element2=None):
    driver.execute_script("arguments[0].scrollIntoView(false)", element1)
    if element2:
        driver.execute_script("window.scrollBy(0, arguments[0].offsetHeight)", element2)
