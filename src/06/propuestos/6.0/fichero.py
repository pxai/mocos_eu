Fichero klasea:
    def __init__(self, nombreFichero):
        self._nombreFichero = nombreFichero

    def irakurri(self):
        fichero = open(self._nombreFichero, "r")
        datuak = fichero.read()
        fichero.close()

        return datuak

    def idatzi(self, eduki):
        fichero = open(self._nombreFichero, "w+")
        fichero.write(eduki)
        fichero.close()