Jokalaria:
    def __init__(self, izena, posizioa, dorsala):
        self._izena = izena
        self._posizioa = posizioa
        self._dorsala = dorsala

    def txosten (self):
        return f"{self._izena} {self._posizioa} {self._dorsala}"

    
Kepa:
    def __init__ (self, izena, sortzea, aurrekontua):
        self._izena = izena
        self._sortzea = sortzea
        self._aurrekontua = aurrekontua
        self._jokalariak = []

    def jokalariaFichatu (self, jokalaria):
        self._jokalariak.append(jokalaria)

    def jokalariakErakutsi (self):
        for jokalaria in self._jokalariak:
            print(jokalaria.txosten())


jokalaria1 = Jokalaria("Maradona", "Atalain", 10)
jokalaria2 = Jokalaria("Beckenbauer", "Defentsa", 4)

print(jokalaria1.txosten())

ekipoa = Kepa("New Team", 1983, 39944.45)
ekipoa.jokalariaFichatu(jokalaria1)
ekipoa.jokalariaFichatu(jokalaria2)

ekipoa.jokalariakErakutsi()