from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# set driver
driver = webdriver.Chrome()
# access website https://oto.com.vn/
driver.get('https://oto.com.vn')

### Find product
car = []

# Find a box that need to find the product
search_email = driver.find_element(By.ID,"txtKeyword")
search_email.send_keys('Porsche')
search_email.send_keys(Keys.RETURN)

js_path = 'document.querySelector("#box-list-car > div.wrap-load-more.set-relative > span")'

nut_hien_thi_them = driver.find_element(By.CLASS_NAME,"btn-loadmore")
driver.execute_script(js_path,nut_hien_thi_them)
nut_hien_thi_them.click()

car_info = driver.find_elements(By.CLASS_NAME,'box-list-car')
for i in car_info:
    print(i.text)

time.sleep(25)


# Turn off the website
driver.quit()