from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()

class InstagramBot:
    def __init__(self,username , password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def quit(self):
        self.driver.quit()
    
    def login(self):
        self.driver.get('https://instagram.com')
        time.sleep(2)
        username = self.driver.find_element(By.XPATH , '//input[@name="username"]')
        username.clear()
        username.send_keys(self.username)

        password = self.driver.find_element(By.XPATH , '//input[@name="password"]')
        password.clear()
        password.send_keys(self.password)

        self.driver.find_element(By.XPATH , '//button[@type="submit"]').click()
        time.sleep(3000)
        self.driver.get('https://instagram.com/selenium_ww/')

user = 'erfan'
passwordd = '12345'

test = InstagramBot(user ,passwordd)
test.login()