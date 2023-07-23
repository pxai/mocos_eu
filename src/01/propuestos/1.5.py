zenbakia = input("Sartu zenbakia: ")
zenbakia = int(zenbakia)

if zenbakia >= 0 and zenbakia <= 99:
  if zenbakia == 1:
      print("Atari gizona")
  elif zenbakia >= 1 and zenbakia <= 5:
      print("Defentsa jokalaria")
  elif zenbakia >= 6 and zenbakia <= 8 or zenbakia == 11:
      print("Erdilari jokalaria")
  elif zenbakia == 9:
      print("Aurrelari jokalaria")
  else:
      print("Norbera")
else:
    print("Errorea, zenbakia ez dago 0 eta 99 artean")