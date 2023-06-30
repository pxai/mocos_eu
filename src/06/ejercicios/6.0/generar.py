import random

def aleatorio (max):
    return random.randint(0, max - 1)

def generarPassword (longitud):
    caracteres = ["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",
        "0","1","2","3","4","5","6","7","8","9",".","-","_","!","$"]
    password = ""

    for i in range(longitud):
        caracter = caracteres[aleatorio(len(caracteres))]
        password = password + caracter

    return password