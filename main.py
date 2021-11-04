import requests
from bs4 import BeautifulSoup
import csv

""" Creation et importer ses propres modules Python"""
# Module traitant des infos dans un livre
#import module_scraped_book
#print(module_scraped_book)
#ETL Extract url
url='http://books.toscrape.com/catalogue/wall-and-piece_971/index.html'
page=requests.get(url)
soup= BeautifulSoup(page.content, 'html.parser')

#ETL Extract universal_ product_code (upc)
upc=soup.select("td")[0].text
print(upc)
#ETL Extract the_Book_title
titre=soup.find_all("h1")
for e in titre :
    print(e.string)
#ETL EXTRACT product_type
product_type=soup.select("td")[1].text
print(product_type)
#ETL EXTRACT price_including_tax
price_incl_tax=soup.select("td")[2].text
print(price_incl_tax)
#ETL EXTRACT price_excluding_tax
price_excl_tax=soup.select("td")[3].text
print(price_excl_tax)
#ETL EXTRACT number_available
num_available=soup.select("td")[5].string
print(num_available)
#ETL EXTRACT product_description
product_description=soup.select("p")[3].text
print(product_description)
#ETL EXTRACT category
category=soup.select("a")[3].text
print(category)
#ETL EXTRACT review_rating
review=soup.find_all("p", class_="star-rating")[0].get("class")[1]
print(review)
#ETL EXTRACT image_url
#image_url=soup.select("img src")
#print(image_url)