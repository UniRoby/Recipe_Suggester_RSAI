import re

unique_ingredients=[]

with open("unique.txt", "r") as file:
    reader = file.readlines()

    for row in reader:
        row=re.sub(r'\n', '', row)
        unique_ingredients.append(row)


ingredients=[]
ingredients=['frutta mista','chiodi di garofano da ridurre']

for el in ingredients:
    if el in unique_ingredients:
        print(el)
