import json

class Listado:
    def __init__ (self, nombreFichero):
        contenido = open(nombreFichero, "r")
        self._datos = json.load(contenido)
        contenido.close()

    def existitzenDa (self, izena):
        for datu in self._datos:
            if datu["izena"] == izena:
                return True

        return False

    def minuskulatuta (self):
        self._datos = list(map(lambda datu: { "id": datu["id"], "izena": datu["izena"].lower() }, self._datos))

    def posizioa (self, izena):
        i = 0
        for datu in self._datos:
            if datu["izena"] == izena:
                return i
            i += 1
        return -1

    def inprimatu (self):
        for datu in self._datos:
            print(datu)