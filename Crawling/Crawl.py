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
brand_car = ['Porsche','Huyndai','Honda','Kia','Ford','Mazda','Vinfast','Lexus','Chervolet',\
             'Nissan','Suzuki','Audi','Volvo','Volkswagen','Peugeot','BMW','Bentley']

# Features in the table
features = ['brand','name','price' ,'nam_sx' ,'origin' ,'type_car' ,'km_traveled','gear' ,'condition','fuel']
# file csv
csv_file = 'Predict Used Car/Crawling/raw_data_crawled.csv'
with open(csv_file, mode='a', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header (column names)
    writer.writerow(features)


# Find a box that need to find the product
for i in brand_car:
    data = { 'brand': [],
    'name': [],
    'price' : [],
    'nam_sx' : [],
    'origin' : [],
    'type_car' : [],
    'km_traveled' : [],
    'gear' : [],
    'condition' :[],
    'fuel' : []
    }
    # search for each brand car
    search_box = driver.find_element(By.ID,"txtKeyword")
    search_box.send_keys(i)
    search_box.send_keys(Keys.RETURN)

    # scroll all the car on the page
    for count in range(20):
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
        except NoSuchElementException:
            # The button is not found, which means it no longer exists, so break out of the loop
            break
        except Exception as e:
            # Handle other exceptions if necessary
            print(f"An error occurred: {str(e)}")


    # find HTML class that all the information about car in it
    parent_element = driver.find_element(By.CLASS_NAME,"box-list-car")

    # find all the link of the car inside HTML class
    elements = parent_element.find_elements(By.CSS_SELECTOR,'a[href][class][title]')

    # Extract the href and access to each href
    href_links = [element.get_attribute("href") for element in elements]

# take all data for each features
    for href_link in href_links:
        driver.get(href_link)
        # get brand
        data['brand'].append(i)
        # get name
        try:
            data['name'].append(driver.find_element(By.CLASS_NAME,'title-detail').text)
        except:
            print("Error in get name")
            break
        # get price
        try:
             data['price'].append(driver.find_element(By.CLASS_NAME,'price').text)
        except:
            print("Error in get price")
            break

        # get all the information from the box which class is list-info
        try: 
            info_list = driver.find_element(By.CLASS_NAME,'list-info')
            elements = info_list.find_elements(By.CSS_SELECTOR,"li")
            for element in elements:
                label_text = element.find_element(By.CSS_SELECTOR, 'label.label').text
                if "Năm SX" in label_text:
                    data['nam_sx'].append(element.text.replace('\n', ' '))
                if "Kiểu dáng" in label_text:
                    data['type_car'].append(element.text.replace('\n', ' '))
                if "Tình trạng" in label_text:
                    data['condition'].append(element.text.replace('\n', ' '))
                if "Xuất xứ" in label_text:
                    data['origin'].append(element.text.replace('\n', ' '))
                if  "Km đã đi" in label_text:
                    data['km_traveled'].append(element.text.replace('\n', ' '))
                if "Hộp số" in label_text:
                    data['gear'].append(element.text.replace('\n', ' '))
                if "Nhiên liệu" in label_text:
                    data['fuel'].append(element.text.replace('\n', ' '))
            
        except:
            print("Error in get info_list")
        time.sleep(1)


    ## Read into file csv

    with open(csv_file, mode='a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header (column names)
        writer.writerow(data.keys())

        # Write the data
        rows = zip(*data.values())  # Transpose the data to align rows correctly
        writer.writerows(rows)

    print(f'{i} has been written to {csv_file}')

# Turn off the website
driver.quit()

