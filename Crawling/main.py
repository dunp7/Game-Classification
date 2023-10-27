from Crawl import Crawling_tool

# brand car
brand_car = ['Porsche','Huyndai','Honda','Kia','Ford','Mazda','Vinfast','Lexus','Chervolet',\
             'Nissan','Suzuki','Audi','Volvo','Volkswagen','Peugeot','BMW','Bentley']

# website
link = 'https://oto.com.vn'

# Features in the table
features = ['brand','name','price' ,'nam_sx' ,'origin' ,'type_car' ,'km_traveled','gear' ,'condition','fuel']

# file csv
csv_file = 'Predict Used Car/Crawling/raw_data_crawled.csv'
with open(csv_file, mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header (column names)
    writer.writerow(features)


# Crawling data

tool = Crawling_tool(link)
for brand_name in brand_car:
    tool.crawling_data(brand_name,csv_file)

tool.quit()