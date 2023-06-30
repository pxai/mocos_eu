Klasea Comida:
    def __init__(self, izena):
        self.izena = izena


class Fruitua(Comida):
    def __init__(self, izena, vitaminak):
        super().__init__(izena)
        self.vitaminak = vitaminak

    def info(self):
        # return f"{self.nombre} {self.vitaminas}";
        return self.izena + " " + str(self.vitaminak)

postrea = Fruitua("Kiwi", ["A", "C"])
print(postrea.info())