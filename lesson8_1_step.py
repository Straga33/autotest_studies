from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit_bm = browser.find_element(By.TAG_NAME, 'button')
    submit_bm.click()

    alert_bm = browser.switch_to.alert
    alert_bm.accept()

    valuex_bm = browser.find_element(By.ID, 'input_value')
    x = valuex_bm.text
    y = calc(x)

    input_bm = browser.find_element(By.ID, 'answer')
    input_bm.send_keys(y)

    sub_bm = browser.find_element(By.CLASS_NAME, 'btn-primary')
    sub_bm.click()

finally:
    time.sleep(10)
    browser.quit()

