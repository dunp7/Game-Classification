from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import csv
# set driver
driver = webdriver.Chrome()
# access website https://oto.com.vn/
driver.get('https://oto.com.vn')

### Find product
brand_car = ['Porsche','Huyndai']

# Features in the table
data = { 'name': [],
'price' : [],
'nam_sx' : [],
'origin' : [],
'type_car' : [],
'km_traveled' : [],
'gear' : [],
'condition' :[],
'fuel' : []
}


# Find a box that need to find the product
for i in brand_car:
    # search for each brand car
    search_box = driver.find_element(By.ID,"txtKeyword")
    search_box.send_keys(i)
    search_box.send_keys(Keys.RETURN)

    # scroll all the car on the page
    # while True:
    #     try:
    #         # Find the "Hiển thị thêm" button
    #         nut_hien_thi_them = driver.find_element(By.CLASS_NAME, "btn-loadmore")
    #         print(nut_hien_thi_them)
    #         if nut_hien_thi_them.is_enabled():
    #             # Scroll to the element to make it visible
    #             ActionChains(driver).move_to_element(nut_hien_thi_them).perform()           
    #             # Click the button
    #             nut_hien_thi_them.click()
    #         else:
    #             # If the button is no longer enabled, break out of the loop
    #             break
    #     except NoSuchElementException:
    #         # The button is not found, which means it no longer exists, so break out of the loop
    #         break
    #     except Exception as e:
    #         # Handle other exceptions if necessary
    #         print(f"An error occurred: {str(e)}")


    # find HTML class that all the information about car in it
    parent_element = driver.find_element(By.CLASS_NAME,"box-list-car")

    # find all the link of the car inside HTML class
    elements = parent_element.find_elements(By.CSS_SELECTOR,'a[href][class][title]')

    # Extract the href and access to each href
    href_links = [element.get_attribute("href") for element in elements]

# take all data for each features
    for href_link in href_links:
        driver.get(href_link)
        # get name
        try:
            data['name'].append(driver.find_element(By.CLASS_NAME,'title-detail').text)
        except:
            print("Error in get name")
        # get price
        try:
             data['price'].append(driver.find_element(By.CLASS_NAME,'price').text)
        except:
            print("Error in get price")
        # get nam_sx
        try:
            data['nam_sx'].append(driver.find_element(By.CLASS_NAME,'price').text)
        except:
            print("Error in nam_sx")
        # get origin
        try:
            data['origin'].append(driver.find_element(By.CLASS_NAME,'price').text)
        except:
            print("Error in Origin")
        # get type_car 
        try:
            data['type_car'].append(driver.find_element(By.CLASS_NAME,'price').text)
        except:
            print("Error in type_car")
        # get km_traveled 
        try:
            data['km_traveled'].append(driver.find_element(By.CLASS_NAME,'price').text)
        except:
            print("Error in km_traveled")
        # get gear 
        try:
            data['gear'].append(driver.find_element(By.CLASS_NAME,'price').text)
        except:
            print("Error in get gear")
        # get condition
        try:
            data['condition'].append(driver.find_element(By.CLASS_NAME,'price').text)
        except:
            print("Error in get condition")
        # get fuel
        try:
            data['fuel'].append(driver.find_element(By.CLASS_NAME,'price').text)
        except:
            print("Error in get fuel")
        time.sleep(1)

# file csv
data_file = 'Predict Used Car/raw_data_crawled.csv'

with open(data_file,mode='w', newline= '') as f:
    writer = csv.DictWriter(f, fieldnames= data.keys())
    writer.writeheader()
    # Write the data to the CSV file
    writer.writerows(data)

# Turn off the website
driver.quit()

print(data)