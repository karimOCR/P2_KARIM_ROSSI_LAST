"""Defintion de fonctions pour les catégories, et le site books.toscrape.com"""
import requests
from bs4 import beautifulsoup
import csv
import scraped_book

def get_url():
    requests.get




"""
def get_book(url):
    soup=get_page(url)
    return {
        "title": get_title(),
        "UPC": get_universal_product_code(),
        "Price_without_taxes": get_price_excluding_tax(),
        "Price_with_taxes": get_price_including_tax(),



    }
"""

"""Définition de fonctions pour extraire les informations d'un livre"""

def get_universal_product_code():
    return soup.select("td")[0].text

def get_product_page_url():
    return get.requests(url)

def get_title():
    return soup.find_all("h1")

def get_price_including_tax():
    return soup.select("td")[2].text

def get_price_excluding_tax():
    return soup.select("td")["3"].text



def get_category(url):

#def get_category_list():

#def get_site(url):
    #Obtenir les données de la page d'accueil
    page_accueil=get_page(http://books.toscrape.com/index.html)
    #Catégories_urls = Extract la liste des urls de chaque catégories dans la page d'accueil
    #Books_urls = Extract la liste des urls de chaque livres dans une

import requests
from bs4 import BeautifulSoup
import csv



def main(url):
    for csv in etl_list_names_categories(url):
        creation_csv(csv)

    names_categories = etl_list_names_categories(url)
    for page in etl_pages_category("https://books.toscrape.com/catalogue/category/books/travel_2/index.html"):
        etl_books_in_page(page)
        for books in etl_books_in_page(page):
            writer_data_book_csv(etl_book(books), names_categories[0])


def etl_list_names_categories(url_names_categories):#récupère les noms des catégories.
    page = requests.get(url_names_categories)
    soup = BeautifulSoup(page.content, 'html.parser')
    links_categories = soup.find('ul', class_="nav nav-list").find_all('a')
    list_links_categories_raw = []
    for category in links_categories:
        list_links_categories_raw.append(category.get('href'))
    # on va d'abord récupérer les liens des catégories
    del list_links_categories_raw[0]  # on supprime le premier lien inutile
    list_links_categories = []

    # on récupère le nom des catégories. pb, selon les noms, il y a soit les 2 caractères de la fin à enlever, soit 3.
    list_names_str = ','.join(list_links_categories_raw)
    str_names_without_star = list_names_str.replace("catalogue/category/books/","")  # on enlève d'abord la partie du lien de début
    str_names_without_end = str_names_without_star.replace("/index.html", "")  # puis la partie de lien de fin.
    names_with_number = str_names_without_end.split(',')
    first_names_without_number = []
    last_names_without_number = []
    names_first_part = names_with_number[0:7]  # on sépare la liste entre ceux qui ont 2 caractère à enlever et ceux qui ont 3.
    names_end_part = names_with_number[8:50]
    for name in names_first_part:  # on enlève les 2 derniers caractères de cette partie de la liste
        first_name_without_number = name[:-2]
        first_names_without_number.append(first_name_without_number)
    for name in names_end_part:
        last_name_without_number = name[:-3]  # on enlève les 3 derniers caractères de cette partie de la liste
        last_names_without_number.append(last_name_without_number)
    list_names = first_names_without_number + last_names_without_number  # on a enfin notre liste avec les noms de catégories!
    return list_names
