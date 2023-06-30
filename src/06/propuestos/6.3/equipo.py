import json
import jugador

class Equipo:
    def cargar(self):
        contenido = open("./jugadores.json")
        jugadores = json.load(contenido)
        print("Kargatuta:", jugadores)
        self._jugadores = []
        for j in jugadores:
            self._jugadores.append(jugador.Jokalaria(j["izena"], j["dorsala"]))

    def fichaje(self, izena, dorsala):
        fitxategiBerria = jugador.Jokalaria(izena, dorsala)
        self._jugadores.append(fitxategiBerria)

    def mostrar(self):
        for jokalaria in self._jugadores:
            print(jokalaria.toString())