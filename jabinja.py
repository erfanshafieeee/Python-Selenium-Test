from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://jobinja.ir/login/user')
log_user=driver.find_element(By.NAME , 'identifier')
log_user.send_keys('erfanshafieeee@gmail.com')
log_pass=driver.find_element(By.NAME, 'password')
log_pass.send_keys('erfan5183')
log_enter = driver.find_element(By.CSS_SELECTOR, "[value='وارد شوید']")
log_enter.click()
input()