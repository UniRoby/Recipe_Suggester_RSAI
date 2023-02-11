import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
from random import randrange
from sklearn.svm import SVC
from sklearn.neighbors import NearestNeighbors
    
class TfidfEmbeddingVectorizer(object):
    def __init__(self, word_model):

        self.word_model = word_model
        self.word_idf_weight = None
        self.vector_size = word_model.wv.vector_size

    def fit(self, docs):  
        """
		Adattarsi ad un elenco di documenti, che erano stati preelaborati e tokenizzati,
        Crea un modello tfidf per calcolare l'idf di ogni parola come peso.
        Il peso tf è già coinvolto durante la costruzione di vettori di parole medie, e quindi omesso.
        :param
                pre_processed_docs: elenco di documenti, che sono tokenizzati
        :ritorno:
                se stesso
		"""

        text_docs = []
        for doc in docs:
            text_docs.append(" ".join(doc))

        #tfidf = TfidfVectorizer()
        tfidf = TfidfVectorizer(token_pattern = r'[^,]+')
        tfidf.fit(text_docs)  # must be list of text string
        '''
        se una parola non è mai stata vista, deve essere almeno altrettanto rara
        come una qualsiasi delle parole conosciute, quindi l'idf di default è il massimo degli
        idf noti
        '''
        max_idf = max(tfidf.idf_)  #utilizzato come valore predefinito per defaultdict
        self.word_idf_weight = defaultdict(
            lambda: max_idf,
            [(word, tfidf.idf_[i]) for word, i in tfidf.vocabulary_.items()],
        )
        return self

    def transform(self, docs): # soddisfare i requisiti del trasformatore scikit-learn
        doc_word_vector = self.word_average_list(docs)
        return doc_word_vector

    def word_average(self, sent):
        """
            Calcola il vettore di parole medio per un singolo documento/frase.
            :param inviato: elenco di token di frase
            :ritorno: media
		"""

        mean = []
        for word in sent:
            if word in self.word_model.wv.index_to_key:
                mean.append(
                    self.word_model.wv.get_vector(word) * self.word_idf_weight[word]
                )  # idf weighted

        if not mean:  
            # parole vuote
            # Se un testo è vuoto, restituisce un vettore di zeri.
           
            return np.zeros(self.vector_size)
        else:
            mean = np.array(mean).mean(axis=0)
            return mean

    def word_average_list(self, docs):
        """
            Calcola il vettore di parole medio per più documenti, in cui i documenti erano stati tokenizzati.
            :param docs: elenco di frasi nell'elenco di token separati
            :ritorno:
            array di vettore di parole medio in forma (len(docs),)
		"""
        return np.vstack([self.word_average(sent) for sent in docs])    
'''
Word2Vec cerca di prevedere le parole in base all'ambiente circostante,
quindi era fondamentale ordinare gli ingredienti in ordine alfabetico
'''
def get_and_sort_corpus(data):
    corpus_sorted = []
    for doc in data.ingredients.values:
        doc=str(doc).split(",")
        doc.sort()
        corpus_sorted.append(doc)
    return corpus_sorted
  
# calculate average length of each document 
def get_window(corpus):
    lengths = [len(doc) for doc in corpus]
    avg_len = float(sum(lengths)) / len(lengths)
    return round(avg_len)

# Top-N recomendations order by score
def get_recommendations(N, indici):
    # load in recipe dataset 
    df_recipes = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')
    
    recommendation = pd.DataFrame(columns = ['ricetta', 'ingredienti'])
    count = 0
    for i in indici:
        recommendation.at[count, 'ricetta'] = df_recipes['title'][i]
        recommendation.at[count, 'ingredienti'] = df_recipes['ingredients'][i]
        
        count += 1
    return recommendation

def get_recs(ingredients, N=5):
    # load in word2vec model
    model = Word2Vec.load("model_cbow.bin")
   # model.init_sims(replace=True)
    #if model:
        #print("Modello caricato correttamente")
    # load in data
    data = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')
    
    # create corpus
    corpus = get_and_sort_corpus(data)

    tfidf_vec_tr = TfidfEmbeddingVectorizer(model)
    tfidf_vec_tr.fit(corpus)
    doc_vec = tfidf_vec_tr.transform(corpus)
    #doc_vec = [doc.reshape(1, -1) for doc in doc_vec]
    #assert len(doc_vec) == len(corpus)

    # create embessing for input text
    input = ingredients
    # create tokens with elements
    input = input.split(",")

    input_vec = tfidf_vec_tr.transform([input])
  
    #input_embedding = tfidf_vec_tr.transform([input])[0].reshape(1, -1)

    #input_embedding = tfidf_vec_tr.transform([input])[0].reshape(1, -1)

    # get KNN between input embedding and all the document embeddings
    knn = NearestNeighbors(n_neighbors=N, algorithm='ball_tree')
    knn.fit(doc_vec)
    distances, indices = knn.kneighbors(input_vec)
    recommendations = get_recommendations(N, indices[0])
    
    return recommendations


if __name__ == "__main__":

    df = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')
  
    n= randrange(0,6030)
   
    test_ingredients = "farina,uova,grana padano,pangrattato"
   
    recs = get_recs(test_ingredients)
    i=0
    while i<len(recs):
        print("\n---"+recs.ricetta[i])
        print(recs.ingredienti[i])
        i+=1
   
        