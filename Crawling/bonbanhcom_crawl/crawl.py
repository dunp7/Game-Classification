# from Crawl_tool import Crawl_tool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import re
class Crawl_tool:
    def __init__(self):
        #initial set up
        self.driver = webdriver.Chrome() 

    def access(self,link):
        # Access the website
        self.driver.get(link)

    def quit(self):
        # Turn off the website
        self.driver.quit()

class Crawl_link_tool(Crawl_tool):
    def __init__(self):
        super().__init__()


    def input_brand_name(self,brand_name):
        search_box = self.driver.find_element(By.CLASS_NAME,'text-input')
        search_box.send_keys(brand_name)
        search_box.send_keys(Keys.RETURN)
    
    def load_into_other_page(self,brand):
        # locate the > icon 
        while True:
            page = 1
            # try:
            next_icon = self.driver.find_element(By.XPATH,\
                    f'span.bbl.[url="https://bonbanh.com/oto/page,{page+1}?q={brand.lower()}"]')
            next_icon.click()
            page += 1
            # except:
            #     print('next icon is not available')
            #     break


if __name__ == '__main__':
    a = Crawl_link_tool()
    a.access('https://bonbanh.com')
    a.input_brand_name('Audi')
    a.load_into_other_page('Audi')