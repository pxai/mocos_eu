import random

def aleatorio(max):
    return random.randint(0, max - 1)

def generarNombre(silabak):
    oinak = ["a", "e", "i", "o", "u"]
    konsonanteak = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
    izena = ""

    for i in range(silabak):
        konsonantea = konsonanteak[aleatorio(len(konsonanteak))]
        oina = oinak[aleatorio(len(oinak))]
        izena = izena + konsonantea + oina

    return izena

print(generarNombre(3))