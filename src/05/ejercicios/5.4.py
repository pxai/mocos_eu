Kode Python hau itzuli ezazu baskeraz, aldagaiak lehen letra larritzen gabe:

class Piloto:
    def __init__(self, izena):
        self._izena = izena

    @property
    def izena (self):
        return self._izena

    @izena.setter
    def izena (self, izena):
        self._izena = izena



class Aeroplano:
    def __init__(self, modelo, piloto, kopiloto):
        self._modelo = modelo
        self._piloto = piloto
        self._kopiloto = kopiloto

    @property
    def modelo (self):
        return self._modelo

    @modelo.setter
    def modelo (self, modelo):
        self._modelo = modelo

    def hegaldu (self):
        return f"{self._modelo} modeloaren {self._piloto.izena} eta {self._kopiloto.izena} batekin hegaldia egiten"


piloto1 = Piloto("Han Solo")
piloto2 = Piloto("Murdock")
hegazkin-txikia = Aeroplano("AirBluff 727", piloto1, piloto2)

print(hegazkin-txikia.hegaldu())