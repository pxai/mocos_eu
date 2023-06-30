class Janari:
    def __init__(hau, izena, pisua):
        hau._izena = izena
        hau._pisua = pisua

    @property
    def izena (hau):
        return hau._izena

    @izena.setter
    def izena (hau, izena):
        hau._izena = izena

    @property
    def pisua (hau):
        return hau._pisua

    @pisua.setter
    def pisua (hau, pisua):
        hau._pisua = pisua

    def toString (hau):
        return f"{hau._izena} {hau._pisua}"


class Fruta(Janari):
    def __init__(hau, izena, pisua, bitamina):
        super().__init__(izena, pisua)
        hau._bitamina = bitamina

    @property
    def bitamina (hau):
        return hau._bitamina

    @bitamina.setter
    def bitamina (hau, bitamina):
        hau._bitamina = bitamina

    def toString (hau):
        return f'{super().toString()} {hau._bitamina}'


class Karamelo(Janari):
    def __init__(hau, izena, pisua, kaloria):
        super().__init__(izena, pisua)
        hau._kaloria = kaloria

    @property
    def kaloria (hau):
        return hau._kaloria

    @kaloria.setter
    def kaloria (hau, kaloria):
        hau._kaloria = kaloria

    def toString (hau):
        return f'{super().toString()} {hau._kaloria}'


class Kesta:
    def __init__(hau):
        hau._janariak = []

    def sartuJanari (hau, janari):
        hau._janariak.append(janari)

    def pisuGuztira (hau):
        guztira = 0
        for janaria in hau._janariak:
            guztira += janaria.pisua

        return guztira

    def toString (hau):
        informazioa = ""
        for janaria in hau._janariak:
            informazioa = informazioa + janaria.toString() + "\n"

        return informazioa


txintxa = Karamelo("Cheiw", 0.2, 100)
gominoa = Karamelo("Fresa", 0.3, 210)
udarea = Fruta("Pera", 0.1, "B")
sagarra = Fruta("Manzana", 0.15, "A")

kest1 = Kesta()
kest1.sartuJanari(txintxa)
kest1.sartuJanari(gominoa)
kest1.sartuJanari(udarea)
kest1.sartuJanari(sagarra)

print("Kesta edukia:", kest1.toString())
print("Pisu guztira:", kest1.pisuGuztira())