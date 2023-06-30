import random

def aleatorio (maximo):
    return random.randint(0, maximo)

class Dado:
    def __init__(self, lados = 6, admite_cero = False):
        self._lados = lados
        self._admite_cero = admite_cero

    @property
    def lados (self):
        return self._lados

    @lados.setter
    def lados (self, lados):
        self._lados = lados

    @property
    def admite_cero (self):
        return self._admite_cero

    @admite_cero.setter
    def admite_cero (self, admite_cero):
        self._admite_cero = admite_cero

    def tirar (self):
        numero =  aleatorio(self._lados)

        if not self._admite_cero:
            numero = numero + 1

        return numero



dado = Dado()
for i in range(10):
    print(dado.tirar())