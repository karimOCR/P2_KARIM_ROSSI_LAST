"""Defintion de fonctions pour les données d'un livre"""

""" Creation et importer ses propres modules Python"""


# Module traitant des infos dans un livre
# url='http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'
# page=requests.get(url)
# soup= BeautifulSoup(page.content, 'html.parser')

def get_universal_product_code(soup):
    UPC = soup.select("td")[0].text
    return UPC


# print (get_universal_product_code (soup))

def get_title(soup):
    title = soup.find_all("h1")[0].text
    return title


# print(get_title(soup))

def get_product_type(soup):
    product_type = soup.select("td")[1].text
    return product_type


# print(get_product_type(soup))

def get_price_incl_tax(soup):
    price_incl_tax = soup.select("td")[2].text
    return price_incl_tax


# print(get_price_incl_tax(soup))

def get_price_excl_tax(soup):
    price_excl_tax = soup.select("td")[3].text
    return price_excl_tax


# print(get_price_excl_tax(soup))

def get_num_available(soup):
    num_available = soup.select("td")[5].string
    return num_available


# print(get_num_available(soup))

def get_product_description(soup):
    description = soup.select("p")[3].text
    return description


# print(get_product_description(soup))

def get_category(soup):
    category = soup.select("a")[3].text
    return category


# print(get_category(soup))

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


# print(get_notation(soup))

def get_image_url(soup):
    image_url = soup.find("div", class_="item active").img["src"]
    image_url = "http://books.toscrape.com/" + image_url.replace('../', '')
    return image_url


# print(get_image_url(soup))

"""def get_image_url_by_string(soup):
    image_url=str(soup.find_all("img")[0])
    image_url= image_url.split(" ")[7].replace("../","")
    image_url=image_url.replace("src=", "").replace("\"", "").replace("/>", "")
    image_url="http://books.toscrape.com/"+image_url
    return image_url
print(get_image_url_by_string(soup))"""


def export_csv():
    filename = "export_data_book.csv"
    f = open("export_data_book.csv", "w")
    f.write("See you soon!")
    f.close()
