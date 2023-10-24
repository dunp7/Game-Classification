from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
# set driver
driver = webdriver.Chrome()
# access website https://oto.com.vn/
driver.get('https://oto.com.vn')

### Find product
brand_car = ['Porsche']

# Find a box that need to find the product
search_email = driver.find_element(By.ID,"txtKeyword")
search_email.send_keys('Porsche')
search_email.send_keys(Keys.RETURN)


while True:
    try:
        # Find the "Hiển thị thêm" button
        nut_hien_thi_them = driver.find_element(By.CLASS_NAME, "btn-loadmore")
        
        if nut_hien_thi_them.is_enabled():
            # Scroll to the element to make it visible
            ActionChains(driver).move_to_element(nut_hien_thi_them).perform()
            
            # Click the button
            nut_hien_thi_them.click()
        else:
            # If the button is no longer enabled, break out of the loop
            break
    except Exception as e:
        # Handle exceptions if necessary
        print(f"An error occurred: {str(e)}")



parent_element = driver.find_element(By.CLASS_NAME,"box-list-car")
elements = parent_element.find_elements(By.CSS_SELECTOR,'a[href][class][title]')
# Extract the href and access to each href

href_links = [element.get_attribute("href") for element in elements]


for href_link in href_links:
    print(href_link)
    driver.get(href_link)
    time.sleep(1)

time.sleep(5)



# Turn off the website
driver.quit()