from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import csv
# set driver

class Crawling_tool:
    def __init__(self, link):
        # access the website
        self.driver = webdriver.Chrome().get(link)

    def quit(self):
        # Turn off the website
        self.driver.quit()

    def input_the_brand_car(self,brand_name):
        search_box = driver.find_element(By.ID,"txtKeyword")
        search_box.send_keys(i)
        search_box.send_keys(Keys.RETURN)

    def loading_all_the_car(self):
        # scroll all the car on the page
        for count in range(20):
            try:
                # Find the "Hiển thị thêm" button
                nut_hien_thi_them = self.driver.find_element(By.CLASS_NAME, "btn-loadmore")
                if nut_hien_thi_them.is_enabled():
                    # Scroll to the element to make it visible
                    ActionChains(self.driver).move_to_element(nut_hien_thi_them).perform()           
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

    def find_all_link_cars(self):
        # find HTML class that all the information about car in it
        parent_element = self.driver.find_element(By.CLASS_NAME,"box-list-car")
        # find all the link of the car inside HTML class
        elements = parent_element.find_elements(By.CSS_SELECTOR,'a[href][class][title]')
        # Extract the href and access to each href
        href_links = [element.get_attribute("href") for element in elements]
        return href_links

    def add_information_into_csvfile(self,csv_file):
        ## Read into file csv
        with open(csv_file, mode='a', newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the header (column names)
            writer.writerow(data.keys())
            # Write the data
            rows = zip(*data.values())  # Transpose the data to align rows correctly
            writer.writerows(rows)

        print(f'{i} has been written to {csv_file}')

    def crawling_data(self,brand_name,csv_file):
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
        self.input_the_brand_car(brand_name)
        self.loading_all_the_car()
        href_links = self.find_all_link_cars()
        #take all data for each features
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

        self.add_information_into_csvfile(csv_file)

