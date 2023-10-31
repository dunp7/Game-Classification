import csv
from otocom_crawl.Crawl import Crawling_link_tool,Crawling_data_tool
import time
import pickle
# brand car

brand_car = ['Porsche','Huyndai','Honda','Kia','Ford','Mazda','Vinfast','Lexus','Chervolet','Nissan',\
             'Suzuki','Audi','Volvo','Volkswagen','Peugeot','BMW','Bentley']
# website
link_web = 'https://oto.com.vn'

# Features in the table
features = ['brand','name','price' ,'nam_sx' ,'origin' ,'type_car' ,\
            'km_traveled','gear' ,'condition','fuel','engine']

# file csv

file_path = 'Predict Used Car/Data/link_crawled/saved_list.pkl'
csv_file = 'Predict Used Car/Data/Raw_data/raw_data_crawled_otocom.csv'
with open(csv_file, mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header (column names)
    writer.writerow(features)
    print('Add header successfully')
    
with open(file_path, 'wb') as file:
    pass

# Crawling data

# website oto.com 
# crawl link
link_cars = list()
for brand_name in brand_car:
    link_tool = Crawling_link_tool()
    brand_car_link = link_tool.find_all_link_cars(brand_name,link_web)
    link_cars.extend(brand_car_link)
    time.sleep(5)

with open(file_path, 'ab') as file:
    pickle.dump(link_cars,file)
    print('link has been saved')

# data_tool = Crawling_data_tool(file_path)
# data_tool.crawling_data(csv_file)

