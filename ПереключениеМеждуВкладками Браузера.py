from selenium import webdriver
import time
import math

def calc(x):
   return  math.log(abs(12*math.sin(x)))

try:

    link = "http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    #жмем кнопку в первом окне, чтобы открылось второе окно
    button.click()

    #переключаемся во второе окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #если надо переключиться обратно в первое окно, то его 
    #можно предварительно запомнить вот так:
    #first_window = browser.window_handles[0]

    x_element = browser.find_element_by_id('input_value')
    x = (int(x_element.text))
    result = calc(x)

    text_field = browser.find_element_by_id('answer')
    text_field.send_keys(str(result))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(70)
    # закрываем браузер после всех манипуляций
    browser.quit()


