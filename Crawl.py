from selenium import webdriver
from selenium.webdriver.common.by import By

# set driver
driver = webdriver.Chrome()
# access website baomoi.com
driver.get('https://baomoi.com')

data = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[3]/div/div')
for i in data:
    print(i.text)
driver.quit()