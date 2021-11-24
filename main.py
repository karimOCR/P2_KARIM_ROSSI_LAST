"""extraire toutes les categories de livres disponibles"""
"""extraire dans un csv distinct par catégorie tous les livres de toutes les catégories"""
"""télécharger et enregistrer dans un dossier tous les fichiers image de chaque livre"""
import requests
from bs4 import BeautifulSoup
import csv
import os
#from scraped_category import *
#import scraped_book_with_function as sbwf
import P2_01_scraped_book_and_category_wiith_functions as sbwf
import time

start = time.time()
print("hello")


url_all_categories = "http://books.toscrape.com/index.html"
page = requests.get(url_all_categories)
soup = BeautifulSoup(page.content, 'html.parser')

"""P2_cover_images_directory = "./P2_06_scraped_Books_images"
if not os.path.exists(P2_cover_images_directory):
    os.mkdir(P2_cover_images_directory)
reponse = requests.get(cover_book, allow_redirects=True)
picture_file = ()"""

"""Création du dossier dans lequel on va stocker les miniatures"""
P2_cover_images_directory = "./P2_06_scraped_books_images"
if not os.path.exists(P2_cover_images_directory):
    os.mkdir(P2_cover_images_directory)

"""Création du dossier dans lequel on va stocker les fichiers .csv"""
P2_06_csv_files_directory = "./P2_06_csv_files_directory"
if not os.path.exists(P2_06_csv_files_directory):
    os.mkdir(P2_06_csv_files_directory)


"""ici on crée une première soupe pour récuperer l'url de toutes les catégorie dans une liste"""
url_of_each_category = soup.find('ul', class_="nav nav-list").find_all('a')
list_url = []
for category in url_of_each_category:
    list_url.append("http://books.toscrape.com/"+category.get('href'))

list_url.pop(0)# suppression du premier lien qui renvoie à la page d'accueil appelé "Books".
#print(list_url)

"""ici on crée la deuxième soupe pour récuperer le contenu  de la première page de la catégorie"""
for each_url_of_category in list_url:
    category_page = requests.get(each_url_of_category)
    category_soup = BeautifulSoup(category_page.content, 'html.parser')

    """recuperer le nom de la catégorie pour l'attribuer à chaque fichier csv"""
    categorie_name = category_soup.find("div", class_="page-header action").find("h1").text

    """creer ici le csv d'une categorie dans le dossier préalablement créé """
    csv_filename = "P2_06_csv_files_directory/"+ categorie_name+".csv"
    csv_categorie = open(csv_filename,"w")

    """on écrit les en-têtes du fichier .csv"""
    writer = csv.DictWriter(csv_categorie, fieldnames=['Titre', 'Universal product code', 'Prix avec taxes',
                                                 'Prix sans taxes', 'Nombre disponible', 'Description du livre',
                                                 'Categorie', 'Note sur 5', 'Lien premiere page de couverture'])
    writer.writeheader()

    """ici on crée la soupe la premiere page d'une catégorie"""
    for book_link in get_books_links(category_soup):
        page_of_book = requests.get(book_link)
        book_soup = BeautifulSoup(page_of_book.content, 'html.parser')

        """ici on récupere le lien de l'image de couverture"""
        image_link = sbwf.get_image_url(book_soup)
        #print(image_link)
        """ici on télécharge la miniature de  la première page dont nous connaissons l'adresse"""
        response = requests.get(image_link, stream=True)
        with open("P2_06_scraped_books_images/" + image_link.split("/")[7], "wb") as file:
            file.write(response.content)
        """ici on écrit les infos relatives au livre"""
        dico_data_book = {'Titre': sbwf.get_title(book_soup),
                          'Universal product code': sbwf.get_universal_product_code(book_soup),
                          'Prix avec taxes': sbwf.get_price_incl_tax(book_soup),
                          'Prix sans taxes': sbwf.get_price_excl_tax(book_soup),
                          'Nombre disponible': sbwf.get_num_available(book_soup),
                          'Description du livre': sbwf.get_product_description(book_soup),
                          'Categorie': sbwf.get_category(book_soup),
                          'Note sur 5': sbwf.get_notation(book_soup),
                          'Lien premiere page de couverture': sbwf.get_image_url(book_soup)}
        writer.writerow(dico_data_book)

    """ici on recupère la soupe des pages suivantes de la catégorie"""
    next_page = category_soup.find("li", "next")
    while next_page:
        next_page_url = each_url_of_category.replace("index.html", "") + next_page.a["href"]

        actual_page_in_cat = requests.get(next_page_url)
        soup = BeautifulSoup(actual_page_in_cat.content, 'html.parser')
        next_page = soup.find("li", "next")

        for book_link in get_books_links(soup):
            page_of_book = requests.get(book_link)
            book_soup = BeautifulSoup(page_of_book.content, 'html.parser')

            """ici on récupere le lien de l'image de couverture"""
            image_link = sbwf.get_image_url(book_soup)

            """ici on télécharge la miniature des pages suivantes dont nous connaissons l'adresse"""
            response = requests.get(image_link, stream = True)
            with open("P2_06_scraped_books_images/" + image_link.split("/")[7], "wb") as file:
                file.write(response.content)
            """ici on écrit les infos relatives au livre"""
            dico_data_book = {'Titre': sbwf.get_title(book_soup),
                              'Universal product code': sbwf.get_universal_product_code(book_soup),
                              'Prix avec taxes': sbwf.get_price_incl_tax(book_soup),
                              'Prix sans taxes': sbwf.get_price_excl_tax(book_soup),
                              'Nombre disponible': sbwf.get_num_available(book_soup),
                              'Description du livre': sbwf.get_product_description(book_soup),
                              'Categorie': sbwf.get_category(book_soup),
                              'Note sur 5': sbwf.get_notation(book_soup),
                              'Lien premiere page de couverture': sbwf.get_image_url(book_soup)}
            writer.writerow(dico_data_book)

    csv_categorie.close()

end = time.time()
second = end - start
minute = second / 60
second = second - int (minute)*60
print(str(int (minute))+" minutes "+str(int (second))+" secondes")