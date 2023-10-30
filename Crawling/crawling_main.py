import csv
from otocom_crawl.Crawl import Crawling_link_tool,Crawling_data_tool
import time
import pickle
# brand car

brand_car = ['Porsche','Huyndai','Honda','Kia','Ford','Mazda','Vinfast','Lexus','Chervolet','Nissan',\
             'Suzuki','Audi','Volvo','Volkswagen','Peugeot','BMW','Bentley']
# website
link = 'https://oto.com.vn'

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
    
with open(file_path, 'ab') as file:
    pass

# Crawling data

# website oto.com 
for brand_name in brand_car:
    link_tool = Crawling_link_tool()
    link_tool.add_links_into_file(brand_name,file_path,link)
    time.sleep(10)

# data_tool = Crawling_data_tool(file_path)
# data_tool.crawling_data(csv_file)

