import requests
from bs4 import BeautifulSoup
import csv

""" Creation et importer ses propres modules Python"""
# Module traitant des infos dans un livre
# import scraped_book
# print(module_scraped_book)
# ETL Extract url
url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# ETL Extract universal_ product_code (upc)
upc = soup.select("td")[0].text
print(upc)
# ETL Extract the_Book_title
titre = soup.find_all("h1")
for e in titre:
    print(e.string)
# ETL EXTRACT product_type
product_type = soup.select("td")[1].text
print(product_type)
# ETL EXTRACT price_including_tax
price_incl_tax = soup.select("td")[2].text
print(price_incl_tax)
# ETL EXTRACT price_excluding_tax
price_excl_tax = soup.select("td")[3].text
print(price_excl_tax)
# ETL EXTRACT number_available
num_available = soup.select("td")[5].string
print(num_available)
# ETL EXTRACT product_description
product_description = soup.select("p")[3].text
print(product_description)
# ETL EXTRACT category
category = soup.select("a")[3].text
print(category)
# ETL EXTRACT review_rating
def get_notation(soup):
    review = soup.find_all("p", class_="star-rating")[0].get("class")

    if review[1] == 'Four':
        return 4
    elif review[1] == 'Three':
        return 3
    elif review[1] == 'Five':
        return 5
    elif review[1] == 'Two':
        return 2
    elif review[1] == 'One':
        return 1
    else:
        return 0
print(get_notation(soup))





#if review[1] == 'Four': print(4)
# a finir après revision des conditions


#print(review, 'on five')
# ETL EXTRACT image_url
image_url = soup.find("div", class_="item active").img["src"]
image_url = "http://books.toscrape.com/" + image_url.replace('../', '')
print(image_url)

dico_data_book = [{'Titre': titre[0].text,
                   'Universal product code': upc,
                   'Prix avec taxes': price_incl_tax,
                   'Prix sans taxes': price_excl_tax,
                   'Nombre disponible': num_available,
                   'Description du livre': product_description,
                   'Categorie': category,
                   'Note sur 5': get_notation(soup),
                   'Lien premiere page de couverture': image_url}]

csv_file = "table_data_book.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile,
                            fieldnames=['Titre', 'Universal product code', 'Prix avec taxes', 'Prix sans taxes',
                                        'Nombre disponible',
                                        'Description du livre', 'Categorie', 'Note sur 5',
                                        'Lien premiere page de couverture'])
    writer.writeheader()
    for data in dico_data_book:
        writer.writerow(data)
