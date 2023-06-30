import random

def aleatorio (max):
    return random.randint(0, max)

class Moneda:
    def tirar (self):
        lados = ["aurpegi", "koroa"]
        numero = aleatorio(1)

        return lados[numero]

moneda = Moneda()

for i in range(10):
    print(moneda.tirar())