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
        #self.driver.get('https://instagram.com/selenium_ww/')



    def like(self , hs, num):
        hashtag = hs.split(',')
        for i in range(len(hashtag)):
            self.driver.get(f'https://instagram.com/explore/tags/{hashtag[i]}')
            link_2 = []

            for j in range(num):
                link = self.driver.find_elements(By.TAG_NAME , 'a')
                link_2 = [l.get_attribute('herf') for l in link if 'com/p/' in l.get_attribute('herf')]
                for i in range(len(link_2)):
                    self.driver.get(link_2[i])
                    self.driver.find_element(By.CLASS_NAME , 'wp0fb') . click()
                    time.sleep(random.randint(1 , 6))


user = 'erfanyofski'
passwordd = 'erfan5183'

test = InstagramBot(user ,passwordd)
test.login()
test.Like('python , linux')