from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://jobinja.ir/login/user

name = input("enter your user name : ")
password = input("enter your password : ")

log_user = driver.find_element(By.NAME, 'identifier')
log_user.send_keys(name)
log_pass = driver.find_element(By.NAME, 'password')
log_pass.send_keys(password)

log_enter = driver.find_element(By.XPATH, "//input[@type='submit']")
log_enter.click()


submit = driver.find_element(By.NAME, 'button')
title_name = driver.find_element(By.NAME, 'filters[keywords][]')
title_name.send_keys('backend')
submit.click()


checkbox_location = driver.find_element(By.XPATH, "//input[@name='filters[locations][0]']")
driver.execute_script("arguments[0].click();", checkbox_location)

checkbox_job = driver.find_element(By.XPATH, "//input[@name='filters[job_categories][1]']")
driver.execute_script("arguments[0].click();", checkbox_job)

# checkbox_job_type = driver.find_element(By.XPATH, "//input[@value='1']")
# driver.execute_script("arguments[0].click();", checkbox_job_type)

# checkbox_job_type = driver.find_element(By.XPATH, "//input[@value='is_parttime']")
# driver.execute_script("arguments[0].click();", checkbox_job_type)

# checkbox_w_e = driver.find_element(By.XPATH, "//input[@value='under_two']")
# driver.execute_script("arguments[0].click();", checkbox_w_e)

# checkbox_w_e = driver.find_element(By.XPATH, "//input[@value='any']")
# driver.execute_script("arguments[0].click();", checkbox_w_e)

time.sleep(5)


job_list = driver.find_elements(By.CSS_SELECTOR, "ul.o-listView__list li")

for i in range(len(job_list)):
    try:
        job_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.o-listView__list li"))
        )
        
        
        job_link = job_list[i].find_element(By.CSS_SELECTOR, "h2.c-jobListView__title a").get_attribute('href')
        
        
        driver.get(job_link)

        current_position = 0
        target_position = 2000
        scroll_step = 50  
        delay = 0.05 

        while current_position < target_position:
            driver.execute_script(f'window.scrollTo(0, {current_position});')
            current_position += scroll_step
            time.sleep(delay)

        driver.execute_script(f'window.scrollTo(0, {target_position});')
        
        print(f"Visiting job: {job_link}")
        
        time.sleep(3)
        
        driver.back()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.o-listView__list li h2.c-jobListView__title a")))
        
        time.sleep(2)
    
    except Exception as e:
        print(f"Error encountered: {e}")
        continue

print("All jobs have been visited. Staying on the main page.")
input()

