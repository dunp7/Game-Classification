from selenium import webdriver
from Crawling.crawl_tool import Crawling_tool
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import csv

# create link_car.csv
link_car = 'all_link_cars.csv'
with open(file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([])

# link
link = 'https://oto.com.vn'

class Crawling_link_tool(Crawling_tool):
    def __init__(self):
        #initial set up
        self.driver = webdriver.Chrome()

    def access(self,link):
        # Access the website
        self.driver.get('https://oto.com.vn')

    def quit(self):
        # Turn off the website
        self.driver.quit()

    def input_the_brand_car(self,brand_name):
        search_box = self.driver.find_element(By.ID,"txtKeyword")
        search_box.send_keys(brand_name)
        search_box.send_keys(Keys.RETURN)

    def loading_all_the_available_car(self):
        # scroll all the car on the page (limit 20 times)
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
            time.sleep(1)
            self.driver.set_page_load_timeout(5)

    def find_all_link_cars(self):
        # find HTML class that all the information about car in it
        parent_element = self.driver.find_element(By.CLASS_NAME,"box-list-car")
        # find all the link of the car inside HTML class
        elements = parent_element.find_elements(By.CSS_SELECTOR,'a[href][class][title]')
        # Extract the href and access to each href
        href_links = [element.get_attribute("href") for element in elements]
        return href_links

    def save_link_into_csvfile(self,csv_file,link,brand):
        ## Read into file csv
        with open(csv_file, mode='a', newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the data
            writer.writerows(link)
        print(f'link {brand} has been written to {csv_file}')
    
    def crawl_link_cars(csv_file,link,brand):
        self.access

class Crawling_features_tool:
    def __init__(self):
        pass



if __name__ == 'main':
    pass