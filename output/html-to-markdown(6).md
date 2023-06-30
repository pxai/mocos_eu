   @page Section1 { size:432.05pt 432.05pt; margin:28.35pt 42.55pt 36pt } div.Section1 { page:Section1 }

### 7.3.6    Ejercicio 0.10

Escribe un programa que solicite un número al usuario y compruebe que no es ni positivo ni par.

```Python
valor = input("Introduce un número: ")
valor = int(valor)

positivoYPar = (valor >= 0) and (valor % 2 == 0)
resultado = not positivoYPar
print("¿No es par y positivo?", resultado)
```

Resultado:

```console
Introduce un número: -4
¿No es par y positivo? True
```

### 7.3.7    Combinando operadores

Podemos combinar los operadores tanto como necesitemos:

```Python
jubilado = 65
if edad > 17 and edad < (jubilado + 1):
    print("Ya puedes trabajar")
```

Generalmente, los operadores condicionales se utilizan dentro de las condiciones de los bloques condicionales, bucles, etc.