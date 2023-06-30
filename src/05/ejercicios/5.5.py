import random

class Zenbakia:
    @staticmethod
    def aleatorio (max):
      return random.randint(0, max)

for i in range(5):
  print(Zenbakia.aleatorio(10))