import pandas as pd

# Carica il dataset

df_clustered = pd.read_csv("ricette6k_clustered.csv",encoding='iso-8859-1')
selected_recipe_index = 1


print("La ricetta selezionata è: ", df_clustered.iloc[selected_recipe_index]['title'])
#Stampa le ricette simili alla ricetta selezionata


similar_recipes = df_clustered[df_clustered['cluster'] == df_clustered.iloc[selected_recipe_index]['cluster']]
print("Le ricette simili sono:")
print(similar_recipes[['title', 'cluster']][:10])
