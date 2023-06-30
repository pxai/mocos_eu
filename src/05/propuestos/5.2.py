Klasea Sumador:
    def __init__(self, balio1, balio2):
        self.balio1 = balio1
        self.balio2 = balio2

    @property
    def balio1 (self):
        return self._balio1

    @balio1.setter
    def balio1 (self, balio1):
        if balio1 > 0:
            self._balio1 = balio1
        else:
            self._balio1 = 0

    @property
    def balio2 (self):
        return self._balio2

    @balio2.setter
    def balio2 (self, balio2):
        if balio2 > 0:
            self._balio2 = balio2
        else:
            self._balio2 = 0

    def batu (self):
        return self._balio1 + self._balio2


sumador = Sumador(28, 14)
print(sumador.batu())

sumador.balio1 = 600
sumador.balio2 = 66
print(sumador.batu())