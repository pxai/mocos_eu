zenbakia = input("Sartu zenbaki bat: ")
zenbakia = int(zenbakia)

if zenbakia <= 0 or zenbakia % 2 != 0:
    print("0 baino handiagoa den zenbaki bikoitza sartu behar duzu")
else:
    izarak = ""
    while zenbakia > 0:
        izarak = izarak + "*"
        zenbakia = zenbakia - 1

    print(izarak)