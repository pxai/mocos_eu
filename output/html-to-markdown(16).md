11.6 Ejercicios propuestos
--------------------------

### 11.6.1                       Ejercicio 3.0

Escribe un programa que inicie una lista de 5 números (iniciados a 0), otro de 5 nombres iniciados a mano y otro de valores 5 booleanos (iniciados a false)

```Python
nombres = ["Frodo", "Sam", "Merrin", "Pippin"]
booleanos = [True]*5
numeros = [0]*5

print(nombres)
print(numeros)
print(booleanos)
```

Resultado:

```console
["Frodo", "Sam", "Merrin", "Pippin"]
[0, 0, 0, 0, 0]
[True, True, True, True, True]
```

### 11.6.2                       Ejercicio 3.1

Escribe un programa que defina una lista de 10 números. Luego debe crear un bucle que en las posiciones pares meta un 0.

```Python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numeros)):
    if i % 2 == 0:
        numeros[i] = 0

print(numeros)
```

Resultado:

```console
[0, 2, 0, 4, 0, 6, 0, 8, 0, 10]
```

### 11.6.3                       Ejercicio 3.2

Escribe un programa para gestionar una lista, que muestre al usuario un menú con 4 opciones: (1) meter elemento, (2) eliminar, (3) mostrar y (4) salir. El menú debe mostrarse mientras el usuario no meta la opción 4. Si elige la opción 1, se hace push de un valor cualquiera, si elige 2 se hace pop, si elige 3 se muestra el contenido dla lista.

```Python
numeros = []
opcion = -1

while opcion != "4":
    print("Elige opción")
    print("1. Meter elemento.")
    print("2. Sacar elemento.")
    print("3. Mostrar lista.")
    print("4. Salir.")
    opcion = input("Elige opción: ")

    if "1":
        numeros.append(0)
    elif "2":
        numeros.pop()
    elif "3":
        print(numeros)
    elif "4":
        print("Hasta otra")
    else:
        print("Opción desconocida")
```

Resultado:

```console
Elige opción
1. Meter elemento.
2. Sacar elemento.
3. Mostrar lista.
4. Salir.
Elige opción: 3
[]
```

### 11.6.4                       Ejercicio 3.3

Escribe un programa que solicite palabras al usuario y las vaya concatenando para construir una frase, hasta que el usuario escriba un punto (.). Entonces el programa deberá mostrar la frase creada. Si el usuario no escribe nada, no se debe concatenar nada.

```Python
frase = ""
palabra = ""

while palabra != ".":
    palabra = input("Escribe una palabra: ")

    if palabra != "." or palabra != "":
        frase = frase + " " + palabra

print("Frase creada:", frase)
```

Resultado:

```console
Escribe una palabra: Hola
Escribe una palabra: qué
Escribe una palabra: tal
Escribe una palabra: .
Hola qué tal
```

### 11.6.5                       Ejercicio 3.4

Escribe un programa que solicite al usuario su nombre, su lugar de nacimiento y su año de nacimiento. Luego debe mostrar una frase con toda esa información utilizando la interpolación o plantillas de cadenas.

```Python
nombre = input("Escribe tu nombre: ")
lugar = input("Escribe tu lugar de nacimiento: ")
fecha = input("Escribe tu año de nacimiento: ")

mensaje = f"Te llamas {nombre} naciste en {lugar} en {fecha}"

print(mensaje)
```

Resultado:

```console
Escribe tu nombre: Ada
Escribe tu lugar de nacimiento: Teverga
Escribe tu año de nacimiento: 2006
Te llamas Ada naciste en Teverga en 2006
```

### 11.6.6                       Ejercicio 3.5

Escribe un programa que solicite al usuario una frase. Luego debe solicitar una palabra de esa frase, y como resultado, el programa devolverá la misma frase con esa palabra en mayúsculas:

```Python
frase = input("Escribe una frase: ")
palabra = input("Escribe una palabra de esa frase: ")

posicion = frase.index(palabra)

if posicion != -1:
    inicio = frase[0:posicion]
    final = frase[posicion + len(palabra):len(frase)]
    resultado = f"{inicio}{palabra.upper()}{final}"

    print(resultado)
else:
    print(palabra, "no está en la frase.")
```

Resultado:

```console
Escribe una frase: Qué buena es la profa Ada
Escribe una palabra de esa frase: buena
Qué BUENA es la profa Ada
```

### 11.6.7                       Ejercicio 3.6

Crea un programa que defina una lista de 5 nombres y luego utilice un bucle para mostrar los nombres de uno en uno.

```Python
nombres = ["Frodo", "Merrin", "Sam", "Pip", "Bilbo"]

for nombre in nombres:
    print(nombre)

# variante:
for i in range(len(nombres)):
    print(nombres[i])
```

Resultado:

```console
Frodo
Merrin
Sam
Pip
Bilbo
```

### 11.6.8                       Ejercicio 3.7

Crea un programa que defina una lista de 10 números enteros. Luego crea otro bucle que calcule que incremente en uno cada uno de los elementos y los muestre.

```Python
numeros = [3, 5, -4, 2, 1, 4, 0, 6, 9, 8, 3]

for i in range(len(numeros)):
    numeros[i] = numeros[i] + 1

print(numeros)

# Alternativa para la suma:
# numerosIncrementados = numeros.map( numero => numero + 1 )
```

Resultado:

```console
[4, 6, -3, 3, 2, 5, 1, 7, 10, 9, 4]
```

### 11.6.9                       Ejercicio 3.8

Crea un programa que defina una lista de 10 números enteros Luego crea un bucle que determine si en la lista hay algún elemento repetido. Con que encuentre uno repetido es suficiente.

```Python
numeros = [3, 5, -4, 2, 1, 4, 0, 6, 9, 8, 3]
repetido = False
i = 0
j = 0

while i < len(numeros) and not repetido:
    while j < len(numeros):
        if numeros[i] == numeros[j]:
            repetido = True
            break
        j = j + 1
    i = i + 1

if repetido:
    print("Hay un número repetido")
else:
    print("No hay un número repetido")
```

Resultado:

```console
Hay un número repetido
```

### 11.6.10                  Ejercicio 3.9

Crea un programa que defina una lista iniciado con 10 números enteros. Luego crea otro bucle que contabilice el total de números positivos, negativos y los que sean 0.

```Python
numeros = [3, 5, -4, 2, 1, 4, 0, 6, -9, 8, 3]

positivos = 0
negativos = 0
ceros = 0

for numero in numeros:
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    else:
        ceros = ceros + 1

print("Positivos: ", positivos)
print("Negativos: ", negativos)
print("Ceros: ", ceros)
```

Resultado:

```console
Positivos:  8
Negativos:  2
Ceros:  1
```

### 11.6.11                  Ejercicio 3.10

Crea un programa que defina una lista de dos dimensiones de 5x10 elementos. Crea un bucle que inicie los valores de la lista usando números aleatorios. Para crear números aleatorios importa la librería random y utiliza la función random.randint(), tal y como se muestra aquí:


```Python
import random
random.randint(0, 30); # número aleatorio entre 0 y 30
```

Después de eso crea otro bucle que si encuentra el número 15 en algún elemento interrumpa el bucle y muestre la posición en la que está.

```Python
import random

matriz = [([0] * 10)] * 5

print(matriz)

for i in range(len(matriz)):
    random.seed()
    for j in range(len(matriz[i])):
        matriz[i][j] = random.randint(0, 30)

print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 15:
            print("Encontrado 15 en ", i, )
```

### 11.6.12                  Ejercicio 3.11

Crea un programa que defina una lista iniciado con 10 números enteros. En un bucle muestra por pantalla todos los elementos. Luego crea otro bucle que baraje los elementos usando el método random del ejercicio anterior en los índices. Luego muestra el resultado.

```Python
import random

numeros = [4, 7, -3, 7, 1, 11, 9, 0, 5, 8]

print(numeros)

for i in range(len(numeros)):
    indiceAleatorio = random.randint(0, len(numeros) - 1)
    anterior = numeros[i]
    numeros[i] = numeros[indiceAleatorio]
    numeros[indiceAleatorio] = anterior

print(numeros)
```

Resultado:

```console
[5, 4, 11, 7, 1, -3, 0, 9, 7, 8]
```

12         Funciones
====================


|miau()|dormir()|
|--|--|
|![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.017.jpeg)|![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.018.jpeg)|

Las funciones son pequeños programas dentro de los programas. Esta sería una función que simplemente saca un saludo por pantalla:

```Python
def saludo ():
    print "Hola"
```

Como se puede ver, una función se define utilizando la palabra def seguida del nombre de la función, en este caso saludo y la lista de parámetros (), la cual está vacía en este caso. En el cuerpo de la función, podemos poner las instrucciones que queramos.

Y siguiendo con el estilo de Python, observa que el código que va dentro de la función va precedido de una tabulación o espacios.

Una vez definida esa función, cada vez que la utilicemos se ejecutará el código que hay en ella:

```Python
saludo()
```

Lo cual mostrará:

```console
Hola
```

### 12.1.1                       Ejercicio 4.0

Escribe un programa con tres funciones llamadas días, tardes y noches. Cada una debe mostrar un saludo distinto, "Buenos días", "Buenas tardes" y "Buenas noches" respectivamente. Añade las llamadas de a las tres funciones.

```Python
def dias ():
    print("Buenos días")

def tardes ():
    print("Buenos tardes")

def noches ():
    print("Buenos noches")

dias()
tardes()
noches()
```

Resultado:

```console
Buenos días
Buenos tardes
Buenos noches
```

12.2 Parámetros
---------------

Las funciones pueden recibir parámetros. Estos se convierten en variables dentro de la función y nos permiten que la función haga cosas diferentes según lo que les pasemos.

Por ejemplo, podemos crear una función que salude a alguien:

```Python
def saluda(persona):
    print("Hola", persona)
```

Dentro de la función, el valor de persona será distinto según lo que se le pase en la llamada Se podría usar así:

```Python
saluda("Neko")  # persona será "Neko"
saluda("Ada")   # persona será "Ada"
```

Lo que resultaría en:

```console
Hola Neko
Hola Ada
```

### 12.2.1                       Ejercicio 4.1

Escribe un programa con una función llamada cuadrado que tenga un parámetro a. La función debe multiplicar a * a y mostrar el resultado por pantalla.

```Python
def cuadrado (a):
    print(a * a)


cuadrado(3)
```

Resultado:

```console
9
```

### 12.2.2                       Parámetro con valor por defecto

Los parámetros de una función pueden tener un valor por defecto. Es decir, se les puede asignar un valor concreto y si no se pasa ese parámetro en la llamada, el parámetro tomará ese valor por defecto.

```Python
def saluda(persona, veces = 3):
    for i in range(veces):
        print("Hola", persona)
```

Si se le llama con:

```Python
saluda("Neko", 2)
```

Se vería:

```console
Hola Neko
Hola Neko
```

En cambio, si no pasamos el segundo parámetro, vecestomará el valor por defecto 3:

```Python
saluda("Bug")
```

Sería:

```console
Hola Bug
Hola Bug
Hola Bug
```


### 12.2.3                       Parámetros infinitos

Las funciones en Python permiten que les pases un número indeterminado de parámetros. Suena un poco raro, pero resulta útil. Imagina que quieres crear una función que sume los todos parámetros que le pases.

```Python
def sumar(*valores):
    resultado = 0

    for valor in valores:
        resultado = resultado + valor
   
    return resultado
```

Si te fijas, hemos definido el parámetro valores con un * por delante. Con eso le estamos indicando que no se trata de un único parámetro, sino una lista que puede tener cualquier longitud.

Por tanto, a esa función la podemos llamar así:

```Python
sumar(3, 4, 5) # 12
sumar(2, 45)   # 47
```


### 12.2.4                       Ejercicio 4.2

Escribe un programa con una función llamada unir que reciba parámetros indefinidos o dinámicos. La función unir debe tomar los parámetros y retornar un texto con todos ellos formando una frase.

```Python
def unir(*palabras):
    frase = ""

    for palabra in palabras:
        frase = frase + " " + palabra
   
    return frase


print(unir("Hola", "qué", "tal"))
```

Resultado:

```console
Hola qué tal
```


12.3 Retorno
------------

Las funciones pueden hacer todas las operaciones que sean necesarias, pero son más útiles cuando devuelven un resultado.

Para eso se utiliza la instrucción return, la cual solo puede devolver un dato concreto o una estructura de datos.

Por ejemplo, una función que calcule la suma de dos valores:

```Python
def suma(a, b):
    resultado = a + b
    return resultado
```


Se puede abreviar un poco haciendo directamente:

```Python
def suma(a, b):
    return a + b
```

Se podría usar la función así:

```Python
print(suma(40, 2))  # 42
```

Debes tener en cuenta un par de cosas con el return:

1-    Una vez se hace return, el programa sale de la función.

2-    Puedes tener más de un return en la función, pero solo se ejecutará uno de ellos.