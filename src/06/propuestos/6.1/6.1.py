listado-eko = importatu
nire_listadoa = listado.Listado("4.json")

badaude = nire_listadoa.existe("eugene")
if badaude:
    print("Dago!")

nire_listadoa.aMinusculas()
nire_listadoa.print()

badaude = nire_listadoa.existe("eugene")
if badaude:
    posizioa = nire_listadoa.posicion('eugene')
    print("Dago!")
    print(posizioa)