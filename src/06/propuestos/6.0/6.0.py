datak importatu
importatu fitxategia

miFichero = fitxategia.Fichero("6.0.txt")

print("Aurreko edukia: ", miFichero.leer())

miFichero.escribir("Eduki aldatuta!!! " + str(date.today()))
print("Edukia:", miFichero.leer())