zenbakia = input("Sartu zenbaki bat: ")
zenbakia = int(zenbakia)

if zenbakia <= 0:
    print("0 baino handiagoa den zenbakia sartu behar duzu")
else:
    zatigarria = False
    originala = zenbakia
    zenbakia = zenbakia - 1

    while zenbakia > 1 and not zatigarria:
        if originala % zenbakia == 0:
            zatigarria = True

        zenbakia = zenbakia - 1


    if not zatigarria:
        print(originala, " zenbakia lehena da.")
    else:
        print(originala, " lehen ez da.")