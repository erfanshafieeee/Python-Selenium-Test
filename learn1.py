from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://google.com')
driver.find_element(By.NAME, 'q').send_keys("hi"+Keys.ENTER)


input()
