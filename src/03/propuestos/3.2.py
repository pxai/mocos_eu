zenbakiak = []
aukera = -1

while aukera != "4":
    print("Aukeratu")
    print("1. Elementua sartu.")
    print("2. Elementua kendu.")
    print("3. Arraia erakutsi.")
    print("4. Irten.")
    aukera = input("Sartu aukera: ")

    if "1":
        zenbakiak.append(0)
    elif "2":
        zenbakiak.pop()
    elif "3":
        print(zenbakiak)
    elif "4":
        print("Agurra")
    else:
        print("Aukera ezezaguna")