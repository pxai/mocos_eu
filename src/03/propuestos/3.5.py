frasea = input("Idatzi esaldi bat: ")
hitza = input("Idatzi esalditik hitz bat: ")

posizioa = frasea.index(hitza)

if posizioa != -1:
    hasiera = frasea[0:posizioa]
    bukaera = frasea[posizioa + len(hitza):len(frasea)]
    emaitza = f"{hasiera}{hitza.upper()}{bukaera}"

    print(emaitza)
else:
    print(hitza, "ez dago esaldian.")