telefonoenak = {"Ada": 666555333, "Bug": 111000111 }

izena = input("Sartu izena: ")

del telefonoenak[izena]

for izena in telefonoenak.keys():
    print(izena, telefonoenak[izena])