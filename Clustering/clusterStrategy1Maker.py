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
 
# Calcola la matrice di similarità tra tutte le ricette nel dataset utilizzando la funzione `cosine_similarity`
cos_sim_matrix = cosine_similarity(tfidf_recipe)


# Effettua il clustering con K-means utilizzando la matrice di similarità
kmeans = KMeans(n_clusters=17, random_state=0).fit(cos_sim_matrix)

# Aggiungi una colonna "cluster" al dataframe per indicare a quale cluster appartiene ogni ricetta
df['cluster'] = kmeans.labels_

df.to_csv("ricette6k_clustered.csv", index=False)

# Riduci le dimensioni dei dati utilizzando PCA per renderli visualizzabili
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(tfidf_recipe.toarray())


# Crea il grafico a dispersione utilizzando le prime due componenti principali
fig, ax = plt.subplots()
scatter = ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=kmeans.labels_)

# Mostra il grafico
plt.show()

from sklearn.metrics import silhouette_score


silhouette_avg = silhouette_score(cos_sim_matrix, kmeans.labels_)
print("Il Silhouette Coefficient è: ", silhouette_avg)

'''
# Initialize a list to store the sum of squared errors for each number of clusters
sse = []

    # Iterate over different values of K
for k in range(1, 20):
        # Initialize the KMeans model
        kmeans = KMeans(n_clusters=k,max_iter=50)
        
        # Fit the model to the data
        kmeans.fit(cos_sim_matrix)
        
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


