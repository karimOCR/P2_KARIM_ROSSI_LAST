"""Appels de fonctions pour une catégorie"""
import csv
import requests
from bs4 import BeautifulSoup
import scraped_book_with_function as sbwf


url_category = 'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html'
page = requests.get(url_category)
soup = BeautifulSoup(page.content, 'html.parser')


# ici on retrouve les urls des livres existants dans la rubrique d'une categorie
def get_books_links(soup):
    books_links = []
    temp = soup.select("h3")
    for link in temp:
        anchors = link.select("a")
        for anchor in anchors:
            books_links.append("http://books.toscrape.com/catalogue/" + anchor.get("href").replace('../', ''))

    return books_links


# ici on extrait le lien next et on denombre le nombre de page par des boucles

#print(url_category)
#print(get_books_links(soup))

next_page = soup.find("li", "next")

csv_file = "All_books_of_category.csv"
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Titre', 'Universal product code', 'Prix avec taxes', 'Prix sans taxes',
                                            'Nombre disponible',
                                            'Description du livre', 'Categorie', 'Note sur 5',
                                            'Lien premiere page de couverture'])
    writer.writeheader()

    for book_link in get_books_links(soup):
        page_of_book = requests.get(book_link)
        book_soup = BeautifulSoup(page_of_book.content, 'html.parser')

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

    while next_page:
        next_page_url = url_category.replace("index.html", "") + next_page.a["href"]
        #print(next_page_url)
        actual_page_in_cat = requests.get(next_page_url)
        soup = BeautifulSoup(actual_page_in_cat.content, 'html.parser')
        next_page = soup.find("li", "next")

        for book_link in get_books_links(soup):
            page_of_book = requests.get(book_link)
            book_soup = BeautifulSoup(page_of_book.content, 'html.parser')

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

def write_in_file():
    csv_file = "All_books_of_category.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Titre', 'Universal product code', 'Prix avec taxes', 'Prix sans taxes',
                                            'Nombre disponible',
                                            'Description du livre', 'Categorie', 'Note sur 5',
                                            'Lien premiere page de couverture'])
        writer.writeheader()

        #for data in dico_data_book:
            #writer.writerow(data)




        #writer.writerow(get_books_links(soup))
#all_books_of_category = get_books_links(soup)
#print(all_books_of_category)







