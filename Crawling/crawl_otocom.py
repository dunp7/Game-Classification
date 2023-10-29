import csv
from otocom_crawl.Crawl import Crawling_tool
import time

# brand car

brand_car = ['Porsche','Huyndai','Honda','Kia','Ford','Mazda','Vinfast','Lexus','Chervolet','Nissan',\
             'Suzuki','Audi','Volvo','Volkswagen','Peugeot','BMW','Bentley']
# website
link = 'https://oto.com.vn'

# Features in the table
features = ['brand','name','price' ,'nam_sx' ,'origin' ,'type_car' ,\
            'km_traveled','gear' ,'condition','fuel','engine']

# file csv
csv_file = 'Predict Used Car/Crawling/raw_data/raw_data_crawled.csv'
with open(csv_file, mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header (column names)
    writer.writerow(features)
    print('Add header successfully')


# Crawling data

# website oto.com 
for brand_name in brand_car:
    tool = Crawling_tool()
    tool.crawling_data(brand_name,csv_file,link)
    time.sleep(20)

