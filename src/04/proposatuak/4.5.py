import random

def ausazkoa(max):
    return random.randint(0, max - 1)

def izenaSortu(silabak):
    oinak = ["a", "e", "i", "o", "u"]
    konsonanteak = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
    izena = ""

    for i in range(silabak):
        konsonantea = konsonanteak[ausazkoa(len(konsonanteak))]
        oina = oinak[ausazkoa(len(oinak))]
        izena = izena + konsonantea + oina

    return izena

print(izenaSortu(3))