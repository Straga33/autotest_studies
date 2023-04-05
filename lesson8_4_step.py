from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    price_true = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    bottom_bm = browser.find_element(By.ID, 'book')
    bottom_bm.click()

    valuex_bm = browser.find_element(By.ID, 'input_value')
    x = valuex_bm.text
    y = calc(x)

    input_bm = browser.find_element(By.ID, 'answer')
    input_bm.send_keys(y)

    sub_bm = browser.find_element(By.ID, 'solve')
    sub_bm.click()
finally:
    time.sleep(10)
    browser.quit()





