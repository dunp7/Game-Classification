from selenium import webdriver

class Crawl_tool():
    def __init__(self):
        #initial set up
        self.driver = webdriver.Chrome()

    def access(self,link):
        # Access the website
        self.driver.get(link)

    def quit(self):
        # Turn off the website
        self.driver.quit()