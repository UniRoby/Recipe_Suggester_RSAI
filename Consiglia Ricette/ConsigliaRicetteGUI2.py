import customtkinter as ctk
import tkinter
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from random import randrange

class MeanEmbeddingVectorizer(object):
    def __init__(self, word_model):
        self.word_model = word_model
        self.vector_size = word_model.wv.vector_size

    def fit(self):  # comply with scikit-learn transformer requirement
        return self

    def transform(self, docs):  # comply with scikit-learn transformer requirement
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
                mean.append(self.word_model.wv.get_vector(word))

        if not mean:  # parole vuote
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
  
# calculate average length of each document 
def get_window(corpus):
    lengths = [len(doc) for doc in corpus]
    avg_len = float(sum(lengths)) / len(lengths)
    return round(avg_len)

# Top-N recomendations order by score
def get_recommendations(N, scores):
    # load in recipe dataset 
    df_recipes = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')
    # order the scores with and filter to get the highest N scores
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:N]
    # crea un dataframe per caricarci le raccomandazioni
    recommendation = pd.DataFrame(columns = ['ricetta', 'ingredienti', 'score'])
    count = 0
    for i in top:
        recommendation.at[count, 'ricetta'] = df_recipes['title'][i]
        recommendation.at[count, 'ingredienti'] = df_recipes['ingredients'][i]
        recommendation.at[count, 'score'] = "{:.3f}".format(float(scores[i]))
        count += 1
    return recommendation

def get_recs(ingredients, N=5, mean=False):
    # load in word2vec model
    model = Word2Vec.load("model_cbow.bin")
   # model.init_sims(replace=True)
    #if model:
        #print("Modello caricato correttamente")
    # load in data
    data = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')
    
    # create corpus
    corpus = get_and_sort_corpus(data)
    
    if mean:
        #ottenere incorporamenti medi per ogni documento
        mean_vec_tr = MeanEmbeddingVectorizer(model)
        doc_vec = mean_vec_tr.transform(corpus)#corpus è un array
        doc_vec = [doc.reshape(1, -1) for doc in doc_vec]
        assert len(doc_vec) == len(corpus)
    else:
        # usa TF-IDF come pesi per ogni incorporamento di parole
        tfidf_vec_tr = TfidfEmbeddingVectorizer(model)
        tfidf_vec_tr.fit(corpus)
        doc_vec = tfidf_vec_tr.transform(corpus)
        doc_vec = [doc.reshape(1, -1) for doc in doc_vec]
        assert len(doc_vec) == len(corpus)

    # create embessing for input text
    input = ingredients
    # create tokens with elements
    input = input.split(",")

    # get embeddings for ingredient doc
    if mean:
        input_embedding = mean_vec_tr.transform([input])[0].reshape(1, -1)
    else:
        input_embedding = tfidf_vec_tr.transform([input])[0].reshape(1, -1)

    # get cosine similarity between input embedding and all the document embeddings
    cos_sim = map(lambda x: cosine_similarity(input_embedding, x)[0][0], doc_vec)
    scores = list(cos_sim)
    # Filter top N recommendations
    recommendations = get_recommendations(N, scores)
    return recommendations

def start_search(n,input_ingredients):
        
        df = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')
        result=""
        
        if input_ingredients !="":
            ingredients=input_ingredients
            result+="\n---Ingredienti inseriti in Input: "+ingredients
        elif n>=0:
            print(" \n avvio ricerca ricette....")
            print(" \n ing: "+df['ingredients'][n])
            ingredients=df['ingredients'][n]
            result+="\n-----Consigli per la ricetta: "+df['title'][n]
            result+="\n---ingredienti ricetta: "+ingredients
            
        result+="\n"
       
        recs = get_recs(ingredients)
            
        i=1
        while i<len(recs):
            #print(" \n "+recs.ricetta[i])
            #result_text.insert(tk.END,"\n---"+recs.ricetta[i])
            #result_text.insert(tk.END,recs.ingredienti[i])
            result+="\n---"+recs.ricetta[i]
            i+=1
        print(result)
        return result
            

    

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


class Recipe:
    def __init__(self,title, ingredients):
        self.id = id
        self.title = title
        self.ingredients = ingredients


def getRecipes():
    data = pd.read_csv("ricette6k.csv",encoding='iso-8859-1')
    # carica le ricette dal dataset
    recipes= []
    for index, row in data.iterrows():
        
        
        ingredientArray = []
        for ingredient in row[1].split(","):
            ingredient=ingredient.strip()
            ingredientArray.append(ingredient)
        
        recipe = Recipe(row["title"],ingredientArray)
        recipes.append(recipe)
    return recipes



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
    global vars
    global checkboxes
    global numbers
    
    selected = []
    for i in range(len(vars)):
        var = vars[i]
        result=""
        if var.get() == 1:
            selected.append(checkboxes[i].cget("text")+ " indx dataset: "+str(numbers[i]))
            
            result+=""+start_search(numbers[i],"")
    print("\nresult  show_selected")
    print(result)
    buttons_frame.pack_forget()
    
    

    result_text.pack(pady=10,padx=10,fill="both",expand=True,side="top")
    result_text.configure(state='normal',font=("Arial Black",20))
    '''
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "\n----------------------Selected:")
    result_text.insert(tk.END , selected)
    result_text.insert(tk.END, "\n")
    '''
    if input_text.get() !='':
        ingredients = input_text.get()
        result+=""+start_search(-1,ingredients)
        
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "\nRISULTATI\n")
    result_text.insert(tk.END , result)
    result_text.insert(tk.END, "\n")   
        #result_text.insert(tk.END, "Ingredienti inseriti: "+ ingredients)
        
    
   

    
    
    
root= ctk.CTk()
root.geometry("1280x720 ")
root.title("No wAIste")

sidebar_frame= ctk.CTkFrame(root)
sidebar_frame.pack(pady=10,padx=10,fill="both", side="left")

'''
show_frame = ctk.CTkFrame(root)
show_frame.pack(pady=10,padx=10,fill="both",expand=True,side="top")
result_text = tkinter.Text(show_frame, state='disabled')
result_text.pack(pady=10,padx=10,fill="both",expand=True)
'''
# create textbox
#textbox = ctk.CTkTextbox(root)
#textbox.insert("0.0", "CTkTextbox\n\n" + "")
#result_text = ctk.CTkTextbox(root, state='disabled')
#result_text.pack(pady=10,padx=10,fill="both",expand=True)
#result_text.pack(pady=10,padx=10,fill="both",expand=True,side="top")

input_frame= ctk.CTkFrame(root)
input_frame.pack(pady=10,padx=10,fill="both",side="bottom")

buttons_frame=ctk.CTkFrame(root)
buttons_frame.pack(pady=10,padx=10,fill="both",expand=True,side="top")

result_text = ctk.CTkTextbox(root, state='disabled')
df = pd.read_csv('ricette6k.csv',encoding='iso-8859-1')

vars = []
checkboxes = []
numbers=[]

printInitialRecipe()


logo_label = ctk.CTkLabel(sidebar_frame, text="No wAIste")
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
