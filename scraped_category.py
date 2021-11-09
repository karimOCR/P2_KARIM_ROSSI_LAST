"""Appels de fonctions pour une catégorie"""
import requests
from bs4 import BeautifulSoup
import scraped_book_with_function as sbwf
#from scraped_book_with_function import * #danger car possibilité de conflit

#Création d'une nouvelle soup_categories dans laquelle on retrouve que les urls des categories
#def get_soup_categories_urls_list(soup):
   # soup_categories_urls_list= soup.find_all(class_="nav")
 #   return (soup_categories_urls_list)
#print(get_soup_categories_urls_list(soup))

url_category= 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html'
page = requests.get(url_category)
soup = BeautifulSoup(page.content, 'html.parser')


def get_all_categories_urls(soup):
    all_categories_urls=soup.find_all("a")
    return all_categories_urls
print(get_all_categories_urls(soup))


for link in soup.find_all('a', class_=""):
    print(link.get('href'))



#urlbooks= soup.find_all("article", class_="product_pod")
#print(urlbooks)

#for nbre_page in range(0,3):
#    soup.find_all("a")



"""
h3list=soup.find_all("h3")
#print (dir (h3))
for h3tag in h3list:
    print(h3tag)
    #anchor=h3tag.text.replace ("<h3>", "")

"""

"""

#Appels des fonctions pour extraire les informations d'un livre
sbwf.get_product_type(soup)
sbwf.get_title(soup)
sbwf.get_price_incl_tax(soup)
sbwf.get_universal_product_code(soup)
sbwf.get_notation(soup)
"""




#def get_category_list():

#def get_site(url):
    #Obtenir les données de la page d'accueil
    #page_accueil=get_page(http://books.toscrape.com/index.html)
    #Catégories_urls = Extract la liste des urls de chaque catégories dans la page d'accueil
    #Books_urls = Extract la liste des urls de chaque livres dans une




"""def main(url):
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
    return list_names"""





"""
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

with open(csv_file, 'a') as csvfile:
    writer = csv.DictWriter(csvfile,
                            fieldnames=['Titre', 'Universal product code', 'Prix avec taxes', 'Prix sans taxes',
                                        'Nombre disponible',
                                        'Description du livre', 'Categorie', 'Note sur 5',
                                        'Lien premiere page de couverture'])
    writer.writeheader()
    for data in dico_data_book:
        writer.writerow(data)

"""

#je veux recuperer les url de chaque livre

def get_urls_all_c(soup):
    urls_all_categories=soup.find_all("a", class_="side_categories")
    return urls_all_categories
print(get_urls_all_categories(soup))