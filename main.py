





"""extraction de toutes les pages d'une catégorie"""
def get_all_categories_pages(category):

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

"""URL_MODELE = "https://books.toscrape.com/catalogue/category/books/<nom de la catégorie>/index.html"

FONCTION get_all_categories_pages(category):
    category_url = remplacer <nom de la catégorie> par category dans URL_MODELE
    pages = Crée une liste de départ ne contenant que category_url
    
    TANT QUE url a une valeur valide FAIRE:
        page = Récupérer la page de la située à category_url
        next = Récupérer le bouton next en bas de la page
        SI le bouton next n'a pas été trouvé FAIRE:
            Donner la valeur None à category_url pour arrêter la boucle
        SINON SI on a trouvé un bouton next FAIRE
            Ajouter l'url du bouton next à la fin de category_url en remplaçant index.html ou la page
            Ajouter la nouvelle category_url dans la liste pages
        FIN SI  

        RETURN la liste pages qui contient toutes les urls
    FIN TANT QUE 
FIN DE LA FONCTION"""