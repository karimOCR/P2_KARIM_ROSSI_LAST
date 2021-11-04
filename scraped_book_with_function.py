"""Defintion de fonctions pour les données d'un livre"""
import requests
from bs4 import BeautifulSoup


""" Creation et importer ses propres modules Python"""
#Module traitant des infos dans un livre
url='http://books.toscrape.com/catalogue/wall-and-piece_971/index.html'
page=requests.get(url)
soup= BeautifulSoup(page.content, 'html.parser')

def get_universal_product_code():
    UPC=soup.select("td")[0].text
    #print(UPC) #debug
    return UPC

def get_title():
    title=soup.find_all("h1")
    return title

print (get_universal_product_code ())


def get_notation(rev):
    if rev[1] == 'Four': return 4
    elif rev[1] == 'Three': return 3
    elif rev[1] == 'five': return 5
    elif rev[1] == 'two': return 2
    elif rev[1] == 'one': return 1

review = soup.find_all("p", class_="star-rating")[0].get("class")
print(get_notation(review))