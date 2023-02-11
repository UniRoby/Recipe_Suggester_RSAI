import csv
import statistics
import re


def ingredientRoot(ingredient):

        if ingredient=='olio ':
            ingredient="olio extravergine d'oliva"
        if ingredient=='alchermes o altro aroma a scelta':
            ingredient=""
        if ingredient=='smarties e':
            ingredient=""
        if ingredient=='semola duro per la spianatoia':
            ingredient=""
        if ingredient=='torta al cioccolato':
            ingredient=""
        if ingredient=="preparato per confetture:":
            ingredient=""


        if 'alcol' in ingredient:
            ingredient = 'alcol'
        if 'salsa piccante' in ingredient:
            ingredient = 'salsa piccante'
        if 'zafferano' in ingredient:
            ingredient = 'zafferano'
        if 'piadine' in ingredient:
            ingredient = 'piadine'
        if 'uvetta' in ingredient:
            ingredient = 'uvetta'
        if 'porri' in ingredient:
            ingredient = 'porri'
        if 'topping' in ingredient:
            ingredient = 'topping'
        if 'salsa di soia' in ingredient:
            ingredient = 'salsa di soia'
        if 'alga' in ingredient:
            ingredient = 'alga'
        if 'biscotti' in ingredient:
            ingredient = 'biscotti'
        if 'prugne' in ingredient:
            ingredient = 'prugne'
        if 'mortadella' in ingredient:
            ingredient = 'mortadella'
        if 'salsiccia' in ingredient:
            ingredient = 'salsiccia'
        if 'lievito' in ingredient:
            ingredient = 'lievito'
        if 'cocco' in ingredient:
            ingredient = 'cocco'
        if 'mozzarell' in ingredient:
            ingredient = 'mozzarella'
        if 'spaghett' in ingredient:
            ingredient = 'spaghetti'
        if 'fave' in ingredient:
            ingredient = 'fave'
        if 'parmigiano reggiano' in ingredient:
            ingredient = 'parmigiano reggiano'
        if 'broccol' in ingredient:
            ingredient = 'broccoli'
        if 'broccol' in ingredient:
            ingredient = 'broccoli'
        if 'tacchino' in ingredient:
            ingredient = 'tacchino'
        if 'whisky' in ingredient:
            ingredient = 'whisky'
        if 'lime' in ingredient:
            ingredient = 'lime'
        if 'spinac' in ingredient:
            ingredient = 'spinaci'
        if 'polpo' in ingredient:
            ingredient = 'polpo'
        if 'rum' in ingredient:
            ingredient = 'rum'
        if 'timo' in ingredient:
            ingredient = 'timo'
        if 'guanciale' in ingredient:
            ingredient = 'guanciale'
        if 'pak choi' in ingredient:
            ingredient = 'pak choi'
        if 'fontina' in ingredient:
            ingredient = 'fontina'
        if 'marmellata' in ingredient:
            ingredient = 'marmellata'
        if 'sedano' in ingredient:
            ingredient = 'sedano'
        if 'funghi' in ingredient:
            ingredient = 'funghi'
        if 'orata' in ingredient:
            ingredient = 'orata'
        if 'panna liquida' in ingredient:
            ingredient = 'panna'
        if 'melanzane' in ingredient:
            ingredient='melanzane'
        if 'tuorl' in ingredient:
            ingredient='uova'
        if 'pesce spada' in ingredient:
            ingredient='pesce spada'
        if 'merluzz' in ingredient:
            ingredient='merluzzo'
        if 'ciliegie' in ingredient:
            ingredient='ciliegie'
        if 'passata di pomodoro' in ingredient:
            ingredient='passata di pomodoro'
        if 'aranc' in ingredient:
            ingredient='arance'
        if 'rosmarino' in ingredient:
            ingredient='rosmarino'
        if 'anatra' in ingredient:
            ingredient='anatra'
        if 'coniglio' in ingredient:
            ingredient='coniglio'
        if 'fichi' in ingredient:
            ingredient='fichi'
        if 'crema di marroni' in ingredient:
            ingredient='crema di marroni'
        if 'ananas' in ingredient:
            ingredient='ananas'
        if 'provolone' in ingredient:
            ingredient='provolone'
        if 'mozzarella' in ingredient:
            ingredient='mozzarella'
        if 'carne bovina' in ingredient:
            ingredient='carne bovina'
        if 'carne di suino' in ingredient:
            ingredient='carne di suino'
        if 'scarola' in ingredient:
            ingredient='cavolo'
        if 'cavolo' in ingredient:
            ingredient='cavolo'
        if 'cavolfiore' in ingredient:
            ingredient='cavolfiore'
        if 'gamberetti' in ingredient:
            ingredient='gamberetti'
        if 'zucca' in ingredient:
            ingredient='zucca'
        if 'cereali' in ingredient:
            ingredient='cereali'
        if 'aglio' in ingredient:
            ingredient='aglio'
        if 'speck' in ingredient:
            ingredient='speck'
        if 'fruttapec' in ingredient:
            ingredient='carne bovina'
        if 'fruttapec' in ingredient:
            ingredient='fruttapec'
        if 'albicocche' in ingredient:
            ingredient='albicocche'
        if 'tè verde' in ingredient:
            ingredient='tè verde'
        if 'banan' in ingredient:
            ingredient='banane'
        if 'prosciutto cotto' in ingredient:
            ingredient='prosciutto cotto'
        if 'prosciutto crudo' in ingredient:
            ingredient='prosciutto crudo'
        if 'farfalle' in ingredient:
            ingredient='farfalle'
        if 'pere' in ingredient:
            ingredient='pere'
        if 'la bottega di olivia' in ingredient:
            ingredient='cracker'
        if 'nocciole' in ingredient:
            ingredient='nocciole'
        if 'panna fresca liquida' in ingredient:
            ingredient='panna fresca liquida'
        if 'erbe' in ingredient:
            ingredient='erbe'
        if 'gelatina' in ingredient:
            ingredient='gelatina'
        if 'confetti' in ingredient:
            ingredient='confetti'
        if 'olio di semi' in ingredient:
            ingredient='olio di semi'
        if 'lenticchie' in ingredient:
            ingredient='lenticchie'
        if 'pasta sfoglia' in ingredient:
            ingredient='pasta sfoglia'
        if 'sardine' in ingredient:
            ingredient='sardine'
        if 'miele' in ingredient:
            ingredient='miele'
        if 'kiwi' in ingredient:
            ingredient='kiwi'
        if 'senape' in ingredient:
            ingredient='senape'
        if 'finocchietto' in ingredient:
            ingredient='finocchietto'
        if 'melone' in ingredient:
            ingredient='melone'
        if 'cioccolato fondente' in ingredient:
            ingredient='cioccolato fondente'
        if 'pancetta' in ingredient:
            ingredient='pancetta'
        if 'scampi' in ingredient:
            ingredient='scampi'
        if 'limon' in ingredient:
            ingredient='limone'
        if 'tonno' in ingredient:
            ingredient='tonno'
        if 'maiale' in ingredient:
            ingredient='carne di suino'
        if 'spezie' in ingredient:
            ingredient='spezie'
        if 'broccoli' in ingredient:
            ingredient='broccoli'
        if 'carciofi' in ingredient:
            ingredient='carciofi'
        if 'cipoll' in ingredient:
            ingredient='cipolle'
        if 'acqua' in ingredient:
            ingredient='acqua'
        if 'peperoni' in ingredient:
            ingredient='peperoni'
        if 'manzo' in ingredient:
            ingredient='manzo'
        if 'pistacchi' in ingredient:
            ingredient='pistacchi'
        if 'zucchero' in ingredient:
            ingredient='zucchero'
        if 'barbecue' in ingredient:
            ingredient='salsa barbecue'
        if 'pisellini' in ingredient:
            ingredient='pisellini'
        if 'cacao' in ingredient:
            ingredient='cacao'
        if 'uov' in ingredient:
            ingredient='uova'
        if 'pepe' in ingredient:
            ingredient='pepe'
        if 'pane' in ingredient:
            ingredient='pane'
        if 'basilico' in ingredient:
            ingredient='basilico'
        if 'cipolle' in ingredient:
            ingredient='cipolle'
        if 'capper' in ingredient:
            ingredient='capperi'
        if 'aceto' in ingredient:
            ingredient='aceto'
        if 'polenta' in ingredient:
            ingredient='polenta'
        if 'olive' in ingredient:
            ingredient='olive'
        if 'fagioli' in ingredient:
            ingredient='fagioli'
        if 'pomodori' in ingredient:
            ingredient='pomodori'
        if 'pollo' in ingredient:
            ingredient='pollo'
        if 'sale' in ingredient:
            ingredient='sale'
        if 'acciughe' in ingredient:
            ingredient='acciughe'
        if 'coloranti alimentari' in ingredient:
            ingredient ='coloranti alimentari'
        if 'caffè' in ingredient:
            ingredient ='caffè'
        if 'vino' in ingredient:
            ingredient='vino'
        if 'farina' in ingredient:
            ingredient='farina'
        if 'mele' in ingredient:
            ingredient='mele'
        if 'riso' in ingredient:
            ingredient='riso'
        if 'uva' in ingredient:
            ingredient='uva'
        if 'luganega' in ingredient:
            ingredient = 'salsiccia'
        if 'burro' in ingredient:
            ingredient='burro'
        if 'wafer' in ingredient:
            ingredient='wafer'
        if 'ricotta' in ingredient:
            ingredient='ricotta'
        if 'insalata' in ingredient:
            ingredient = 'insalata'
        if 'lasagne' in ingredient:
            ingredient = 'lasagne'
        if 'carot' in ingredient:
            ingredient = 'carote'
        if 'zucchine' in ingredient:
            ingredient = 'zucchine'
        if 'mais' in ingredient:
            ingredient = 'mais'
        if 'yogurt' in ingredient:
            ingredient = 'yogurt'
        if 'extravergine' in ingredient:
            ingredient = "olio extravergine d'oliva"
        if 'gelato' in ingredient:
            ingredient = 'gelato'
        if 'vitello' in ingredient:
            ingredient = 'vitello'
        if 'brodo' in ingredient:
            ingredient = 'brodo'
        if 'gamberi' in ingredient:
            ingredient = 'gamberi'
        if 'salmone' in ingredient:
            ingredient = 'salmone'
        if 'salame' in ingredient:
            ingredient = 'salame'
        if 'noci' in ingredient:
            ingredient = 'noci'
        if 'formaggio fresco spalmabile' in ingredient:
            ingredient = 'formaggio fresco spalmabile'
        if 'vaniglia' in ingredient:
            ingredient = 'vaniglia'
        if 'latte' in ingredient:
            ingredient = 'latte'
        if 'menta' in ingredient:
            ingredient = 'menta'
        if 'birra' in ingredient:
            ingredient = 'birra'
        if 'agnello' in ingredient:
            ingredient = 'agnello'
        if 'mix di frutta secca' in ingredient:
            ingredient = 'mix di frutta secca'
        if 'patate' in ingredient:
            ingredient = 'patate'
        if 'pecorino' in ingredient:
            ingredient = 'pecorino'
        if 'mandarini' in ingredient:
            ingredient = 'mandarini'
        if 'salvia' in ingredient:
            ingredient = 'salvia'
        if 'biscotti' in ingredient:
            ingredient = 'biscotti'
        if 'mandorl' in ingredient:
            ingredient = 'mandorle'
        if 'marmellata' in ingredient:
            ingredient = 'marmellata'
        if 'tabasco' in ingredient:
            ingredient = 'tabasco'
        if 'lattuga' in ingredient:
            ingredient = 'lattuga'
        if 'prezzemolo' in ingredient:
            ingredient = 'prezzemolo'
        if 'prugne' in ingredient:
            ingredient = 'prezzemolo'
        if 'confettura' in ingredient:
            ingredient = 'marmellata'
        if 'panini' in ingredient:
            ingredient = 'panini'
        if 'penne' in ingredient:
            ingredient = 'penne'
        if 'semi' in ingredient:
            ingredient = 'semi'
        if 'zenzero' in ingredient:
            ingredient = 'zenzero'
        if 'cannella' in ingredient:
            ingredient = 'cannella'
        if 'paprika' in ingredient:
            ingredient = 'paprika'
        if 'pinoli' in ingredient:
            ingredient = 'pinoli'
        if 'grano' in ingredient:
            ingredient = 'grano'
        if 'semol' in ingredient:
            ingredient = 'semola'
        if 'gorgonzola' in ingredient:
            ingredient = 'gorgonzola'
        if 'carciofo' in ingredient:
            ingredient = 'carciofo'
        if 'pesche' in ingredient:
            ingredient = 'pesche'
        if 'galletto' in ingredient:
            ingredient = 'pollo'
        if 'pasta fillo' in ingredient:
            ingredient = 'pasta fillo'
        if 'maggiorana' in ingredient:
            ingredient = 'maggiorana'
        if 'gnocch' in ingredient:
            ingredient = 'gnocchi'
        if 'radicchio' in ingredient:
            ingredient = 'radicchio'
        if 'noce moscata' in ingredient:
            ingredient = 'noce moscata'
        if 'worcestershire' in ingredient:
            ingredient = 'salsa worcestershire'
        if 'pesce' in ingredient:
            ingredient = 'pesce'
        if 'pepi' in ingredient:
            ingredient = 'pepe'
        if 'liquore' in ingredient:
            ingredient = 'liquore'
        if 'arachidi' in ingredient:
            ingredient = 'arachidi'
        if 'origano' in ingredient:
            ingredient = 'origano'
        return ingredient
          

def cleanIngredients(ingredients):
    ingredient_names = []

    for ingredient in ingredients.split(','):
        # Rimuovi parentesi e abbreviazioni dalla stringa
        ingredient = ingredient.lower()


        ingredient = re.sub(r",", "", ingredient)
        ingredient = re.sub(r'\(.*\)', '', ingredient)
        ingredient = re.sub(r'q.b.', '', ingredient)
        ingredient = re.sub(r'q.b', '', ingredient)
        ingredient = re.sub(r'[0-9]+,[0-9]+', '', ingredient)
        ingredient = re.sub(r'\d+ gr', '', ingredient)
        ingredient = re.sub(r'\d+ g', '', ingredient)
        ingredient = re.sub(r' da kg', '', ingredient)
        ingredient = re.sub(r' kg', '', ingredient)
        ingredient = re.sub(r'\d+ lt', '', ingredient)
        ingredient = re.sub(r'\d+ l', '', ingredient)
        ingredient = re.sub(r' ml', '', ingredient)
        ingredient = re.sub(r'[0-9]', '', ingredient)
        ingredient = re.sub(r'½', '', ingredient)
        ingredient = re.sub(r'¼', '', ingredient)
        ingredient = re.sub(r'%', '', ingredient)
        ingredient = re.sub(r' ciuffo', '', ingredient)
        ingredient = re.sub(r' freschissimo', '', ingredient)
        ingredient = re.sub(r" senza glutine", "", ingredient)
        ingredient = re.sub(r" medie", "", ingredient)
        ingredient = re.sub(r" tamari", "", ingredient)
        ingredient = re.sub(r" in grani", "", ingredient)
        ingredient = re.sub(r" la parte verde", "", ingredient)
        ingredient = re.sub(r" carcasse intere", "", ingredient)
        ingredient = re.sub(r" spicchio", "", ingredient)
        ingredient = re.sub(r" spicchi", "", ingredient)
        ingredient = re.sub(r" in stecche", "", ingredient)
        ingredient = re.sub(r" in polvere", "", ingredient)
        ingredient = re.sub(r' fino', '', ingredient)
        ingredient = re.sub(r" grossolanamente", "", ingredient)
        ingredient = re.sub(r' grosso', '', ingredient)
        ingredient = re.sub(r' grossa', '', ingredient)
        ingredient = re.sub(r' grossi', '', ingredient)
        ingredient = re.sub(r" dop", "", ingredient)
        ingredient = re.sub(r" cucchiaio", "", ingredient)
        ingredient = re.sub(r" cucchiaino", "", ingredient)
        ingredient = re.sub(r" cucchiai", "", ingredient)
        ingredient = re.sub(r' cucchiaini', '', ingredient)
        ingredient = re.sub(r" sgusciati", "", ingredient)
        ingredient = re.sub(r" già", "", ingredient)
        ingredient = re.sub(r" macinata", "", ingredient)
        ingredient = re.sub(r" rametto", "", ingredient)
        ingredient = re.sub(r" rametti", "", ingredient)
        ingredient = re.sub(r" intero", "", ingredient)
        ingredient = re.sub(r" denocciolati", "", ingredient)
        ingredient = re.sub(r" denocciolate", "", ingredient)
        ingredient = re.sub(r" marino", "", ingredient)
        ingredient = re.sub(r" integrale", "", ingredient)
        ingredient = re.sub(r" integrali", "", ingredient)
        ingredient = re.sub(r" calda", "", ingredient)
        ingredient = re.sub(r" caldo", "", ingredient)
        ingredient = re.sub(r" fredda", "", ingredient)
        ingredient = re.sub(r" freddo", "", ingredient)
        ingredient = re.sub(r" ghiacciata", "", ingredient)
        ingredient = re.sub(r" da grattugiare", "", ingredient)
        ingredient = re.sub(r" grattugiato", "", ingredient)
        ingredient = re.sub(r" grattugiata", "", ingredient)
        ingredient = re.sub(r" non trattato", "", ingredient)
        ingredient = re.sub(r" freddo di frigo", "", ingredient)
        ingredient = re.sub(r" a temperatura ambiente", "", ingredient)
        ingredient = re.sub(r" intiepidito", "", ingredient)
        ingredient = re.sub(r" tiepida", "", ingredient)
        ingredient = re.sub(r" pizzico", "", ingredient)
        ingredient = re.sub(r" facoltativo", "", ingredient)
        ingredient = re.sub(r" selvatico", "", ingredient)
        ingredient = re.sub(r'®', '', ingredient)
        ingredient = re.sub(r' ½', '', ingredient)
        ingredient = re.sub(r' ¼', '', ingredient)
        ingredient = re.sub(r' %', '', ingredient)
        ingredient = re.sub(r" possibilmente biologiche", "", ingredient)
        ingredient = re.sub(r" secco", "", ingredient)
        ingredient = re.sub(r"baccello di ", "", ingredient)
        ingredient = re.sub(r" rossi piccanti", "", ingredient)
        ingredient = re.sub(r" gialli", "", ingredient)
        ingredient = re.sub(r" verdi", "", ingredient)
        ingredient = re.sub(r" rossi", "", ingredient)
        ingredient = re.sub(r" rosa", "", ingredient)
        ingredient = re.sub(r" neri", "", ingredient)

        ingredient = re.sub(r" rosso piccante", "", ingredient)
        ingredient = re.sub(r" morbido", "", ingredient)
        ingredient = re.sub(r" fresco dolce a fette", "", ingredient)
        ingredient = re.sub(r" dolce", "", ingredient)
        ingredient = re.sub(r" a fette", "", ingredient)
        ingredient = re.sub(r" fette", "", ingredient)
        ingredient = re.sub(r" macinato", "", ingredient)
        ingredient = re.sub(r" novelli", "", ingredient)
        ingredient = re.sub(r" secchi", "", ingredient)
        ingredient = re.sub(r" secco", "", ingredient)
        ingredient = re.sub(r" una manciata", "", ingredient)
        ingredient = re.sub(r" senza lattosio", "", ingredient)
        ingredient = re.sub(r" bollente", "", ingredient)
        ingredient = re.sub(r" mazzetto", "", ingredient)
        ingredient = re.sub(r" rettangolare da", "", ingredient)
        ingredient = re.sub(r" a pezzettoni", "", ingredient)
        ingredient = re.sub(r" cappelle", "", ingredient)
        ingredient = re.sub(r" ago qualche", "", ingredient)
        ingredient = re.sub(r" frizzante", "", ingredient)
        ingredient = re.sub(r" tonde viola", "", ingredient)
        ingredient = re.sub(r" fetta", "", ingredient)
        ingredient = re.sub(r" un'unica", "", ingredient)
        ingredient = re.sub(r" fine", "", ingredient)
        ingredient = re.sub(r" per ungere il vassoio", "", ingredient)
        ingredient = re.sub(r" per frittura italiano", "", ingredient)
        ingredient = re.sub(r" scarti della pulizia", "", ingredient)
        ingredient = re.sub(r" di cottura mestoli", "", ingredient)
        ingredient = re.sub(r" bianche", "", ingredient)
        ingredient = re.sub(r" di colfiorito", "", ingredient)
        ingredient = re.sub(r" piccolo", "", ingredient)
        ingredient = re.sub(r" di digione forte", "", ingredient)
        ingredient = re.sub(r"patate dolci", "patate", ingredient)
        ingredient = re.sub(r" foglia", "", ingredient)
        ingredient = re.sub(r" pulita e sbollentata", "", ingredient)
        ingredient = re.sub(r"anice un", "anice", ingredient)
        ingredient = re.sub(r" senza lattosio", "", ingredient)
        ingredient = re.sub(r" di tazza", "", ingredient)
        ingredient = re.sub(r" tazza", "", ingredient)
        ingredient = re.sub(r"succo di ", "", ingredient)
        ingredient = re.sub(r" solo foglie", "", ingredient)
        ingredient = re.sub(r" mesi di stagionatura", "", ingredient)
        ingredient = re.sub(r" al naturale", "", ingredient)
        ingredient = re.sub(r" per decorare", "", ingredient)
        ingredient = re.sub(r" di curry giallo", "", ingredient)
        ingredient = re.sub(r" acqua dei fasolari", "", ingredient)
        ingredient = re.sub(r" congelati", "", ingredient)
        ingredient = re.sub(r" circa", "", ingredient)
        ingredient = re.sub(r" saraceno", "", ingredient)
        ingredient = re.sub(r" di grano", "", ingredient)
        ingredient = re.sub(r" sottili", "", ingredient)
        ingredient = re.sub(r" o riccioli", "", ingredient)
        ingredient = re.sub(r" qualche", "", ingredient)
        ingredient = re.sub(r" per un totale di", "", ingredient)
        ingredient = re.sub(r" fuso", "", ingredient)
        ingredient = re.sub(r" da pulire", "", ingredient)
        ingredient = re.sub(r" surgelati", "", ingredient)
        ingredient = re.sub(r" pulita", "", ingredient)
        ingredient = re.sub(r" bicchiere", "", ingredient)
        ingredient = re.sub(r" ciuffetto", "", ingredient)
        ingredient = re.sub(r" sbucciate", "", ingredient)
        ingredient = re.sub(r" disossato", "", ingredient)
        ingredient = re.sub(r" di zucchina", "", ingredient)
        ingredient = re.sub(r" filetti", "", ingredient)
        ingredient = re.sub(r" semistagionato", "", ingredient)
        ingredient = re.sub(r" fetta", "", ingredient)
        ingredient = re.sub(r" in scaglie", "", ingredient)
        ingredient = re.sub(r" e pulite", "", ingredient)
        ingredient = re.sub(r" sgusciate", "", ingredient)
        ingredient = re.sub(r" precotti", "", ingredient)
        ingredient = re.sub(r" precotte", "", ingredient)
        ingredient = re.sub(r"trota salmonata da", "trota", ingredient)
        ingredient = re.sub(r" pulito", "", ingredient)
        ingredient = re.sub(r" puliti", "", ingredient)
        ingredient = re.sub(r" abbondante", "", ingredient)
        ingredient = re.sub(r" fettine", "", ingredient)
        ingredient = re.sub(r" grande", "", ingredient)
        ingredient = re.sub(r" da tritare", "", ingredient)
        ingredient = re.sub(r" tritato", "", ingredient)
        ingredient = re.sub(r" tritata", "", ingredient)
        ingredient = re.sub(r" tritate", "", ingredient)
        ingredient = re.sub(r" l'uno", "", ingredient)
        ingredient = re.sub(r" di vinacciolo", "", ingredient)
        ingredient = re.sub(r" un pezzo", "", ingredient)
        ingredient = re.sub(r" mezzo", "", ingredient)
        ingredient = re.sub(r" bicchierino", "", ingredient)
        ingredient = re.sub(r" tipo tuc", "", ingredient)
        ingredient = re.sub(r" metà", "", ingredient)
        ingredient = re.sub(r" mezzo", "", ingredient)
        ingredient = re.sub(r" grandi", "", ingredient)
        ingredient = re.sub(r" pezzetto", "", ingredient)
        ingredient = re.sub(r" precotto", "", ingredient)
        ingredient = re.sub(r" polpa a pezzi", "", ingredient)
        ingredient = re.sub(r" per il piano", "", ingredient)
        ingredient = re.sub(r" rimacinata", "", ingredient)
        ingredient = re.sub(r" fogli", "", ingredient)
        ingredient = re.sub(r" grattuggiata", "", ingredient)
        ingredient = re.sub(r" a piacere", "", ingredient)
        ingredient = re.sub(r" macinati", "", ingredient)
        ingredient = re.sub(r" bocconcini", "", ingredient)        
        ingredient = re.sub(r" da montare", "", ingredient)
        ingredient = re.sub(r" piccole", "", ingredient)
        ingredient = re.sub(r" scaglie", "", ingredient)
        ingredient = re.sub(r" disidratato", "", ingredient)
        ingredient = re.sub(r" disidratati", "", ingredient)
        ingredient = re.sub(r" ciuffi", "", ingredient)
        ingredient = re.sub(r" freschi", "", ingredient)        
        ingredient = re.sub(r" foglie", "", ingredient)
        ingredient = re.sub(r" precotto da cui ricavare di polpa", "", ingredient)
        ingredient = re.sub(r" da filtrare", "", ingredient)
        ingredient = re.sub(r" affumicato", "", ingredient)
        ingredient = re.sub(r" affumicata", "", ingredient)
        ingredient = re.sub(r" lunghi - cm", "", ingredient)
        ingredient = re.sub(r" un pezzo", "", ingredient)        
        ingredient = re.sub(r" ragusano", "", ingredient)
        ingredient = re.sub(r" cotti", "", ingredient)
        ingredient = re.sub(r" lessato", "", ingredient)
        ingredient = re.sub(r" ¾", "", ingredient)
        ingredient = re.sub(r" media", "", ingredient)
        ingredient = re.sub(r" con guscio", "", ingredient)
        ingredient = re.sub(r" teste", "", ingredient)
        ingredient = re.sub(r" green", "", ingredient)
        ingredient = re.sub(r" mature", "", ingredient)
        ingredient = re.sub(r" pulite", "", ingredient)
        ingredient = re.sub(r" di cremona", "", ingredient)
        ingredient = re.sub(r" vegano", "", ingredient)
        ingredient = re.sub(r" affettato", "", ingredient)
        ingredient = re.sub(r" sottilmente", "", ingredient)
        ingredient = re.sub(r" in radici", "", ingredient)
        ingredient = re.sub(r" cespo", "", ingredient)
        ingredient = re.sub(r" sbriciolati", "", ingredient)
        ingredient = re.sub(r" baby e", "", ingredient)
        ingredient = re.sub(r" perlina", "", ingredient)
        ingredient = re.sub(r" medi", "", ingredient)
        ingredient = re.sub(r" crude", "", ingredient)
        ingredient = re.sub(r" da pestare", "", ingredient)
        ingredient = re.sub(r" mente", "", ingredient)
        ingredient = re.sub(r" rotolo", "", ingredient)
        ingredient = re.sub(r" una sola", "", ingredient)
        ingredient = re.sub(r" sodo", "", ingredient)
        ingredient = re.sub(r" montata", "", ingredient)
        ingredient = re.sub(r" intera", "", ingredient)
        ingredient = re.sub(r"cotto di ", "", ingredient)
        ingredient = re.sub(r" viola", "", ingredient)
        ingredient = re.sub(r" in una spessa", "", ingredient)
        ingredient = re.sub(r" fresco", "", ingredient)
        ingredient = re.sub(r" solubile ni", "", ingredient)
        ingredient = re.sub(r" cotte al forno", "", ingredient)
        ingredient = re.sub(r" consistenza", "", ingredient)
        ingredient = re.sub(r" di martina franca", "", ingredient)
        ingredient = re.sub(r" la scorza", "", ingredient)
        ingredient = re.sub(r" solo lee", "", ingredient)
        ingredient = re.sub(r"bicarbonato un", "bicarbonato", ingredient)
        ingredient = re.sub(r" soffiata", "", ingredient)
        ingredient = re.sub(r" scuro", "", ingredient)
        ingredient = re.sub(r" rosse", "", ingredient)
        ingredient = re.sub(r" bianchi", "", ingredient)
        ingredient = re.sub(r" da macinare", "", ingredient)
        ingredient = re.sub(r" selvatici", "", ingredient)
        ingredient = re.sub(r" selvatica", "", ingredient)
        ingredient = re.sub(r" grezze", "", ingredient)
        ingredient = re.sub(r" classici", "", ingredient)
        ingredient = re.sub(r" di ariccia", "", ingredient)
        ingredient = re.sub(r" stagionatura", "", ingredient)
        ingredient = re.sub(r"melissa e", "melissa", ingredient)
        ingredient = re.sub(r" rosso", "", ingredient)
        ingredient = re.sub(r" un trancio", "", ingredient)
        ingredient = re.sub(r" precedentemente ammollato e senza pelle", "", ingredient)
        ingredient = re.sub(r" sgranate e", "", ingredient)
        ingredient = re.sub(r" in spesse", "", ingredient)
        ingredient = re.sub(r" da sgusciare", "", ingredient)
        ingredient = re.sub(r" in busta", "", ingredient)
        ingredient = re.sub(r" oe secche", "", ingredient)
        ingredient = re.sub(r" secche", "", ingredient)
        ingredient = re.sub(r" radice", "", ingredient)
        ingredient = re.sub(r" pezzo", "", ingredient)
        ingredient = re.sub(r" pezzi", "", ingredient)
        ingredient = re.sub(r" a forma di roselline", "", ingredient)
        ingredient = re.sub(r" a forma di roselline", "", ingredient)
        ingredient = re.sub(r"  da ciascuno", "", ingredient)
        ingredient = re.sub(r" tazze", "", ingredient)
        ingredient = re.sub(r" trancio", "", ingredient)
        ingredient = re.sub(r" tranci", "", ingredient)
        ingredient = re.sub(r" facoltativa", "", ingredient)
        ingredient = re.sub(r" fresca", "", ingredient)
        ingredient = re.sub(r" la crosta", "", ingredient)
        ingredient = re.sub(r" da tagliare", "", ingredient)
        ingredient = re.sub(r" a julienne", "", ingredient)
        ingredient = re.sub(r" light", "", ingredient)
        ingredient = re.sub(r" piccola", "", ingredient)
        ingredient = re.sub(r" in sfoglie", "", ingredient)
        ingredient = re.sub(r" smarties e", "smarties", ingredient)
        ingredient = re.sub(r" stagionato o", "", ingredient)
        ingredient = re.sub(r" bianco", "", ingredient)
        ingredient = re.sub(r" nero", "", ingredient)
        ingredient = re.sub(r" pezzi", "", ingredient)
        ingredient = re.sub(r" piccoli", "", ingredient)
        ingredient = re.sub(r" siciliano", "", ingredient)
        ingredient = re.sub(r" romano", "", ingredient)
        ingredient = re.sub(r" scura", "", ingredient)
        ingredient = re.sub(r" secca", "", ingredient)
        ingredient = re.sub(r" intere", "", ingredient)
        ingredient = re.sub(r" sgocciolato", "", ingredient)
        ingredient = re.sub(r"granella di ", "", ingredient)
        ingredient = re.sub(r" sgocciolati", "", ingredient)
        ingredient = re.sub(r" di frigo", "", ingredient)
        ingredient = re.sub(r" tricolore", "", ingredient)
        ingredient = re.sub(r" da ammi ciascuna", "", ingredient)
        ingredient = re.sub(r" petali", "", ingredient)
        ingredient = re.sub(r" pugliesi", "", ingredient)
        ingredient = re.sub(r" ciliegino", "", ingredient)
        ingredient = re.sub(r" vasetto", "", ingredient)
        ingredient = re.sub(r" purea", "", ingredient)
        ingredient = re.sub(r" chicci", "", ingredient)
        ingredient = re.sub(r" succo", "", ingredient)
        ingredient = re.sub(r" da ciascuno", "", ingredient)
        ingredient = re.sub(r" sgocciolate", "", ingredient)
        ingredient = re.sub(r"gocce di ", "", ingredient)
        ingredient = re.sub(r" con sciroppo ", "", ingredient)
        ingredient = re.sub(r" sciroppate", "", ingredient)
        ingredient = re.sub(r" stagionata", "", ingredient)
        ingredient = re.sub(r" stecca", "", ingredient)
        ingredient = re.sub(r" bacca", "", ingredient)
        ingredient = re.sub(r" stellato", "", ingredient)
        ingredient = re.sub(r" rasi ni", "", ingredient)
        ingredient = re.sub(r" rinfrescato il giorno prima", "", ingredient)
        ingredient = re.sub(r" dischetti", "", ingredient)
        ingredient = re.sub(r"segatura di faggio", "", ingredient) #rimozione ingrediente
        ingredient = re.sub(r" abbattuta", "", ingredient)
        ingredient = re.sub(r" occe", "", ingredient)
        ingredient = re.sub(r"tuorlio", "tuorli", ingredient)
        ingredient = re.sub(r"pinoli ni", "pinoli", ingredient)
        ingredient = re.sub(r"salvia oline", "salvia", ingredient)
        ingredient = re.sub(r" anelli", "", ingredient)
        ingredient = re.sub(r" a cubetti", "", ingredient)
        ingredient = re.sub(r" farcire", "", ingredient)
        ingredient = re.sub(r" di una", "", ingredient)
        ingredient = re.sub(r" cespi", "", ingredient)
        ingredient = re.sub(r" belga", "", ingredient)
        ingredient = re.sub(r" di montagna", "", ingredient)
        ingredient = re.sub(r" il succo e", "", ingredient)
        ingredient = re.sub(r" non trattate", "", ingredient)
        ingredient = re.sub(r" da denocciolare", "", ingredient)
        ingredient = re.sub(r" stagionato", "", ingredient)
        ingredient = re.sub(r" lessati e strizzati", "", ingredient)
        ingredient = re.sub(r" abbattuto", "", ingredient)
        ingredient = re.sub(r" da ammi", "", ingredient)
        ingredient = re.sub(r" di modica", "", ingredient)
        ingredient = re.sub(r" del contadino", "", ingredient)
        ingredient = re.sub(r" purea", "", ingredient)
        ingredient = re.sub(r" polpa", "", ingredient)
        ingredient = re.sub(r" biologica", "", ingredient)
        ingredient = re.sub(r" cremoso", "", ingredient)
        ingredient = re.sub(r" fresche", "", ingredient)
        ingredient = re.sub(r" eviscerate", "", ingredient)
        ingredient = re.sub(r" spesse", "", ingredient)
        ingredient = re.sub(r" da ciascuna", "", ingredient)
        ingredient = re.sub(r" tipo cremini", "", ingredient)
        ingredient = re.sub(r"salsa di pomodoro", "pomodoro", ingredient)
        ingredient = re.sub(r" rettangolo da x cm", "", ingredient)
        ingredient = re.sub(r" lavata e precotta", "", ingredient)
        ingredient = re.sub(r"prezzemolo un", "prezzemolo", ingredient)
        ingredient = re.sub(r" in riccioli", "", ingredient)
        ingredient = re.sub(r"sarde sarde", "sarde", ingredient)
        ingredient = re.sub(r" salati", "", ingredient)
        ingredient = re.sub(r" scarti", "", ingredient)
        ingredient = re.sub(r" pizzichi", "", ingredient)
        ingredient = re.sub(r" per strauben", "", ingredient)
        ingredient = re.sub(r" mazzetti", "", ingredient)
        ingredient = re.sub(r" costola", "", ingredient)
        ingredient = re.sub(r" in pasta", "", ingredient)
        ingredient = re.sub(r" da sgranare", "", ingredient)
        ingredient = re.sub(r" eviscerato", "", ingredient)
        ingredient = re.sub(r" farcito", "", ingredient)
        ingredient = re.sub(r" - mesi", "", ingredient)
        ingredient = re.sub(r" cm di", "", ingredient)
        ingredient = re.sub(r" a pasta bianca", "", ingredient)
        ingredient = re.sub(r"in scatola", "", ingredient)
        ingredient = re.sub(r"gallina", "pollo", ingredient)
        ingredient = re.sub(r" sbriciolata", "", ingredient)
        ingredient = re.sub(r" in da l'una", "", ingredient)
        ingredient = re.sub(r" privato della scorza", "", ingredient)
        ingredient = re.sub(r" wakame o da cm", "", ingredient)
        ingredient = re.sub(r" in un unico", "", ingredient)
        ingredient = re.sub(r" da hot dog", "", ingredient)
        ingredient = re.sub(r" due", "", ingredient)
        ingredient = re.sub(r"ketchup o maionese", "", ingredient)
        ingredient = re.sub(r" spurgate", "", ingredient)
        ingredient = re.sub(r" a dadini", "", ingredient)
        ingredient = re.sub(r" semi-stagionata", "", ingredient)
        ingredient = re.sub(r" abbattuti", "", ingredient)
        ingredient = re.sub(r" puro gradazione °", "", ingredient)
        ingredient = re.sub(r" raso", "", ingredient)
        ingredient = re.sub(r"cotechino cotto", "", ingredient)
        ingredient = re.sub(r" cosce", "", ingredient)
        ingredient = re.sub(r" ossi", "", ingredient)
        ingredient = re.sub(r" unghi", "", ingredient)
        ingredient = re.sub(r" eviscerati", "", ingredient)
        ingredient = re.sub(r" atte", "", ingredient)
        ingredient = re.sub(r" surgelate", "", ingredient)
        ingredient = re.sub(r"mini ", "", ingredient)
        ingredient = re.sub(r"aroma di ", "", ingredient)
        ingredient = re.sub(r"aroma al ", "", ingredient)
        ingredient = re.sub(r"bucce di ", "", ingredient)
        ingredient = re.sub(r"mezzi ", "", ingredient)
        ingredient = re.sub(r" mista ", "", ingredient)
        ingredient = re.sub(r" disidratata", "", ingredient)
        ingredient = re.sub(r" crema di marroni", "crema di castagne", ingredient)
        ingredient = re.sub(r" salsa", "", ingredient)
        ingredient = re.sub(r" da cannolo", "", ingredient)
        ingredient = re.sub(r"grani di", "", ingredient)
        ingredient = re.sub(r"cookies", "biscotti", ingredient)
        ingredient = re.sub(r" romana", "", ingredient)
        ingredient = re.sub(r" silano", "", ingredient)
        ingredient = re.sub(r" o asparagina", "", ingredient)
        ingredient = re.sub(r"verza e", "verza", ingredient)
        ingredient = re.sub(r" riserva oltre mesi", "", ingredient)
        ingredient = re.sub(r" modena", "", ingredient)
        ingredient = re.sub(r" non zuccherati", "", ingredient)

        ingredient = re.sub(r"  ", " ", ingredient)
        ingredient = ingredient.strip()
        ingredient= ingredientRoot(ingredient)

        if ingredient!='' and ingredient not in ingredient_names:
            ingredient_names.append(ingredient)

    return ingredient_names




with open('ricetteEsatteMod.csv', mode='w', newline='',encoding='iso-8859-1') as csv_newFile:
        writer = csv.writer(csv_newFile)
        writer.writerow(['title', "ingredients", 'time', 'ratings', 'type', 'instructions'])
        # Apri il file CSV in modalità di lettura
        with open('ricetteEsatte.csv', mode='r',encoding='iso-8859-1') as csv_file:
            # Crea un oggetto reader
            reader = csv.reader(csv_file)
           
            # Salta la prima riga (intestazione)
            next(reader)
       
            # Per ogni riga del file CSV

            for row in reader:  
                            ingredients=cleanIngredients(row[1])
                            row[1]=str(ingredients)

                            row[1] = re.sub(r'\[', '', row[1])
                            row[1] = re.sub(r'\]', '', row[1])
                            row[1] = re.sub(r"'", '', row[1])
                            row[1] = re.sub(r'"', '', row[1])
                            row[1] = re.sub(r' ,', ',', row[1])
                            row[1] = re.sub(r', ', ',', row[1])
                            row[1] = re.sub(r"doliva", "d'oliva", row[1])
                            row[1] = row[1].strip()
                            row[1] = row[1].lower()
                            # scrivo nel nuovo file
                            newRow = [
                                row[0],
                                row[1],
                                row[2],
                                row[3],
                                row[4],
                                row[5]
                            ]

                            writer.writerow(newRow)
                  
print("dataset cvs creato\n")


