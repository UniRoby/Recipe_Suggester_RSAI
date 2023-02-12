import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import nltk
import pickle 
from sklearn.metrics.pairwise import cosine_similarity  #coseno


# Carica il dataset
df = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')

# Rimuovi le righe che contengono valori mancanti
df.dropna(subset=['ingredients'], inplace=True)
df.reset_index(drop=True, inplace=True)

df['ingredients'] = df.ingredients.values.astype('U')
# TF-IDF feature extractor Term Frequency - Inverse Document Frequency" (TF-IDF)
tfidf = TfidfVectorizer(min_df=5, max_df=0.60,encoding='iso-8859-1',token_pattern = r'[^,]+') #Questa regex matcha una qualsiasi serie di caratteri che non sia una virgola
tfidf.fit(df['ingredients'])
tfidf_recipe = tfidf.transform(df['ingredients'])

selected_recipe_index = 1950


ingredients=df.iloc[selected_recipe_index]["ingredients"]
# usa il nostro modello tfidf preaddestrato per codificare i nostri ingredienti di input
ingredients_tfidf = tfidf.transform([ingredients])
    
# calcola la similarità del coseno tra gli ingredienti reali della ricetta e quelli dell'input
cos_sim = map(lambda x: cosine_similarity(ingredients_tfidf, x), tfidf_recipe)
scores = list(cos_sim)

# Trasforma le similarità in un array numpy
scores = np.array(scores)

# Effettua il clustering con K-means
kmeans = KMeans(n_clusters=5, random_state=0).fit(scores.reshape(-1, 1))

#print(tfidf_recipe.shape)


# Aggiungi una colonna "cluster" al dataframe per indicare a quale cluster appartiene ogni ricetta
df['cluster'] = kmeans.labels_


# Riduci le dimensioni dei dati utilizzando PCA per renderli visualizzabili
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(tfidf_recipe.toarray())


# Crea il grafico a dispersione utilizzando le prime due componenti principali
fig, ax = plt.subplots()
scatter = ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=kmeans.labels_)

# Mostra il grafico
#plt.show()

from sklearn.metrics import silhouette_score


silhouette_avg = silhouette_score(scores.reshape(-1, 1), kmeans.labels_)
print("Il Silhouette Coefficient è: ", silhouette_avg)


#Stampa le ricette simili alla ricetta selezionata
print("La ricetta selezionata è: ", df.iloc[selected_recipe_index]['title'])
similar_recipes = df[df['cluster'] == df.iloc[selected_recipe_index]['cluster']]
print("Le ricette simili sono:")
selected_recipes=similar_recipes[['title', 'cluster']][:10]

for recipe in selected_recipes['title']:
    print(recipe)



'''
# Initialize a list to store the sum of squared errors for each number of clusters
sse = []

    # Iterate over different values of K
for k in range(1, 20):
        # Initialize the KMeans model
        kmeans = KMeans(n_clusters=k,max_iter=50)
        
        # Fit the model to the data
        kmeans.fit(scores.reshape(-1, 1))
        
        # Calculate the sum of squared errors for this number of clusters
        sse.append(kmeans.inertia_)

 # Plot the sum of squared errors against the number of clusters
plt.plot(range(1, 20), sse)
plt.title('Elbow Method')
plt.xlabel('Numero di Cluster')
plt.ylabel("Somma errori quadratici")

# Show the plot
plt.show()
'''
