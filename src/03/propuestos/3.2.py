zenbakiak = []
aukera = -1

while aukera != "4":
    print("Aukeratu aukera")
    print("1. Elementua txertatu.")
    print("2. Elementua kendu.")
    print("3. Arraya erakutsi.")
    print("4. Irten.")
    aukera = input("Aukeratu aukera: ")

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