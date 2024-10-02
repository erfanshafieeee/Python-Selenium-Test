from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# راه‌اندازی مرورگر
driver = webdriver.Chrome()
driver.get('https://jobinja.ir/login/user')

# ورود اطلاعات کاربری
log_user = driver.find_element(By.NAME, 'identifier')
log_user.send_keys('erfanshafieeee@gmail.com')

log_pass = driver.find_element(By.NAME, 'password')
log_pass.send_keys('erfan5183')

log_enter = driver.find_element(By.CSS_SELECTOR, "[value='وارد شوید']")
log_enter.click()

# اعمال فیلترهای جستجو
submit = driver.find_element(By.NAME, 'button')
title_name = driver.find_element(By.NAME, 'filters[keywords][]')
title_name.send_keys('backend')
submit.click()

# انتخاب فیلترهای مختلف
checkbox_location = driver.find_element(By.XPATH, "//input[@name='filters[locations][0]']")
driver.execute_script("arguments[0].click();", checkbox_location)

checkbox_job = driver.find_element(By.XPATH, "//input[@name='filters[job_categories][1]']")
driver.execute_script("arguments[0].click();", checkbox_job)

checkbox_job_type = driver.find_element(By.XPATH, "//input[@value='1']")
driver.execute_script("arguments[0].click();", checkbox_job_type)

checkbox_job_type = driver.find_element(By.XPATH, "//input[@value='is_parttime']")
driver.execute_script("arguments[0].click();", checkbox_job_type)

checkbox_w_e = driver.find_element(By.XPATH, "//input[@value='under_two']")
driver.execute_script("arguments[0].click();", checkbox_w_e)

checkbox_w_e = driver.find_element(By.XPATH, "//input[@value='any']")
driver.execute_script("arguments[0].click();", checkbox_w_e)

time.sleep(5)

# پیدا کردن تمامی آگهی‌های فیلتر شده و مرور بر روی آنها
job_list = driver.find_elements(By.CSS_SELECTOR, "ul.o-listView__list li")

for i in range(len(job_list)):
    try:
        # پیدا کردن مجدد لیست آگهی‌ها پس از هر بار بازگشت به صفحه لیست
        job_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.o-listView__list li"))
        )
        
        # پیدا کردن لینک آگهی
        job_link = job_list[i].find_element(By.CSS_SELECTOR, "h2.c-jobListView__title a").get_attribute('href')
        
        # رفتن به صفحه آگهی
        driver.get(job_link)
        
        # اینجا می‌توانید کد اضافی برای استخراج اطلاعات صفحه آگهی بگذارید
        print(f"Visiting job: {job_link}")
        
        # توقف کوتاه قبل از بازگشت به صفحه‌ی لیست آگهی‌ها
        time.sleep(3)
        
        # بازگشت به صفحه‌ی لیست آگهی‌ها
        driver.back()
        
        # منتظر بارگذاری کامل لیست آگهی‌ها و یک عنصر مشخص از لیست آگهی‌ها
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.o-listView__list li h2.c-jobListView__title a")))
        
        # توقف کوتاه بعد از بازگشت به صفحه‌ی لیست
        time.sleep(2)
    
    except Exception as e:
        print(f"Error encountered: {e}")
        continue

# پیمایش تمام شد، حالا مرورگر در صفحه اصلی باقی می‌ماند
print("All jobs have been visited. Staying on the main page.")
input()