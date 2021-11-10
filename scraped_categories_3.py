"""Appels de fonctions pour une catégorie"""
import requests
from bs4 import BeautifulSoup
import scraped_book_with_function as sbwf

url_category= 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html'
page = requests.get(url_category)
soup = BeautifulSoup(page.content, 'html.parser')

#ici on retrouve les urls des livres existants dans la rubrique d'une categorie
def get_books_links(soup):
    books_links = []
    temp = soup.select("h3")
    for link in temp:
        anchors=link.select("a")
        for anchor in anchors:
            books_links.append("http://books.toscrape.com/" + anchor.get ("href").replace('../', ''))
    return books_links

#ici on extrait le lien next et on denombre le nombre de page par des boucles

print (url_category)
print(get_books_links(soup))

next_page = soup.find("li", "next")

while next_page:
    next_page_url = url_category.replace("index.html", "") + next_page.a["href"]
    print (next_page_url)
    actual_page_in_cat = requests.get(next_page_url)
    soup = BeautifulSoup(actual_page_in_cat.content, 'html.parser')
    next_page = soup.find("li", "next")
    print (get_books_links(soup))

"""
request = requests.get(next_page_url)
print(requests)
soup_books = soup.find_all("article", "product_pod")"""


"""
urls = url.replace("index.html", "")
    while next_page:
        url_next_page = urls + next_page.a["href"]
        request = requests.get(url_next_page)
        html = request.content
        soup = BeautifulSoup(html, features="html.parser")
        soup_books = soup.find_all("article", "product_pod")
        for i in soup_books:
            url_book = i.a["href"].replace("../", "")
            urls_books.append(url_book)
        next_page = soup.find("li", "next")
    print(urls_books, category)
    #return urls_books, category
"""

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
    return url_general"""
