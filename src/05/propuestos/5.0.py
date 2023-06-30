Gaiolari:
    def __init__(self, izena, mota):
        self._izena = izena
        self._mota = mota

    def jotzea (self):
        print("Jotzen ", self._izena)

    def info (self):
        return f"${self._izena} ${self._mota}"


nireGitarra = Gaiolari("Gitarra", "ordaina")
nireGitarra.jotzea()
print(nireGitarra.info())