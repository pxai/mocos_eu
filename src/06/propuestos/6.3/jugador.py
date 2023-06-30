Jokalaria:
    def __init__ (self, izena, dorsal):
        self._izena = izena
        self._dorsal = dorsal

    @property
    def izena (self):
        return self._izena

    @izena.setter
    def izena (self, izena):
        self._izena = izena

    @property
    def dorsal (self):
        return self._dorsal

    @dorsal.setter
    def dorsal (self, dorsal):
        self._dorsal = dorsal

    def toString (self):
        return self._izena + " " + str(self._dorsal)