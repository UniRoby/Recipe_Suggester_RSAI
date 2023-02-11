from recipe_scrapers import scrape_me
import requests
from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me
import re


def cleanIngredients(ingredients):
    ingredient_names = []

    for ingredient in ingredients:
        # Rimuovi parentesi e abbreviazioni dalla stringa

        ingredient = ingredient.lower()
        ingredient = re.sub(r",", "", ingredient)
        ingredient = re.sub(r"  ", " ", ingredient)
        ingredient = ingredient.strip()
        if ingredient not in ingredient_names:
            ingredient_names.append(ingredient)
    return ingredient_names


def searchRecipeLink():
    url_list = ["https://www.giallozafferano.it/ricette-cat/"]
    url_recipe_list = []

    count = 1
    while count < 425:
        url = "https://www.giallozafferano.it/ricette-cat/page" + str(count) + "/"
        url_list.append(url)
        count += 1

    for url in url_list:
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            recipe_url = link['href']
            if recipe_url.startswith("https://ricette.giallozafferano.it"):
                if ("#anchor=gz-comments-anchor" not in recipe_url):
                    if (recipe_url not in url_recipe_list):
                        url_recipe_list.append(recipe_url)
    return url_recipe_list


def printTitleRecipeList(url_recipe_list):
    for url in url_recipe_list:
        # print(url)
        scraper = scrape_me(url)
        print("Titolo:", scraper.title())
        ingredients = cleanIngredients(scraper.ingredients())

        print("Tempo:", scraper.total_time())
        print("Valutazione:", scraper.ratings())
        print("Categoria: ", scraper.category())
        print("Istruzioni: ", scraper.instructions())


def createRecipesList(url_recipe_list):
    recipes = []
    count = 0
    for url in url_recipe_list:
        scraper = scrape_me(url)

        print(str(count) + " " + scraper.title())
        count += 1
        ingredients = cleanIngredients(scraper.ingredients())
        #ingredients = scraper.ingredients()

        recipe = {'title': scraper.title(), 'ingredients': ingredients, 'time': scraper.total_time(),
                      'ratings': scraper.ratings(), 'type': scraper.category(), 'instructions': scraper.instructions()}

        # Aggiungi le informazioni della ricetta alla lista
        recipes.append(recipe)
    return recipes


def saveRecipe2CSV(recipes):
    import csv

    # Apri il file in modalità di scrittura
    with open('ricetteEsatte.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['title', "ingredients", 'time', 'ratings', 'type', 'instructions'])

        # Scrivi le informazioni delle ricette nel file
        for recipe in recipes:
            row = [
                recipe['title'],
                recipe['ingredients'],
                recipe['time'],
                recipe['ratings'],
                recipe['type'],
                recipe['instructions']
            ]

            writer.writerow(row)
        print("dataset cvs creato\n")


if __name__ == "__main__":
    url_recipe_list = searchRecipeLink()
    # printTitleRecipeList(url_recipe_list)
    recipes = createRecipesList(url_recipe_list)
    # for recipe in recipes:
    # print(recipe)
    saveRecipe2CSV(recipes)

