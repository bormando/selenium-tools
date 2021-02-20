import os


def drag_and_drop(driver, source, target):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    f = open(os.path.join(__location__, "drag_and_drop.js"), "r")
    javascript = f.read()
    f.close()
    driver.execute_script(javascript, source, target)
