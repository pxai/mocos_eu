dorsal = input("Sartu dorsoa: ")
dorsal = int(dorsal)

if dorsal >= 0 and dorsal <= 99:
  if dorsal == 1:
      print("Atari gizona")
  elif dorsal >= 1 and dorsal <= 5:
      print("Defentsa jokalaria")
  elif dorsal >= 6 and dorsal <= 8 or dorsal == 11:
      print("Erdilari jokalaria")
  elif dorsal == 9:
      print("Atalari jokalaria")
  else:
      print("Norbera")
else:
    print("Errorea, dorsoa 0 eta 99 artean ez dago")