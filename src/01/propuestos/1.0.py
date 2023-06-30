numero1 = input("Sartu zenbaki bat: ")
numero2 = input("Sartu beste zenbaki bat: ")

resto = int(numero1) % int(numero2)

if resto == 0:
  print(numero1, " zenbakia ", numero2, " zenbakiaren bikoitza da.")
else:
  print(numero1, " zenbakia ", numero2, " zenbakirik ez da bikoitza.")