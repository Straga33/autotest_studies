import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'https://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    
    input11 = browser.find_element(By.CLASS_NAME, 'form-control')
    input11.send_keys(y)

    check_bm = browser.find_element(By.ID, 'robotCheckbox')
    check_bm.click()

    radio_bm = browser.find_element(By.ID, 'robotsRule')
    radio_bm.click()

    but_bm = browser.find_element(By.CLASS_NAME, 'btn-default')
    but_bm.click()


finally:
    time.sleep(30)
    browser.quit() 