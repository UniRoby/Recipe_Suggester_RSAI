import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pandas as pd


def start_search():
    ingredients = input_text.get().lower()
    # chiamare la funzione per la ricerca delle ricette qui
    results = search_recipes(ingredients)


def on_closing():
    if messagebox.askokcancel("Quit", "Vuoi uscire dall'applicazione?"):
        root.destroy()


def get_audio_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dimmi gli ingredienti che hai ")
        audio = r.listen(source)
    ingredients = r.recognize_google(audio, language="it-IT")
    ingredients_list = ingredients.split()
    ingredients_string = ",".join(ingredients_list)
    ingredients_string=ingredients_string.lower()
    input_text.delete(0, tk.END)
    input_text.insert(0, ingredients_string)


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


def evaluate_recipe(recipe, input_ingredients):
    score = 0
    for ingredient in input_ingredients:
        for ing in recipe.ingredients:
            if ingredient in ing:
                score += 1
    ''' 
    for ingredient in recipe.ingredients:
        if ingredient in input_ingredients:
            score += 1
    score += recipe.rating
    '''
    return score


# funzione di ricerca A*
def find_best_recipe(recipes, input_ingredients):
    open_list = []
    closed_list = []
    best_recipes = []
    best_score = 0
    alternative_recipes = []
    missing_ingredient = []

    open_list = recipes

    while open_list:
        # scegli la ricetta con la valutazione più alta
        current_recipe = max(open_list, key=lambda x: evaluate_recipe(x, input_ingredients))
        open_list.remove(current_recipe)
        closed_list.append(current_recipe)

        # verifica se gli ingredienti della ricetta corrispondono a quelli forniti in input
        #if all(ingredient in input_ingredients for ingredient in current_recipe.ingredients):
            #score = evaluate_recipe(current_recipe, input_ingredients)
           # best_recipes.append(current_recipe)  # aggiungo la ricetta corrente alla lista delle migliori ricette
        score = evaluate_recipe(current_recipe, input_ingredients)
        if score!=0:
            if score == len(current_recipe.ingredients):
                best_recipes.append(current_recipe)  # aggiungo la ricetta corrente alla lista delle migliori ricette
            elif len(current_recipe.ingredients)-score==1:
                otherPossibleRecipe(alternative_recipes, missing_ingredient,current_recipe,input_ingredients)

    return best_recipes, alternative_recipes, missing_ingredient

def otherPossibleRecipe(alternative_recipes, missing_ingredient,recipe, input_ingredients):

    recipe_ingredients = recipe.ingredients.copy()

    for ingredient in input_ingredients:
        for ing in recipe_ingredients:
            if ingredient in ing:
                recipe_ingredients.remove(ing)


    alternative_recipes.append(recipe)
    missing_ingredient.append(recipe_ingredients[0])


'''
        
         crea una copia degli ingredientidella ricetta.
         Poi per ogni ingrediente fornito in input, se l'ingrediente è presente nella lista degli ingredienti
         della ricetta, viene rimosso dalla copia della lista.
         aggiungere la ricetta alla lista delle alternative e salvare l'ingrediente mancante.
         Infine la funzione restituisce la lista delle alternative e l'ingrediente mancante.
 '''


def search_recipes(ingredients):
    input_ingredients = [ingredient.strip() for ingredient in ingredients.split(",")]
    recipes = getRecipes()

    best_recipes, alternative_recipes, missing_ingredients = find_best_recipe(recipes, input_ingredients)
    result_text.configure(state='normal', font=("Arial Black", 20))
    result_text.delete('1.0', tk.END)
    result_text.tag_config("green_bold", foreground="green")
    result_text.tag_config("orange_bold", foreground="orange")

    if len(best_recipes) == 0:
        result_text.insert(tk.END, "")
    elif len(best_recipes) == 1:
        result_text.insert(tk.END, "\n----------------------RICETTA MIGLIORE: ", "green_bold")
        result_text.insert(tk.END, best_recipes[0].title)
        result_text.insert(tk.END, "\n----------------------Ingredienti usati: ")
        result_text.insert(tk.END, best_recipes[0].ingredients)
    else:
        result_text.insert(tk.END, "\n----------------------RICETTE MIGLIORI: \n", "green_bold")
        count = 0;
        for recipe in best_recipes:
            count += 1
            result_text.insert(tk.END, "\n---", recipe.title)
            result_text.insert(tk.END, recipe.title)
            result_text.insert(tk.END, "---")
            result_text.insert(tk.END, "\n--------------Ingredienti usati: ")
            result_text.insert(tk.END, recipe.ingredients)

    #alternative_recipes, missing_ingredients = find_alternative_recipes(getRecipes(), input_ingredients)


    if len(alternative_recipes) == 0:
        result_text.insert(tk.END, "")
    elif len(alternative_recipes) == 1:
        result_text.insert(tk.END, "\n-----------------POSSIBILE RICETTA: ","orange_bold")
        result_text.insert(tk.END, alternative_recipes[0].title)
        result_text.insert(tk.END, "\n-----------------Ingredienti richiesti: ")
        result_text.insert(tk.END, alternative_recipes[0].ingredients)
        result_text.insert(tk.END, "\n-----------------Ingrediente mancante da comprare: ")
        result_text.insert(tk.END, missing_ingredients[0])
    else:
        result_text.insert(tk.END, "\n----------------------POSSIBILI RICETTE: \n","orange_bold")
        count = 0;
        i = 0
        for recipe in alternative_recipes:
            count += 1
            result_text.insert(tk.END, "\n---", recipe.title)
            result_text.insert(tk.END, recipe.title)
            result_text.insert(tk.END, "---")
            result_text.insert(tk.END, "\n--------------Ingredienti richiesti: ")
            result_text.insert(tk.END, recipe.ingredients)
            result_text.insert(tk.END, "\n--------------Ingrediente mancante da comprare: ")
            result_text.insert(tk.END, missing_ingredients[i])
            i += 1
    if len(best_recipes) == 0 and len(alternative_recipes) == 0:
        result_text.insert(tk.END, "\n----------------------Nessuna ricetta trovata----------------------")
    result_text.configure(state='disabled')


ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


# funzione che cambia l'aspetto grafico della GUI
def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


# funzione che effettua lo scaling della GUI
def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)


root = ctk.CTk()
root.geometry("1280x720 ")
root.title("No wAIste")

sidebar_frame = ctk.CTkFrame(root)
sidebar_frame.pack(pady=10, padx=10, fill="both", side="left")

'''
show_frame = ctk.CTkFrame(root)
show_frame.pack(pady=10,padx=10,fill="both",expand=True,side="top")
result_text = tkinter.Text(show_frame, state='disabled')
result_text.pack(pady=10,padx=10,fill="both",expand=True)
'''
# create textbox
# textbox = ctk.CTkTextbox(root)
# textbox.insert("0.0", "CTkTextbox\n\n" + "")
result_text = ctk.CTkTextbox(root, state='disabled')
# result_text.pack(pady=10,padx=10,fill="both",expand=True)
result_text.pack(pady=10, padx=10, fill="both", expand=True, side="top")

input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=10, fill="both", side="bottom")

logo_label = ctk.CTkLabel(sidebar_frame, text="No wAIste")
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

# bottoni

sidebar_button_1 = ctk.CTkButton(sidebar_frame, text="Avvia Ricerca", command=start_search, font=("Helvetica", 14))
sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

appearance_mode_label = ctk.CTkLabel(sidebar_frame, text="Appearance Mode:", anchor="w")
appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
appearance_mode_optionemenu = ctk.CTkOptionMenu(sidebar_frame, values=["Light", "Dark", "System"],
                                                command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
scaling_label = ctk.CTkLabel(sidebar_frame, text="UI Scaling:", anchor="w")
scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
scaling_optionemenu = ctk.CTkOptionMenu(sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                        command=change_scaling_event)
scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

input_text = ctk.CTkEntry(input_frame, placeholder_text="Inserisci Ingredienti", font=("Helvetica", 14))
input_text.grid(row=0, column=0, pady=10, padx=10, columnspan=2, sticky='nsew')

mic_button = ctk.CTkButton(input_frame, text="Mic", command=get_audio_input, height=50, width=5)
mic_button.grid(row=0, column=1, pady=10, padx=10, columnspan=2, sticky='nsew')

input_frame.columnconfigure(0, weight=5)
input_frame.columnconfigure(1, weight=1)

# default values
appearance_mode_optionemenu.set("Dark")
scaling_optionemenu.set("100%")

if __name__ == "__main__":
    root.mainloop()