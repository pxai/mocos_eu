import zerrenda

nire_zerrenda = zerrenda.inprimatu("4.json")

badaude = nire_zerrenda.existitzenDa("eugene")
if badaude:
    print("Dago!")

nire_zerrenda.minuskulatuta()
nire_zerrenda.print()

badaude = nire_zerrenda.existitzenDa("eugene")
if badaude:
    posizioa = nire_zerrenda.posizioa('eugene')
    print("Dago!")
    print(posizioa)