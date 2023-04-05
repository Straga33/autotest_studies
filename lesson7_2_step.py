import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    valuex_bm = browser.find_element(By.ID, 'treasure')
    x = valuex_bm.get_attribute('valuex')
    y = calc(x)

    inp_bm = browser.find_element(By.ID, 'answer')
    inp_bm.send_keys(y)

    check_bm = browser.find_element(By.ID, 'robotCheckbox')
    check_bm.click()

    radio_bm = browser.find_element(By.ID, 'robotsRule')
    radio_bm.click()

    sub_bm = browser.find_element(By.CLASS_NAME, 'btn-default')
    sub_bm.click()

finally:
    time.sleep(10)
    browser.quit() 