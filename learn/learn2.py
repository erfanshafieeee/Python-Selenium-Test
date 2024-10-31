from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://google.com')
driver.find_element(By.NAME, 'q').send_keys("hi")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()

time.sleep(2000)
driver.execute_script('window.scrollTo(0,700)')

input()
