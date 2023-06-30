import json

class Tareas:
    def __init__ (self):
        fitxategia = open("tareas.json", "r")
        self._tareas = json.load(fitxategia)
        fitxategia.close()

    def sortu (self, id, tarea):
        berria = { "id": id, "tarea": tarea };
        self._tareas.append(berria)

    def gorde (self):
        fitxategia = open("tareas.json", "w")
        fitxategia.write(json.dumps(self._tareas))
        fitxategia.close()

    def ezabatu(self, id):
        self._tareas = list(filter(lambda dato: dato["id"] != id, self._tareas))

    def erakutsi (self):
        emaitza = ""
        for dato in self._tareas:
            emaitza += json.dumps(dato) + "\n"

        return emaitza