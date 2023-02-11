import csv

import re


# Apri il file CSV in modalità di lettura
with open('ricette.csv', mode='r') as csv_file:
    # Crea un oggetto reader
    reader = csv.reader(csv_file)

    # Salta la prima riga (intestazione)
    next(reader)

    # Inizializza le variabili per le statistiche
    num_recipes = 0
    total_ratings = 0
    total_prep_time = 0
    differentIngredientsNumber=0

    # Inizializza il dizionario per i tipi di ricette
    recipe_types = {}
    # Inizializza il dizionario per gli ingredienti
    ingredients = {}
    
    
    # Crea le liste per le statistiche
    ratings_2 = []
    prep_time_2 = []



    # Inizializza le variabili per i massimi e minimi
    max_ratings = 0
    max_ratings_recipe = ""
    min_ratings = float("inf")
    min_ratings_recipe = ""
    max_prep_time = 0
    max_prep_time_recipe = ""
    min_prep_time = float("inf")
    min_prep_time_recipe = ""
    max_ingredients = 0
    max_ingredients_recipe = ""
    min_ingredients = float("inf")
    min_ingredients_recipe = ""
    max_ingredients_recipeTitle=""
    tot_ingredients=0
    # Per ogni riga del file CSV
    for row in reader:
        # Incrementa il contatore delle ricette
        num_recipes += 1
        # Aggiungi il numero di "mi piace" alla somma totale
        
        ratings =float(row[3])
        total_ratings += ratings
        # Aggiorna il massimo e il minimo numero di "mi piace"
        if ratings > max_ratings:
            max_ratings = ratings
            max_ratings_recipe = row[3]
        if ratings < min_ratings:
            min_ratings = ratings
            min_ratings_recipe = row[3]
        # Aggiungi il tempo di preparazione alla somma totale
        prep_time = int(row[2])
        total_prep_time += prep_time
        # Aggiorna il massimo e il minimo tempo di preparazione
        if prep_time > max_prep_time:
            max_prep_time = prep_time
            max_prep_time_recipe = row[2]
        if prep_time < min_prep_time:
            min_prep_time = prep_time
            min_prep_time_recipe = row[2]
      
        # Conta il tipo di ricetta
        recipe_type = row[4]
        if recipe_type in recipe_types:
            recipe_types[recipe_type] += 1
        else:
            recipe_types[recipe_type] = 1
            
        
        # Conta gli ingredienti
        for ingredient in row[1].split(","):
            
            ingredient = re.sub(r'\[', '', ingredient)
            ingredient = re.sub(r'\]', '', ingredient)
            ingredient = re.sub(r"'", '', ingredient)
            ingredient = re.sub(r"/", '', ingredient)
            ingredient = re.sub(r'"', '', ingredient)
            ingredient = re.sub(r"doliva", "d'oliva", ingredient)
            ingredient = re.sub(r"\)", "", ingredient)
            

            
            ingredient = re.sub(r"  ", " ", ingredient)
            ingredient = ingredient.strip()
            ingredient = ingredient.lower()
            
            tot_ingredients+=1
            '''
            if ingredient in unique_ingredients':
                print("\nRicetta ",row[0])
               
            '''
            if ingredient in ingredients:
                ingredients[ingredient] += 1
            else:
                ingredients[ingredient] = 1
                
        # Aggiorna il massimo e il minimo numero di ingredienti
        num_ingredients = len(row[1].split(","))
        if num_ingredients > max_ingredients:
            max_ingredients = num_ingredients
            max_ingredients_recipe = row[1]
            max_ingredients_recipeTitle=row[0]
        if num_ingredients < min_ingredients:
            min_ingredients = num_ingredients
            min_ingredients_recipe = row[1]

        # Aggiungi il numero di 'ratings' alla lista
        ratings_2.append(float(row[3]))
        # Aggiungi il tempo di preparazione alla lista
        prep_time_2.append(int(row[2]))
       

# Calcola le statistiche
avg_ratings =total_ratings / num_recipes
avg_prep_time = total_prep_time / num_recipes


# Stampa le statistiche
print("Numero di ricette:", num_recipes)
print("Tempo di preparazione totale (minuti):", total_prep_time)
print("\nMedia di 'rating' per ricetta:", avg_ratings)
print("Media di tempo di preparazione per ricetta (minuti):", avg_prep_time)


# Stampa il numero di ricette per tipo
print("\nNumero di ricette per tipo:")
for recipe_type, count in recipe_types.items():
    print(f"{recipe_type}: {count}")

# Ordina gli ingredienti in base al numero di occorrenze
sorted_ingredients = sorted(ingredients.items(), key=lambda x: x[1])

# Stampa il numero di ingredienti totali
print("\nNumero di ingredienti totali:", tot_ingredients)

print("\nNumero di ingredienti diversi escludendo le ripetizioni: ", len(ingredients))


# Stampa gli ingredienti meno usati
print("\nIngredienti meno usati:")
for ingredient, count in sorted_ingredients[:5]:
    print(f"{ingredient}: {count}")

more_used_ingredients=[]
'''
# Stampa gli ingredienti più usati
print("\nIngredienti più usati:")
i=0
for ingredient, count in sorted_ingredients:
    if ingredient!='':
            print(str(i)+" "+f"{ingredient}: {count}")
            i+=1

'''

# Stampa gli ingredienti unici
totale_ing_unici=0
unique=[]
print("\nIngredienti unici:" )
for ingredient, count in ingredients.items():
    if count == 1: #and ' ' in ingredient:
        totale_ing_unici+=1
        unique.append(ingredient)
        print(ingredient)


with open ("unique.txt","w",encoding='iso-8859-1') as file:
    for el in unique:
        file.write(el + "\n")


   
print("\nTotale Ingredienti unici:", totale_ing_unici)
'''
# Stampa la ricetta con il maggior numero di "ratings"
print("\nRicetta con il 'ratings' massimo: ",max_ratings_recipe)

# Stampa la ricetta con il minore numero di "mi piace"
print("\nRicetta con il 'rating' minimo: ",min_ratings_recipe)



# Stampa la ricetta con il maggior tempo di preparazione
print("\nRicetta con il maggior tempo di preparazione: ",max_prep_time_recipe)

# Stampa la ricetta con il minore tempo di preparazione
print("\nRicetta con il minore tempo di preparazione: ",min_prep_time_recipe)

# Stampa la ricetta con il maggior numero di ingredienti
print("\nRicetta con il maggior numero di ingredienti: ",max_ingredients_recipeTitle+", Numero ingredienti: "+ str(max_ingredients))

# Stampa la ricetta con il minore numero di ingredienti
print("\nRicetta con il minore numero di ingredienti: ",min_ingredients_recipe)



'''
'''
# Calcola e stampa le statistiche
print("Media di 'rating' per ricetta:", sum(ratings_2) / len(ratings_2))
print("Mediana di 'rating' per ricetta:", statistics.median(ratings_2))
print("Moda di 'rating' per ricetta:", statistics.mode(ratings_2))
print("Deviazione standard di 'rating per ricetta:", statistics.stdev(ratings_2))
print("\nMedia di tempo di preparazione per ricetta (minuti):", sum(prep_time_2) / len(prep_time_2))
print("Mediana di tempo di preparazione per ricetta (minuti):", statistics.median(prep_time_2))
print("Moda di tempo di preparazione per ricetta (minuti):", statistics.mode(prep_time_2))
print("Deviazione standard di tempo di preparazione per ricetta (minuti):", statistics.stdev(prep_time_2))

'''
