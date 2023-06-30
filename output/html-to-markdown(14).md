9.4  Ejercicios propuestos
--------------------------

### 9.4.1    Ejercicio 2.0

Escribe un programa con un bucle while que solicite un nombre al usuario por ejemplo "Ada" y muestre un saludo a ese nombre "Hola Ada". Si se introduce el texto "salir" el bucle debe terminar.

```Python
nombre = ""

while nombre != "salir":
    nombre = input("Introduce un nombre: ")
    print("Hola", nombre)

print("Final.")
```

Resultado:

```console
Introduce un nombre: Ada
Hola Ada
Introduce un nombre: Neko
Hola Neko
Introduce un nombre: salir
Final.
```

### 9.4.2    Ejercicio 2.1

Escribe un programa que contenga un bucle while que solicite al usuario un número y que no termine mientras el número sea diferente de 0. Una vez introducido el número debe mostrarse un saludo tantas veces como indique el número. Si el número es menor que 0 debe terminarse el bucle con un break;

```Python
valor = ""

while valor != 0:
    valor = input("Introduce un numero: ")
    valor = int(valor)
    if valor < 0:
        break

    for i in range(valor):
        print("Hola")
```

Resultado:

```console
Introduce un numero: 3
Hola
Hola
Hola
Introduce un numero: -1
```

### 9.4.3    Ejercicio 2.2

Crea un programa que solicite al usuario un valor entero, comprueba si es mayor que 0 y además par y si es así muestre por pantalla una línea con el carácter * (asterisco) tantas veces como el valor del número. Usa print("*"). Por ejemplo si introduce 8 mostrará:

```console
********
```

Si el valor introducido no cumple los requisitos debes mostrar un mensaje de advertencia al usuario y terminar el programa.

```Python
numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0 or numero % 2 != 0:
    print("Debes introducir un número par mayor que 0")
else:
    estrellas = ""
    while numero > 0:
        estrellas  = estrellas + "*"
        numero = numero - 1

    print(estrellas)
```

Resultado:

```console
Introduce un número: 6
******
```

### 9.4.4    Ejercicio 2.3

Crea un proyecto parecido al anterior, que solo debe admitir pares positivos, pero la línea que debes mostrar debe tener este aspecto:

```console
2:*-*
```

```console
6: *-*-*-*
```

Y siempre debe terminar en *

Por ejemplo, si introducen el 4: *-*-*

```Python
numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0 or numero % 2 != 0:
    print("Debes introducir un número par mayor que 0")
else:
    secuencia = ""
    numero = numero / 2
    while numero > 0:
        secuencia  = secuencia + "*-"
        numero = numero - 1

    secuencia = secuencia + "*"

    print(secuencia)
```

Resultado:

```console
Introduce un número: 8
*-*-*-*-*
```

### 9.4.5    Ejercicio 2.4

Crea un programa que solicite al usuario un número entero y usando ese valor debe "dibujar" en la consola un cuadrado formado por *. Por ejemplo si introduce 4 se mostrará:

```console
****
****
****
****
```

```Python
numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0:
    print("Debes introducir un número mayor que 0")
else:
    estrellas = "n"
    for i in range(numero):
        for j in range(numero):
            estrellas = estrellas + "*"
           
        estrellas = estrellas + "n"

    print(estrellas)
```

Resultado:

```console
Introduce un número: 2
**
**
```

### 9.4.6    Ejercicio 2.5

Crea un programa que solicite al usuario un número entero y calcule su factorial. Por ejemplo el factorial de 5 sería 5 x 4 x 3 x 2 x 1 = 120

```Python
numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0:
    print("Debes introducir un número mayor que 0")
else:
    factorial = numero
    while numero > 1:
        numero = numero - 1
        factorial = factorial * numero

    print("Resultado: ", factorial)
```

Resultado:

```console
Introduce un número: 4
Resultado: 24
```

### 9.4.7    Ejercicio 2.6

Crea un programa que solicite al usuario un número entero y comprueba si ese número es primo o no, es decir si solamente es divisible por sí mismo o por 1.

```Python
numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0:
    print("Debes introducir un número mayor que 0")
else:
    divisible = False
    original = numero
    numero = numero - 1

    while numero > 1 and not divisible:
        if original % numero == 0:
            divisible = True

        numero = numero - 1


    if not divisible:
        print(original, " es primo.")
    else:
        print(original, " NO es primo.")
```

Resultado:

```console
Introduce un número: 5
5 es primo.
```

### 9.4.8    Ejercicio 2.7

Crea un programa que muestre todas las tablas de multiplicar desde el número 0 al 10.

```Python
for i in range(11):
    for j in range(11):
      print(i,"x",j,"=",i*j)

# Lo mismo, de otro modo
for i in range(11):
    for j in range(11):
      print(" %d x %d = %d" % (i, j, i*j))
```

10         Estructuras de datos
===============================

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.016.jpeg)

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.016.jpeg)

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.016.jpeg)

Hasta ahora hemos estado jugando con datos simples, variables que contienen un número, un texto, etc. Pero existen otros tipos que nos permiten crear datos más complejos. No es que sean difíciles, simplemente pueden contener algo más que un simple número.

Los programas de ordenador pueden hacer cosas muy complicadas, pero en esencia, todo lo que hacen es procesar datos. Y muchas veces, esos datos viene en secuencias largas. A continuación vamos a ver algunos de esos tipos de datos.

10.1 Listas
-----------

Las listas son un conjunto de datos indexados numéricamente. Esa es la definición muy formal, pero su propio nombre ya te dice lo que son: ¡una lista! En el capítulo sobre tipos de datos ya presentamos las listas y vimos cómo se crean:

```Python
idiomas = ["Inglés", "Español", "Francés"]
```

Recuerda que puedes acceder a los elementos a través de un índice o posición:

```Python
idiomas = ["Inglés", "Español", "Francés"]
print(idiomas[2]) # Francés
```
La lista se puede representar así:

|0|1|2|
|--|--|--|
|`"Inglés"`|`"Español"`|`"Francés"`|
 

### 10.1.1  Ejercicio 3.0

Define una lista de nombres y muéstralas por pantalla:

```Python
nombres = ["Ada", "Bug", "Neko"]

print(nombres) # ["Ada", "Bug", "Neko"]
```

Resultado:

```console
["Ada", "Bug", "Neko"]
```

### 10.1.2                       Ejercicio 3.1

Crea un programa que defina una de 5 números con decimales. Luego crea un bucle que calcule la media de todos los números.

```Python
numeros = [3.4, 2.7, 4.3, 6.6, 8.3]
suma = 0.0

for numero in numeros:
    suma = suma + numero

media = suma / len(numeros)

print("La media es: ", media)
```

Resultado:

```Python
La media es:  5.0600000000000005
```

10.2 Extraer partes de la lista
-------------------------------

Usando el índice numérico, se pueden sacar partes de una lista, creando una sub-lista de la misma. Por ejemplo "quiero los tres primeros valores de la lista" o "quiero desde el 4º al 6º" o "quiero los dos últimos". Para eso basta con indicar un rango de índices:

```Python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros[0:4]  # [1, 2, 3, 4]
numeros[5:8]  # [6, 7, 8]
```

También se pueden sacar los primeros elementos:

```Python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros[:6] # [1, 2, 3, 4, 5, 6]
```

O los últimos valores

```Python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros[-4:] # [6, 7, 8, 9]
```

O simplemente el último de todos:

```Python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros[-1] # [9]
```

10.3 Añadir y eliminar elementos
--------------------------------

Si queremos añadir un elemento a una lista, basta con utilizar la función append:

```Python
idiomas = ["Inglés", "Español", "Francés"]
idiomas.append("Italiano")
print(idiomas) # ["Inglés", "Español", "Francés", "Italiano"]
```

Y si queremos eliminar un elemento de la lista, se puede usar la orden del:

```Python
idiomas = ["Inglés", "Español", "Francés"]
del idiomas[1]
print(idiomas) # ["Inglés", "Francés"]
```

Y también se puede cambiar el valor de un elemento de la lista:

```Python
idiomas = ["Inglés", "Español", "Francés"]
idiomas[2] = "Italiano"
```

Y recuerda, para recorrer la lista, podemos usar un bucle for:

```Python
idiomas = ["Inglés", "Español", "Francés"]
for idioma in idiomas:
    print(idioma)
```

También se puede recorrer la lista utilizando el índice. Para eso tendremos que utilizar la función range, pasándole la longitud de la lista con len:

```Python
idiomas = ["Inglés", "Español", "Francés"]
for i in range(len(idiomas)):
    print(idiomas[i])
```

De todas formas, si no se necesita el índice dentro del bucle, es mejor recorrer la lista sin índice tal y como se hace en el ejemplo anterior.

En otros lenguajes, a las listas se les llama "arrays". Ya los deberías conocer, pero te lo volvemos a recordar.

### 10.3.1                       Ejercicio 3.2

Define una lista de nombres, muéstrala por pantalla. Añade un elemento y muestra la lista por pantalla. Luego elimina un elemento de la lista y muestra la lista por pantalla.

```Python
nombres = ["Ada", "Bug", "Neko"]

print(nombres)

nombres.append("Miranda")

print(nombres)

del nombres[1]

print(nombres)
```

Resultado:

```
["Ada", "Bug", "Neko"]
["Ada", "Bug", "Neko", "Miranda"]
["Ada", "Neko", "Miranda"]
```

10.4 Diccionarios
-----------------

Los diccionarios son conjuntos de datos donde cada elemento tiene una clave y un valor. Dichos de otra manera, son como una lista, pero en lugar de tener un índice numérico como 0, 1, 2,... tienen el valor que tú quieras.

Por ejemplo, podemos definir un diccionario que contenga las edades de varias personas, donde el nombre de la persona es la clave y la edad el valor:

```Python
edades = { "Ada": 14, "Bug": 10, "Neko": 2 }
print(edades["Ada"])  #  14
```

El diccionario se puede representar así:

|`"Ada"`|`"Bug"`|`"Neko"`|
|--|--|--|
|`14`|`10`|`2`|
