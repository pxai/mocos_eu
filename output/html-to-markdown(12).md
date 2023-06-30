   @page Section1 { size:432.05pt 432.05pt; margin:28.35pt 42.55pt 36pt } div.Section1 { page:Section1 }

### 9.2.1    Ejercicio 2.2

Escribe un programa que solicite un número al usuario y muestre su tabla de multiplicar del 0 al 10.

```Python
valor = input("Introduce un número: ")
valor = int(valor)

for i in range(11):
    print(valor,"x",i,"=",(valor*i))
    # Alternativas:
    # print("%d x %d = %d" % (valor, i, valor * i))
```

Resultado:

```console
Introduce un número: 3
0 x 3 = 0
1 x 3 = 3
2 x 3 = 6
...
```