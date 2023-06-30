menua sarrera
nire_menua = menua.Menu(["Erakutsi", "Kendu", "Irten"])

nire_menua.erakutsi()

if nire_menua.aukeratu(1):
    print("1. aukera une honetan dago")
else:
    print("1. aukera ez dago une honetan")