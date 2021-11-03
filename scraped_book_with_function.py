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
    print(UPC)
    return UPC



def get_title():
    return soup.find_all("h1")
