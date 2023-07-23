import random

def ausazkoa (maximoa):
    return random.randint(0, maximoa)

def atributuakSortu(konpentsaketaMaila):
    puntuakEman = 0
    adimena = 0
    indarra = 0
    abiadura = 0

    gainontzekoPuntuak = 20
    puntuak = 0

    while gainontzekoPuntuak > 0:
        if nivel_compensación > gainontzekoPuntuak:
            puntuak = gainontzekoPuntuak
            gainontzekoPuntuak = 0
        else:
            puntuak = aleatorio(konpentsaketaMaila+1)
            gainontzekoPuntuak = gainontzekoPuntuak - puntuak

        puntuakEman = aleatorio(3)

        if puntuakEman == 0:
            adimena = adimena + puntuak
        elif puntuakEman == 1:
            indarra = indarra + puntuak
        elif puntuakEman == 2:
            abiadura = abiadura + puntuak

    print("\nBalioak konpentsazioaren arabera adierazita: ", konpentsaketaMaila)
    print("Adimena: ", adimena)
    print("Indarra: ", indarra)
    print("Abiadura: ", abiadura)


atributuakSortu(3)