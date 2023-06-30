   @page Section1 { size:432.05pt 432.05pt; margin:28.35pt 42.55pt 36pt } div.Section1 { page:Section1 }

### 7.2.1    Ejercicio 0.7

Escribe un programa que solicite dos números al usuario. Después debe comparar su desigualdad y debe mostrar el resultado por la consola.

```Python
valor1 = input("Introduce un número: ")
valor2 = input("Introduce otro número: ")

resultado = valor1 != valor2

print("¿Son distintos?", resultado)
```

Resultado:

```Python
Introduce un número: 42
Introduce otro número: 42
¿Son distintos? False
```

7.3  Operadores booleanos
-------------------------

Los operadores booleanos nos permiten hacer operaciones con valores booleanos Trueo False.

### 7.3.1    and

Este operador solo devuelve True si los dos operandos también son True:

```Python
valor = 5
resultado = (valor == 5) and True;
```

El resultado sería True. Para resumir todas las posibles opciones, esta sería lo que se denomina tabla de la verdad del operador and.

|a||b|Resultado|
|--|--|--|--|
|`False`|`and`|`False`|`False`|
|`False`|`and`|`True`|`False`|
|`True`|`and`|`False`|`False`|
|`True`|`and`|`True`|`True`|

 

### 7.3.2    Ejercicio 0.8

Escribe un programa que solicite un número al usuario. Después debe comparar si el primero es mayor que 0 y además es par.

```Python
valor = input("Introduce un número: ")
valor = int(valor)
resultado = (valor >= 0) and (valor % 2 == 0)

print("¿Es par y positivo?", resultado)
```

Resultado:

```Python
Introduce un número: 14
¿Es par y positivo? True
```

### 7.3.3    or

Este operador devuelve True si cualquiera de los dos operandos también son True:

```Python
valor = 5
resultado = (valor == 5) or True;
```

El resultado sería True. Para resumir todas las posibles opciones, esta sería la tabla de la verdad del operador or:

|a||b|Resultado|
|--|--|--|--|
|`False`|`or`|`False`|`False`|
|`False`|`or`|`True`|`True`|
|`True`|`or`|`False`|`True`|
|`True`|`or`|`True`|`True`|


### 7.3.4    Ejercicio 0.9

Escribe un programa que solicite dos números al usuario y compruebe si alguno de los dos es positivo. A continuación debe mostrar el resultado por la consola.

```Python
valor1 = input("Introduce un número: ")
valor2 = input("Introduce otro número: ")

resultado = (int(valor1) >= 0) or (int(valor2) >= 0)

print("¿Es alguno de los dos positivo?", resultado)
```

Resultado:

```Python
Introduce un número: -4
Introduce otro número: 6
¿Es alguno de los dos positivo? True
```

### 7.3.5    not

Este operador devuelve el valor contrario al operando. Si se aplica a True devuelve False y si se aplica a False devuelve True:

```console
valor = True
resultado = not valor;
```

El resultado sería False. Para resumir todas las posibles opciones, esta sería la tabla de la verdad del operador not.


||a|Resultado|
|--|--|--|
|`not`|`False`|`False`|
|`not`|`True`|`False`|
