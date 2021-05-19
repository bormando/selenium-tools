# Selenium Tools

### About package
There is a known drag & drop bug that reproduces in frameworks that use [webdriver](https://github.com/w3c/webdriver) to send commands to browser. 
This bug is a webdriver's issue and it's unknown when it's going to be fixed (or if it's going to be fixed at all). 
Current solution uses JavaScript code to simulate drag & drop action on web page. 
It works in most of the cases when it doesn't work in [Selenium](https://github.com/SeleniumHQ/selenium).

You may find bug description and current workaround [here](https://medium.com/python-pandemonium/how-to-bypass-selenium-drag-drop-bug-in-python-e33704a15761).

Thanks to [druska](https://gist.github.com/druska) for his [native js drag and drop helper](https://gist.github.com/druska/624501b7209a74040175).

Current package is called **Selenium Tools** for a reason - it will contain more features in future. Feel free to contribute.

### Installation
> pip install seletools

### Drag & Drop
```
from seletools.actions import drag_and_drop

driver = webdriver.Chrome()
source = driver.find_element(By.CSS_SELECTOR, "...")
target = driver.find_element(By.CSS_SELECTOR, "...")
drag_and_drop(driver, source, target)
```

### Scroll
This one helps to scroll vertically to any element on page, even if it's covered by some other element (like navbar or footer). If there's such obstacle - simply add that covering element into scrolling function as `element2`.
```
from seletools.actions import scroll_to_top, scroll_to_bottom

driver = webdriver.Chrome()
element1 = driver.find_element(By.CSS_SELECTOR, "...")
element2 = driver.find_element(By.CSS_SELECTOR, "...")  #optional, used only if you have obastacle (like navbar on footer) on top of the element that you need to scroll to

scroll_to_top(driver, element1, element2)
# OR
scroll_to_top(driver, element1)

scroll_to_bottom(driver, element1, element2)
# OR
scroll_to_bottom(driver, element1)
```

### Notes
Drag & Drop action worked with CSS selectors only a while ago. Now it also supports XPath selectors.