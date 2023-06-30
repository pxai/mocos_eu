zenbakia = input("Sartu zenbaki bat: ")
zenbakia = int(zenbakia)

if zenbakia <= 0:
    print("0 baino handiagoa den zenbaki bat sartu behar duzu")
else:
    izarak = "\n"
    for i in range(zenbakia):
        for j in range(zenbakia):
            izarak = izarak + "*"
            
        izarak = izarak + "\n"

    print(izarak)