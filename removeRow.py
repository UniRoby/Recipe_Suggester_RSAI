import csv
import re

unique_ingredients = []
count = 0


def read_file_to_array():
    global unique_ingredients
    with open("unique.txt", "r") as file:
        reader = file.readlines()
        for row in reader:
            row = re.sub(r'\n', '', row)
            unique_ingredients.append(row)



read_file_to_array()



def removeRow(ingredients,ricetta):
    ingredient_names = []

    for ingredient in ingredients.split(','):

        global unique_ingredients
        global count



        if ingredient in unique_ingredients:
            count += 1
            print(ingredient in unique_ingredients)
            print(ricetta+" rimossa")
            ingredient_names = None
            return ingredient_names




        if ingredient != '' and ingredient not in ingredient_names:
            ingredient_names.append(ingredient)

    return ingredient_names


with open('ricette.csv', mode='w', newline='', encoding='iso-8859-1') as csv_newFile:
    writer = csv.writer(csv_newFile)
    writer.writerow(['title', "ingredients", 'time', 'ratings', 'type', 'instructions'])
    # Apri il file CSV in modalità di lettura
    with open('ricette6k.csv', mode='r', encoding='iso-8859-1') as csv_file:
        # Crea un oggetto reader
        reader = csv.reader(csv_file)

        # Salta la prima riga (intestazione)
        next(reader)

        # Per ogni riga del file CSV

        for row in reader:
            ingredients = removeRow(row[1],row[0])

            if ingredients!=None:
                row[1] = str(ingredients)

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

print(count)
print("dataset cvs creato\n")