   @page Section1 { size:432.05pt 432.05pt; margin:28.35pt 42.55pt 36pt } div.Section1 { page:Section1 }

7.4  Ejercicios propuestos
--------------------------

### 7.4.1    Ejercicio 0.0

Escribe un programa que solicite un número al usuario y le multiplique 7. A continuación debe mostrar el resultado por la consola.

```Python
valor = input("Introduce un número: ")
resultado = int(valor) * 7

print("La multiplicación es:", resultado)
```

Resultado:

```console
Introduce un número: 3
La multiplicación es: 21
```

### 7.4.2    Ejercicio 0.1

Escribe un programa que solicite un número al usuario y lo divida por 2. A continuación debe mostrar el resultado por la consola.

```Python
valor = input("Introduce un número: ")
resultado = int(valor) / 2

print("La división es:", resultado)
```

Resultado:

```console
Introduce un número: 60
La división es: 30
```

### 7.4.3    Ejercicio 0.2

Escribe un programa que solicite un número al usuario y haga módulo 3. A continuación debe mostrar el resultado por la consola.

```Python
valor = input("Introduce un número: ")
resultado = int(valor) % 3

print("El módulo es:", resultado)
```

Resultado:

```console
Introduce un número: 7
El módulo es: 1
```

### 7.4.4    Ejercicio 0.3

Escribe un programa que solicite un número al usuario y le aplique un exponencial de 2. A continuación debe mostrar el resultado por la consola.

```Python
valor = input("Introduce un número: ")
resultado = int(valor) ** 2

print("El exponencial es:", resultado)
```

Resultado:

```console
Introduce un número: 4
El exponencial es: 16
```

### 7.4.5    Ejercicio 0.4

Escribe un programa que solicite un número al usuario y le reste 5. A continuación debe cambiarle el signo y mostrar el resultado por la consola.

```Python
valor = input("Introduce un número: ")
resta = int(valor) - 5
resultado = -resta

print("La resta final es:", resultado)
```

Resultado:

```console
Introduce un número: 4
La resta final es: 1
```

### 7.4.6    Ejercicio 0.5

Escribe un programa que solicite un número al usuario. Después debe comprobar si la operación % 2 es igual a 0 y mostrar el resultado. Si se divide un número por 2 y la resta es 0, significa que ese número es par.

```Python
valor = input("Introduce un número: ")
modulo = int(valor) % 2

resultado = modulo == 0

print("¿Valor es par?", resultado)
```

Resultado

```console
Introduce un número: 8
¿Valor es par? True
```

### 7.4.7    Ejercicio 0.6

Escribe un programa que solicite un número al usuario. Después debes comprobar si ese número es mayor o igual que 0, es decir, positivo.

```Python
valor = input("Introduce un número: ")

resultado = int(valor) >= 0

print("¿Es positivo?", resultado)
```

Resultado:

```console
Introduce un número: 6
¿Es positivo? True
```

### 7.4.8    Ejercicio 0.7

Escribe un programa que solicite un número al usuario. Después debe comparar si el primero es menor que 0 y mostrar el resultado por la consola. Estaríamos detectando si el número es negativo.

```Python
valor = input("Introduce un número: ")

resultado = int(valor) < 0

print("¿Es negativo?", resultado)
```

Resultado:

```console
Introduce un número: -3

¿Es negativo? True
```


8       Condiciones
===================

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.014.jpeg)

En algún momento, los programas necesitan hacer una cosa u otra dependiendo de una condición. Por ejemplo, si un usuario introduce un dato incorrecto, el programa se acaba. Si un dato tiene determinado valor, se procesa de una forma y si no, de otra. ¿Cómo se consigue ese comportamiento? Mediante condiciones.

Las condiciones son estructuras de programación que nos permiten que un código se ejecute solo cuando se cumplan unas condiciones.

8.1  if
-------

La estructura más simple para hacer una condición es el if, el cual tiene este aspecto:

```Python
if *condición*:
    *instrucciones*
    *instrucciones*
    *...*
```

Como puedes observar, if comienza con una condición. La condición puede ser cualquier expresión que devuelva un booleano, es decir, será True o False, verdadero o falso. Si es True, las instrucciones dentro del if se ejecutarán, y si no se saltarán. Por ejemplo:

```Python
valor = -2
if valor < 0:
    print("El valor es menor que 0")
print("Fin del programa")
```

Resultaría en:

```console
El valor es menor que 0
Fin del programa
```

En cambio:

```Python
valor = 5
if valor < 0:
    print("El valor es menor que 0")
print("Fin del programa")
```

Resultaría en:

```console
Fin del programa
```

Nota:

También debes observar algo muy importante: las instrucciones dentro del if van detrás de unos espacios o una tabulación. Esa es una peculiaridad del lenguaje de programación Python: en cualquier bloque como una condición, un bucle, una función, su contenido debe ir tabulado. Esa es una forma que facilita la lectura y permite reconocer fácilmente la estructura de un programa para otros programadores. Incluso para ti mismo si es tu propio programa.

### 8.1.1    Ejercicio 1.0

Escribe un programa que solicite un número al usuario y compruebe si es negativo. So es negativo, debe mostrar un mensaje por consola.

```Python
valor = input("Escribe un número: ")

if int(valor) < 0:
    print("Es negativo")
```

Resultado:

```console
Escribe un número: -5
Es negativo
```

8.2  if else
------------

Con el if podemos crear un bloque que solo se ejecute si se cumple una condición. Pero ¿Qué pasa si queremos que el programa haga una cosa u otra según una condición? Para poder meter "la otra" opción, utilizamos una estructura if-else:

```Python
if *condición*:
    *instrucciones*
else:
    *instrucciones*
```

Por ejemplo:

```Python
nombre = input("Dime tu nombre: ")
if nombre != "":
    print("Hola ", nombre)
else:
    print("¡No has metido nada!")
```

Podría verse algo así, según lo que meta el usuario:

```console
Dime tu nombre: Ada
Hola Ada
```

Pero si el usuario simplemente pulsa enter sin escribir nada:

```console
Dime tu nombre:
¡No has metido nada!
```