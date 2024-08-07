class Fitxategia:
  def __init__(self, nombreFichero):
      self._nombreFichero = nombreFichero

  def irakurri(self):
      fitxategia = open(self._nombreFichero, "r")
      datuak = fitxategia.read()
      fitxategia.close()

      return datuak

  def idatzi(self, eduki):
      fitxategia = open(self._nombreFichero, "w+")
      fitxategia.write(eduki)
      fitxategia.close()