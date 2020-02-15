from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:

    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    a = num1.text
    num2 = browser.find_element_by_id('num2')
    b = num2.text
    s = int(a) + int(b)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(s))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:

    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()

