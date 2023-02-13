import customtkinter as ctk
import tkinter
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from random import randrange
'''
Sistema di raccomandazione di ricette basato su ingredienti. 

Il sistema utilizza il modello di Word2Vec per rappresentare gli ingredienti come vettori nel spazio semantico.
Il codice crea una classe TfidfEmbeddingVectorizer che adatta e trasforma i documenti (liste di ingredienti) 
in vettori di parole medie. La classe TfidfEmbeddingVectorizer ha il seguente funzionamento:

fit: calcola l'IDF (Inverse Document Frequency) di ogni parola utilizzando TfidfVectorizer di scikit-learn.

transform: trasforma i documenti in vettori di parole medie. Questo viene fatto utilizzando la funzione word_average_list che calcola il vettore di parole medie per più documenti.

word_average: calcola il vettore di parole medie per un singolo documento/frase.

word_average_list: calcola il vettore di parole medie per più documenti.

la funzione clustering  usa un algoritmo di clustering con input la cosine_similarity  tra gli ingredienti reali delle ricette e quelli dell'input

la funzione fastClustering  usa un dataset con l'attributo cluster creato in un altro file per ottenere le ricette consigliate
'''
def clustering(n):
    # Carica il dataset
    global df 
    
    
    # usa TF-IDF come pesi per ogni incorporamento di parole
    tfidf = TfidfVectorizer(min_df=5, max_df=0.60,encoding='iso-8859-1',token_pattern = r'[^,]+') #Questa regex matcha una qualsiasi serie di caratteri che non sia una virgola
    tfidf.fit(df['ingredients'])
    tfidf_recipe = tfidf.transform(df['ingredients'])
    
    
    
    print(df["title"][n]+"   index clustering: "+str(n))
    ingredients=df["ingredients"][n]
    # usa il nostro modello tfidf preaddestrato per codificare i nostri ingredienti di input
    ingredients_tfidf = tfidf.transform([ingredients])
        
    # calcola la similarità del coseno tra gli ingredienti reali della ricetta e quelli dell'input
    cos_sim = map(lambda x: cosine_similarity(ingredients_tfidf, x), tfidf_recipe)
    scores = list(cos_sim)

    # Trasforma le similarità in un array numpy
    scores = np.array(scores)

    # Effettua il clustering con K-means
    kmeans = KMeans(n_clusters=5, random_state=0,n_init=10).fit(scores.reshape(-1, 1))

    #print(tfidf_recipe.shape)

    # Aggiungi una colonna "cluster" al dataframe per indicare a quale cluster appartiene ogni ricetta
    df['cluster'] = kmeans.labels_

    #Stampa le ricette simili alla ricetta selezionata

    similar_recipes = df[df['cluster'] == df['cluster'][n]]
  
    return similar_recipes[['title']][:5]

def fastClustering(n):
    # Carica il dataset
    df_clustered = pd.read_csv("ricette6k_clustered.csv",encoding='iso-8859-1')
    print(df['title'][n]+" index clustering S1: "+str(n))

    similar_recipes = df_clustered[df_clustered['cluster'] == df_clustered['cluster'][n]]
    #ricette simili alla ricetta selezionata
    return similar_recipes[['title']][:6]


class TfidfEmbeddingVectorizer(object):
    def __init__(self, word_model):

        self.word_model = word_model
        self.word_idf_weight = None
        self.vector_size = word_model.wv.vector_size

    def fit(self, docs):  # comply with scikit-learn transformer requirement
        """
		Adattarsi a un elenco di documenti, che erano stati preelaborati e tokenizzati,
        Quindi crea un modello tfidf per calcolare l'idf di ogni parola come peso.
        Notato che il peso tf è già coinvolto durante la costruzione di vettori di parole medie, e quindi omesso.
        :param
                pre_processed_docs: elenco di documenti, che sono tokenizzati
        :ritorno:
                se stesso
		"""

        text_docs = []
        for doc in docs:
            text_docs.append(" ".join(doc))

        tfidf = TfidfVectorizer()
        tfidf.fit(text_docs)  # must be list of text string

        # se una parola non è mai stata vista, deve essere almeno altrettanto rara
        # come una qualsiasi delle parole conosciute, quindi l'idf predefinito è il massimo di
        # idf noti
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
            :ritorno:
                    media: float di vettori di parole di media
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
            # logging.warning(
            # "impossibile calcolare la media a causa dell'assenza del vettore per {}".format(sent)
            # )
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
era fondamentale ordinare gli ingredienti in ordine alfabetico
'''
def get_and_sort_corpus(data):
    corpus_sorted = []
    for doc in data.ingredients.values:
        doc=str(doc).split(",")
        doc.sort()
        corpus_sorted.append(doc)
    return corpus_sorted
  

# migliori consigli ordinati in base allo score
def get_recommendations(N, scores):
    # load in recipe dataset 
    global df
    # oridina in basse allo score
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:N]
    # crea un dataframe per caricarci le raccomandazioni
    recommendation = pd.DataFrame(columns = ['ricetta', 'ingredienti', 'score'])
    count = 0
    for i in top:
        recommendation.at[count, 'ricetta'] = df['title'][i]
        recommendation.at[count, 'ingredienti'] = df['ingredients'][i]
        recommendation.at[count, 'score'] = "{:.3f}".format(float(scores[i]))
        count += 1
    return recommendation

def get_recs(ingredients, N=5, mean=False):
    # carica modelo word2vec
    model = Word2Vec.load("model_cbow.bin")
	
    # carica in data
    global df
   
    # crea corpus
    corpus = get_and_sort_corpus(df)

    # usa TF-IDF come pesi per ogni incorporamento di parole
    tfidf_vec_tr = TfidfEmbeddingVectorizer(model)
    tfidf_vec_tr.fit(corpus)
    doc_vec = tfidf_vec_tr.transform(corpus)
    doc_vec = [doc.reshape(1, -1) for doc in doc_vec]
    assert len(doc_vec) == len(corpus)

    input = ingredients
    input = input.split(",")

    input_embedding = tfidf_vec_tr.transform([input])[0].reshape(1, -1)
    # ottieni la similarità del coseno tra input embedding e tutti gli embeddings del documento
    cos_sim = map(lambda x: cosine_similarity(input_embedding, x)[0][0], doc_vec)
    scores = list(cos_sim)
    # prendi le prime N raccomandazioni
    recommendations = get_recommendations(N, scores)
    return recommendations

def start_search(n,input_ingredients,scelta):
        
        global df

        if input_ingredients !="":
            ingredients=input_ingredients

            result_text.insert(tk.END, "\n---Ingredienti inseriti in Input: "+ingredients)

        elif n>=0:
            print(" \n avvio ricerca ricette....")

            ingredients=df['ingredients'][n]

            result_text.insert(tk.END,"\n-----Consigli per la ricetta: "+df['title'][n])
            result_text.insert(tk.END, "\n---ingredienti ricetta: "+ingredients)

            

        if scelta==0:
            recs = get_recs(ingredients)  
            i=1
            while i<len(recs):

                result_text.insert(tk.END, "\n---"+recs.ricetta[i])
                i+=1
        elif scelta==1:
            recs=clustering(n)
            i=0
            for recipe in recs['title']:
                if i>0:
                    result_text.insert(tk.END, "\n---"+recipe)
                i+=1
        else:
            recs=fastClustering(n)
            i=0
            for recipe in recs['title']:
                if i>0:
                    result_text.insert(tk.END, "\n---"+recipe)
                i+=1


def on_closing():
    if messagebox.askokcancel("Quit", "Vuoi uscire dall'applicazione?"):
        root.destroy()

def get_audio_input():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Dimmi gli ingredienti che hai ")
        audio = r.listen(source)
    ingredients = r.recognize_google(audio, language ="it-IT")
    ingredients_list = ingredients.split()
    ingredients_string=",".join(ingredients_list)
    input_text.delete(0,tk.END)
    input_text.insert(0,ingredients_string)


ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


#funzione che cambia l'aspetto grafico della GUI
def change_appearance_mode_event(new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
        
#funzione che effettua lo scaling della GUI
def change_scaling_event( new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)


def printInitialRecipe():
   
    
    global vars
    global checkboxes
    global numbers
    
    vars = []
    checkboxes = []
    numbers=[]
    
    for i in range(4):
        for j in range(3):
            buttons_frame.rowconfigure(i, weight=1, minsize=100)
            buttons_frame.columnconfigure(j, weight=1, minsize=150)
            n= randrange(0,6030)
            random_recipe=df['title'][n]
            random_ingredients=df['ingredients'][n]
            var = tk.IntVar()
            vars.append(var)
            checkbox_1 = ctk.CTkCheckBox(buttons_frame, text=random_recipe, variable=var)
            checkbox_1.grid(row=i, column=j, padx=20, pady=(20, 10), sticky="nsew")
            checkboxes.append(checkbox_1)
            numbers.append(n)     

   
def show_recipes():
    sidebar_button_1.grid()
    result_text.pack_forget()
    buttons_frame.pack(pady=10,padx=10,fill="both",expand=True,side="top")

def new_recipes():
    sidebar_button_1.grid()
    result_text.pack_forget()
    buttons_frame.pack_forget()
    buttons_frame.pack(pady=10,padx=10,fill="both",expand=True,side="top")
    
    printInitialRecipe()

def show_selected():
    sidebar_button_1.grid_remove()
    scelta=radio_var.get()
    if scelta==0:
        print("Scelta: Word2Vec")
    elif scelta==1:
        print("Scelta: K-Means")
    else:
        print("Scelta: K-Means Strategy 1")
	
    global vars
    global checkboxes
    global numbers
    
    selected = []
    result_text.pack(pady=10,padx=10,fill="both",expand=True,side="top")
    result_text.configure(state='normal',font=("Arial Black",20))
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "\nRISULTATI\n")
    for i in range(len(vars)):
        var = vars[i]
        result=""
        if var.get() == 1:
            selected.append(checkboxes[i].cget("text")+ " indx dataset: "+str(numbers[i]))
            print(selected)
            start_search(numbers[i],"",scelta)

    buttons_frame.pack_forget()
    
    



    if input_text.get() !='':
        ingredients = input_text.get()
        start_search(-1,ingredients,0)
        


    result_text.insert(tk.END, "\n")   

        
    
   

    
    
    
root= ctk.CTk()
root.geometry("1280x720 ")
root.title("No Waste")

sidebar_frame= ctk.CTkFrame(root)
sidebar_frame.pack(pady=10,padx=10,fill="both", side="left")


input_frame= ctk.CTkFrame(root)
input_frame.pack(pady=10,padx=10,fill="both",side="bottom")

buttons_frame=ctk.CTkFrame(root)
buttons_frame.pack(pady=10,padx=10,fill="both",expand=True,side="top")

result_text = ctk.CTkTextbox(root, state='disabled')
df = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')
df.dropna(subset=['ingredients'], inplace=True)
df.reset_index(drop=True, inplace=True)
df['ingredients'] = df.ingredients.values.astype('U')

vars = []
checkboxes = []
numbers=[]

printInitialRecipe()


logo_label = ctk.CTkLabel(sidebar_frame, text="No Waste")
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


#bottoni

sidebar_button_1 = ctk.CTkButton(sidebar_frame,text="Avvia Ricerca",command=show_selected,font=("Helvetica", 14))
sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
sidebar_button_2 = ctk.CTkButton(sidebar_frame,text="Lista Ricette",command=show_recipes,font=("Helvetica", 14))
sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
sidebar_button_3 = ctk.CTkButton(sidebar_frame,text="Nuove Ricette",command=new_recipes,font=("Helvetica", 14))
sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)


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

radio_var = tkinter.IntVar(value=0)
label_radio_group = ctk.CTkLabel(master=sidebar_frame, text="Scelta:")
label_radio_group.grid(row=9, column=0, columnspan=1, padx=10, pady=10, sticky="")
radio_button_1 = ctk.CTkRadioButton(master=sidebar_frame, variable=radio_var, value=0, text="Word2Vec")
radio_button_1.grid(row=10, column=0, pady=10, padx=20, sticky="s")
radio_button_2 = ctk.CTkRadioButton(master=sidebar_frame, variable=radio_var, value=1,text="K-means Strategy2")
radio_button_2.grid(row=11, column=0, pady=10, padx=20, sticky="s")
radio_button_3 = ctk.CTkRadioButton(master=sidebar_frame, variable=radio_var, value=2,text="K-means strategy1")
radio_button_3.grid(row=12, column=0, pady=10, padx=20, sticky="s")

input_text = ctk.CTkEntry(input_frame, placeholder_text="Inserisci Ingredienti",font=("Helvetica", 14))
input_text.grid(row=0,column=0,pady=10, padx=10,columnspan=2,sticky='nsew')

mic_button = ctk.CTkButton(input_frame, text="Mic",command=get_audio_input,height= 50, width=5)
mic_button.grid(row=0,column=1,pady=10, padx=10,columnspan=2,sticky='nsew')

input_frame.columnconfigure(0, weight=5)
input_frame.columnconfigure(1, weight=1)

#default values
appearance_mode_optionemenu.set("Dark")
scaling_optionemenu.set("100%")


if __name__ == "__main__":
   root.mainloop()
