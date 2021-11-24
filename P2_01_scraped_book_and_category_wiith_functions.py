"""Defintion de fonctions pour les données d'un livre"""

""" Creation et importer ses propres modules Python"""

# Module traitant des infos dans un livre
# url='http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'
# page=requests.get(url)
# soup= BeautifulSoup(page.content, 'html.parser')

def get_universal_product_code(soup):
    UPC = soup.select("td")[0].text
    return UPC


def get_title(soup):
    title = soup.find_all("h1")[0].text
    return title


def get_product_type(soup):
    product_type = soup.select("td")[1].text
    return product_type


def get_price_incl_tax(soup):
    price_incl_tax = soup.select("td")[2].text
    return price_incl_tax


def get_price_excl_tax(soup):
    price_excl_tax = soup.select("td")[3].text
    return price_excl_tax


def get_num_available(soup):
    num_available = soup.select("td")[5].string
    return num_available


def get_product_description(soup):
    description = soup.select("p")[3].text
    return description


def get_category(soup):
    category = soup.select("a")[3].text
    return category


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


def get_image_url(soup):
    image_url = soup.find("div", class_="item active").img["src"]
    image_url = "http://books.toscrape.com/" + image_url.replace('../', '')
    return image_url


def export_csv():
    filename = "export_data_book.csv"
    f = open("export_data_book.csv", "w")
    f.write("See you soon!")
    f.close()




""""""""""""""""""""""""""
"""Appels de fonctions pour une catégorie"""
#import csv
#import requests
#from bs4 import BeautifulSoup
#import scraped_book_with_function as sbwf


url_category = 'http://books.toscrape.com/catalogue/category/books/art_25/index.html'
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

csv_file = "P2_05_all_books_of_category.csv"
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Titre', 'Universal product code', 'Prix avec taxes',
                                                 'Prix sans taxes', 'Nombre disponible', 'Description du livre',
                                                 'Categorie', 'Note sur 5', 'Lien premiere page de couverture'])
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
    csv_file = "P2_05_all_books_of_category.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Titre', 'Universal product code', 'Prix avec taxes',
                                                     'Prix sans taxes', 'Nombre disponible', 'Description du livre',
                                                     'Categorie', 'Note sur 5', 'Lien premiere page de couverture'])
        writer.writeheader()
