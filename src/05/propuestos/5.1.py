Klase bat sortu "IzenaFormatuta" izenarekin:

class IzenaFormatuta:
    def __init__(self, izena, abizena):
        self._izena = izena
        self._abizena = abizena

    def formatu (self):
        return self._zuzendu(self._izena) + " " + self._zuzendu(self._abizena)


    def _zuzendu (self, katea):
        return self._lehenengo(katea) + self._gainera(katea)


    def _lehenengo (self, katea):
        return katea[0].lower()


    def _gainera (self, katea):
        return katea[1:len(katea)].lower()


formatuador = IzenaFormatuta("JUAN", "PÉREZ")
print(formatuador.formatu())