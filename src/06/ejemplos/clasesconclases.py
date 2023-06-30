Klasea Ikaslea izan da:
    def __init__ (self, izena):
        self._izena = izena

class Gelak:
    def __init__ (self):
        self._ikasleak = []
    
    def ikasleaSartu (self, ikaslea):
        self._ikasleak.append(ikaslea)

    def ordutegiaEman (self):
        for ikaslea in self._ikasleak:
            print(ikaslea._izena)

ikasle1 = Ikaslea("Gumball")
ikasle2 = Ikaslea("Darwin")

gela = Gelak()

gela.ikasleaSartu(ikasle1)
gela.ikasleaSartu(ikasle2)
gela.ordutegiaEman()