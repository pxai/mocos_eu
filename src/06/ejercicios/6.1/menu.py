Klasea Menu:
    def __init__ (self, aukerak):
        self._opciones = aukerak

    def erakutsi (self):
        for i in range(len(self._opciones)):
            print(f"{i+1} {self._opciones[i]}")

    def hautatu (self, zenbakia):
        return zenbakia > 0 and zenbakia <= len(self._opciones)