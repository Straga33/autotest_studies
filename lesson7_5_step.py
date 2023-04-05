import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/file_input.html'

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))


try: 
    browser = webdriver.Chrome()
    browser.get(link)

    inp_bm1 = browser.find_element(By.NAME, 'firstname')
    inp_bm1.send_keys("Pooh")

    inp_b21 = browser.find_element(By.NAME, 'lastname')
    inp_b21.send_keys("Vinny")

    inp_bm2 = browser.find_element(By.NAME, 'email')
    inp_bm2.send_keys("sdfs@ds.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'pp.txt')           # добавляем к этому пути имя файла 
    
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    sub_bm = browser.find_element(By.CLASS_NAME, 'btn-primary')
    sub_bm.click()

finally:
    time.sleep(10)
    browser.quit()