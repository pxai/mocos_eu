   @page Section1 { size:432.05pt 432.05pt; margin:28.35pt 42.55pt 36pt } div.Section1 { page:Section1 }

### 8.3.2    Ejercicio 1.3

Crea un programa que solicite al usuario dos valores enteros, los compare y muestre por pantalla si uno es mayor que el otro o si son iguales.

```Python
numero1 = input("Introduce un número: ")
numero2 = input("Introduce otro número: ")

if numero1 > numero2:
  print(numero1, " es mayor que ", numero2)
elif numero1 < numero2:
  print(numero1, " es menor que ", numero2)
else:
  print(numero1, " es igual que ", numero2)
```

Resultado:

```console
Introduce un número: 5
Introduce otro número: 10
5 es menor que 10
```