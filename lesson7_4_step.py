from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math


link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_bm = browser.find_element(By.ID, 'input_value')
    x_bm_t = x_bm.text
    y = calc(x_bm_t)

    submit_bm = browser.find_element(By.CLASS_NAME, 'btn-primary')

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    check_bm = browser.find_element(By.ID, 'robotCheckbox')
    check_bm.click()

    rad_bm = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rad_bm)
    rad_bm.click()
    
    submit_bm.click()


finally:
    time.sleep(10)
    browser.quit()
    