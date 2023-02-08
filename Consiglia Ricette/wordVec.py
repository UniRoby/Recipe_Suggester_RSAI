import pandas as pd
from gensim.models import Word2Vec

# get corpus with the documents sorted in alphabetical order
def get_and_sort_corpus(data):
    corpus_sorted = []
    for doc in data.ingredients.values:
        doc=doc.split(",")
        doc.sort()
        corpus_sorted.append(doc)
    return corpus_sorted
  
# calculate average length of each document 
def get_window(corpus):
    lengths = [len(doc) for doc in corpus]
    avg_len = float(sum(lengths)) / len(lengths)
    return round(avg_len)

if __name__ == "__main__":
    # load in data
    df = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')

    df.dropna(subset=['ingredients'], inplace=True)
    # get corpus
    corpus = get_and_sort_corpus(df)
    print(f"Length of corpus: {len(corpus)}")
    print(corpus[0])
    '''
    # train and save CBOW Word2Vec model
    model_cbow = Word2Vec(
      corpus, sg=0, workers=8, window=get_window(corpus), min_count=1, vector_size=100
    )
    model_cbow.save('model_cbow.bin')
    print("Word2Vec model successfully trained")
    '''