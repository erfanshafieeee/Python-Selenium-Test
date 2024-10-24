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
    msg2 = driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div/p')
    for j in range (num) :
        msg2.send_keys(msg)
        driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button/span').click()

input()