from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


link = 'http://suninjuly.github.io/selects2.html'

try:
    brouser = webdriver.Chrome()
    brouser.get(link)

    num_bm1 = brouser.find_element(By.ID, 'num1')
    num_bm2 = brouser.find_element(By.ID, 'num2')
    sum_bm = int(num_bm1.text) + int(num_bm2.text)
    print(sum_bm)

    select_bm = Select(brouser.find_element(By.ID, 'dropdown'))
    select_bm.select_by_visible_text(str(sum_bm))
    

    submit_bm = brouser.find_element(By.CLASS_NAME, 'btn-default')
    submit_bm.click()


finally:
    time.sleep(10)
    brouser.quit()
