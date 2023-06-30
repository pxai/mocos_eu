def batu(*hitza):
    esaldia = ""

    for h in hitza:
        esaldia = esaldia + " " + h
    
    return esaldia


print(batu("kaixo", "nola", "naiz"))