peso = input("Sartu zure pisua: ")
altuera = input("Sartu zure altuera: ")
peso = int(peso)
altuera = int(altuera)

imc = peso / (altuera * altuera)

imcRedondeado = (imc * 10000)
print("Zure IMC: ", imcRedondeado)

if imcRedondeado < 16 :
  print("Beharrezkoa da gehiago jan")
elif imcRedondeado >= 16 and imcRedondeado < 25:
  print("Ongi zaude")
elif imcRedondeado >= 25 and imcRedondeado < 30:
  print("Gorputz gordinagoa duzu")
else:
  print("Obesitate arazoa daukazu")