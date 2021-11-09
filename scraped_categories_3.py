"""Appels de fonctions pour une catégorie"""
import requests
from bs4 import BeautifulSoup
import scraped_book_with_function as sbwf

url_category= 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html'
page = requests.get(url_category)
soup = BeautifulSoup(page.content, 'html.parser')

#ici on retrouve les urls des livres existants dans la rubrique d'une categorie

books_links = soup.select("h3")
for link in books_links:
    anchors=link.select("a")
    for anchor in anchors:
        print ("http://books.toscrape.com/" + anchor.get ("href").replace('../', ''))





"""def get_books_url_list(soup):
    book_url_list = soup.find_all("a", class_=)
    return book_url_list
print(get_books_url_list(soup))
"""

"""extraction de toutes les pages d'une catégorie"""
"""def get_all_categories_pages(category):

    i = 0
    while True:
        i = i + 1
        if i == 1:
            url_general= "http://books.toscrape.com/catalogue/category/books/" + category + "/index.html"
            return url_general
        else:
            url_general= "http://books.toscrape.com/catalogue/category/books/" + category + "/page-" + str(i) + ".html"  # concatenar
        page_general = requests.get(url_general)
        if page_general.status_code != 200:
            break
    return url_general
"""