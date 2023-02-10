import pandas as pd
from gensim.models import Word2Vec

#ottieni il corpus con gli ingredienti in oridne alfabetico
def get_and_sort_corpus(data):
    corpus_sorted = []
    for doc in data.ingredients.values:
        doc=doc.split(",")
        doc.sort()
        corpus_sorted.append(doc)
    return corpus_sorted
  
#calcola la lunghezza media di ogni doc (lista ingredienti ricetta)
def get_mean(corpus):
    lengths = [len(doc) for doc in corpus]
    avg_len = float(sum(lengths)) / len(lengths)
    return round(avg_len)

if __name__ == "__main__":
    # load in data
    df = pd.read_csv('ricette.csv',encoding='iso-8859-1')

    df.dropna(subset=['ingredients'], inplace=True)
    # get corpus
    corpus = get_and_sort_corpus(df)
    print(f"Length of corpus: {len(corpus)}")
    print(corpus[0])

    # train and save CBOW Word2Vec model
    model_cbow = Word2Vec(
      corpus, sg=0, workers=8, window=get_mean(corpus), min_count=1, vector_size=100
    )
    print(model_cbow.wv.most_similar(u'pomodori'))

    model_cbow.save('model_cbow.bin')
    print("Word2Vec model successfully trained")


'''
Questo codice utilizza la libreria pandas e gensim per creare un modello 
di word embedding basato sul modello Word2Vec CBOW (Continuous Bag of Words).
Il codice carica un file CSV che contiene le ricette, 
dove ogni riga rappresenta una ricetta e l'unica colonna di interesse è la colonna "ingredienti".
La funzione get_and_sort_corpus prende i valori della colonna "ingredienti" e li divide in una lista di liste dove ogni 
sotto-lista rappresenta un documento (una ricetta) con gli ingredienti separati da virgole. 
Inoltre, gli ingredienti di ogni documento vengono ordinati alfabeticamente.
La funzione get_mean calcola la lunghezza media dei documenti e la utilizza come dimensione della finestra per il modello Word2Vec CBOW.

Il modello viene addestrato sui documenti con l'aiuto della funzione Word2Vec e 
salvato sul disco con il nome 'model_cbow.bin'. 
Infine, viene eseguita una query di similarità per la parola "pomodori" sul modello addestrato e vengono stampate le parole più simili a "pomodori".



'''