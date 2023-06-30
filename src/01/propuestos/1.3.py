zenbaki = input("Sartu zenbaki bat: ")
zenbaki = int(zenbaki)

if zenbaki >= 0 and zenbaki % 2 == 0:
    print(zenbaki, " parra eta positiboa da")
elif zenbaki < 0 and zenbaki % 2 != 0:
    print(zenbaki, " bakoitza eta negatiboa da")
elif zenbaki < 0:
    print(zenbaki, " negatiboa da")
else:
    print(zenbaki, " bakoitza da")