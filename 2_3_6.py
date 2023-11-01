from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
try:    
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    txt1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = txt1.text
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    input1.send_keys(y)
	
	
	# Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла