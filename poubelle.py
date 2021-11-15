

Dico_data_book_of_category = [{'Titre': sbwf.get_title(soup),
                   'Type de produit': sbwf.get_product_type(soup),
                   'Universal product code': sbwf.get_universal_product_code(soup),
                   'Prix avec taxes': sbwf.get_price_incl_tax(soup),
                   'Prix sans taxes': sbwf.get_price_excl_tax(soup),
                   'Nombre disponible': sbwf.get_num_available(soup),
                   'Description du livre': sbwf.get_product_description(soup),
                   'Categorie': sbwf.get_category(soup),
                   'Note sur 5': sbwf.get_notation(soup),
                   'Lien premiere page de couverture': sbwf.get_image_url(soup)}]
print(Dico_data_book_of_category)

csv_file = "table_data_book_of_category.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile,
                            fieldnames=['Titre', 'Type de produit', 'Universal product code', 'Prix avec taxes',
                                        'Prix sans taxes',
                                        'Nombre disponible', 'Description du livre', 'Categorie', 'Note sur 5',
                                        'Lien premiere page de couverture'])
    writer.writeheader()
    for data in dico_data_book_of_category:
        writer.writerow(data)
"""
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
