import pandas as pd


class Recipe:
    def __init__(self, title, ingredients, prep_time,rating, type, instructions):
        self.title = title
        self.ingredients = ingredients
        self.prep_time = prep_time
        self.rating = rating
        self.type = type
        self.instructions = instructions


def getRecipes():
    data = pd.read_csv("recipeScraping.csv", encoding='iso-8859-1')
    # carica le ricette dal dataset
    recipes = []
    for index, row in data.iterrows():

        row[1] = row[1].replace(']', '')
        row[1] = row[1].replace('[', '')
        row[1] = row[1].replace("'", '')

        ingredientArray = []
        for ingredient in row[1].split(","):
            ingredient = ingredient.strip()
            ingredient = ingredient.lower()
            ingredientArray.append(ingredient)

        recipe = Recipe(row["title"], ingredientArray, row["time"], row["ratings"], row["type"],row["instructions"])
        recipes.append(recipe)
    return recipes



def evaluate_recipe( alternative_recipes, missing_ingredient,recipe, input_ingredients):
    score = 0
    for ingredient in input_ingredients:
       for ing in recipe.ingredients:
        if ingredient in ing:
            recipe.ingredients.remove(ing)
    alternative_recipes.append(recipe)
    missing_ingredient.append(recipe.ingredients)


input=['mascarpone', 'uova', 'savoiardi', 'zucchero', 'cacao']

alternative_recipes=[]
missing_ingredient= []

recipes=getRecipes()

evaluate_recipe(alternative_recipes,missing_ingredient,recipes[0],input)

print(alternative_recipes[0].title)
print(missing_ingredient[0])



