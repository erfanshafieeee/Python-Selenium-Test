from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://jobinja.ir/login/user')

# ورود اطلاعات کاربری
log_user = driver.find_element(By.NAME, 'identifier')
log_user.send_keys('erfanshafieeee@gmail.com')

log_pass = driver.find_element(By.NAME, 'password')
log_pass.send_keys('erfan5183')

log_enter = driver.find_element(By.CSS_SELECTOR, "[value='وارد شوید']")
log_enter.click()

submit = driver.find_element(By.NAME, 'button')

title_name = driver.find_element(By.NAME, 'filters[keywords][]')
title_name.send_keys('backend')
submit.click()

checkbox_location = driver.find_element(By.XPATH, "//input[@name='filters[locations][0]']")
driver.execute_script("arguments[0].click();", checkbox_location)

checkbox_job = driver.find_element(By.XPATH, "//input[@name='filters[job_categories][1]']")
driver.execute_script("arguments[0].click();", checkbox_job)

checkbox_job_type = driver.find_element(By.XPATH, "//input[@value='1']")
driver.execute_script("arguments[0].click();", checkbox_job_type)

checkbox_job_type = driver.find_element(By.XPATH, "//input[@value='is_parttime']")
driver.execute_script("arguments[0].click();", checkbox_job_type)

checkbox_w_e = driver.find_element(By.XPATH, "//input[@value = 'under_two']")
driver.execute_script("arguments[0].click();", checkbox_w_e)

checkbox_w_e=driver.find_element(By.XPATH ,"//input[@value = 'any']")
driver.execute_script("arguments[0].click();", checkbox_w_e)

checkbox_w_e=driver.find_element(By.XPATH ,"//input[@value = ':']")
driver.execute_script("arguments[0].click();", checkbox_w_e)

input()
