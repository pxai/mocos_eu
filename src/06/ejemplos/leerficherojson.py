import json

ficherorea = open("texto.json", "r")
edukia = json.load(ficherorea)

for pertsonaia in edukia:
    print(pertsonaia["nombre"])

ficherorea.close()