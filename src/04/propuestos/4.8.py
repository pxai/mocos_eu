import random

def aleatorio (maximo):
    return random.randint(0, maximo)

def generar_atributos (nivel_compensación):
    dar_puntos_a = 0
    inteligencia = 0
    fuerza = 0
    velocidad = 0

    puntos_restantes = 20
    puntos = 0

    while puntos_restantes > 0:
        if nivel_compensación > puntos_restantes:
            puntos = puntos_restantes
            puntos_restantes = 0
        else:
            puntos = aleatorio(nivel_compensación+1)
            puntos_restantes = puntos_restantes - puntos

        dar_puntos_a = aleatorio(3)

        if dar_puntos_a == 0:
            inteligencia = inteligencia + puntos
        elif dar_puntos_a == 1:
            fuerza = fuerza + puntos
        elif dar_puntos_a == 2:
            velocidad = velocidad + puntos

    print("\nBalioak konpentsazioaren arabera adierazita: ", nivel_compensación)
    print("Inteligentzia: ", inteligencia)
    print("Indarra: ", fuerza)
    print("Azkarera: ", velocidad)


generar_atributos(3)