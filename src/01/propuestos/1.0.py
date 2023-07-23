balio1 = input("Sartu zenbaki bat: ")
balio2 = input("Sartu beste zenbaki bat: ")

resto = int(balio1) % int(balio2)

if resto == 0:
  print(balio1, " zenbakia ", balio2, " zenbakiaren bikoitza da.")
else:
  print(balio1, " zenbakia ", balio2, " zenbakirik ez da bikoitza.")