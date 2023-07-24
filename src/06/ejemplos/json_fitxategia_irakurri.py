import json

fitxategiarea = open("texto.json", "r")
edukia = json.load(fitxategiarea)

for pertsonaia in edukia:
    print(pertsonaia["nombre"])

fitxategiarea.close()