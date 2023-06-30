Dispositibo klasea:
    def __init__(self, izena, prezioa):
        self._izena = izena
        self._prezioa = prezioa

    def get_izena():
        return self._izena

    def set_izena(izena):
        self._izena = izena

    def get_prezioa():
        return self._prezioa

    def set_prezioa(prezioa):
        self._prezioa = prezioa

    def toString(self):
        return f"{self._izena} {self._prezioa}";


class Mugikorra(Dispositibo):
    def __init__(self, izena, prezioa, zenbakia):
        super().__init__(izena, prezioa)
        self._zenbakia = zenbakia

    @property
    def zenbakia(self):
        return self._zenbakia

    @zenbakia.setter
    def zenbakia(self, zenbakia):
        self._zenbakia = zenbakia

    def toString(self):
        return f"{super().toString()} {self._zenbakia}"

    def deitu(zenbakia):
        print("Deitzen", zenbakia)


class Ordenagailua(Dispositibo):
    def __init__(self, izena, prezioa, prozesadorea):
        super().__init__(izena, prezioa)
        self._prozesadorea = prozesadorea

    @property
    def prozesadorea(self):
        return self._prozesadorea

    @prozesadorea.setter
    def prozesadorea(self, prozesadorea):
        self._prozesadorea = prozesadorea

    def toString(self):
        return f"{super().toString()} {self._prozesadorea}"


ordenagailua = Ordenagailua("Dell", 4553.4, "Lentium 4")
telefonoa = Mugikorra("Chanmhung", 434.4, 665745345)

print("Ordenagailua:", ordenagailua.toString())
print("Telefonoa:", telefonoa.toString())