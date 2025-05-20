from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

msg = input('enter msg : ')

num = int(input('enter num :'))

name = input('enter names : ')

names = name.split(",")


for i in names:
    user = driver.find_element(By.XPATH , f"//span[@title='{i}']")
    user.click()
    for j in range(num):
        msg_place = driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
        msg_place.click()
        msg_place.send_keys(msg)
        time.sleep(2)
        send_key = driver.find_element(By.XPATH , '/html/body/div[1]/div/div/div[3]/div/div[4]/div/footer/div[1]/div/span/div/div[2]/div/div[4]/button')
        send_key.click()
input()
