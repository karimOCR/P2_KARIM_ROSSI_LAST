"""Appels de fonctions pour une catégorie"""
import requests
from bs4 import BeautifulSoup
import scraped_book_with_function as sbwf
#from scraped_book_with_function import * #danger car possibilité de conflit

#Création d'une nouvelle soup appelée "soup_categories" dans laquelle on retrouve que les urls des categories


url_category = 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html'
page = requests.get(url_category)
soup = BeautifulSoup(page.content, 'html.parser')

#ici on retrouve les urls existantes dans la rubrique categorie
soup_category = soup.find(class_="nav")
for link in soup_category.find_all("a"):
    print(link.get('href'))
#print(soup_category)
print (type (soup_category.find_all("a")))

def get_all_categories_urls():
    all_categories_urls=soup.find_all("a")
    return all_categories_urls
#print(get_all_categories_urls())




def get_categories_urls(soup):
    categories_urls= soup.find_all(class_="nav")
    for element in categories_urls.find_all("a"):
        print(element.get("href"))
    return (categories_urls)
#print(get_soup_for_categories(soup))
#get_categories_urls(soup)





