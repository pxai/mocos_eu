import json

class Zereginak:
    def __init__ (self):
        fitxategia = open("zereginak.json", "r")
        self._zereginak = json.load(fitxategia)
        fitxategia.close()

    def sortu (self, id, tarea):
        berria = { "id": id, "tarea": tarea };
        self._zereginak.append(berria)

    def gorde (self):
        fitxategia = open("tareas.json", "w")
        fitxategia.write(json.dumps(self._zereginak))
        fitxategia.close()

    def ezabatu(self, id):
        self._zereginak = list(filter(lambda dato: dato["id"] != id, self._zereginak))

    def erakutsi (self):
        emaitza = ""
        for dato in self._zereginak:
            emaitza += json.dumps(dato) + "\n"

        return emaitza