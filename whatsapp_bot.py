from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

msg = input('enter mg : ')

num = int(input('enter num :'))

name = input('enter names : ')

names = name.split(",")


for i in names:
    user = driver.find_element(By.XPATH , f"//span[@title='{i}']")
    user.click()
    msg2 = driver.find_element(By.CLASS_NAME , "_13mgZ")
    for j in range (num) :
        msg2.send_keys(msg)
        driver.find_element(By.CLASS_NAME , "_3M-N-").click()