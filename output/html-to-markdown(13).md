### 9.2.2    Ejercicio 2.3

Escribe un programa que pida un número al usuario. Si es igual o menor a 0 debe indicar que meta algo mayor, y si no, debe mostrar el mensaje "Python mola!" por pantalla tantas veces como indique el número:

```Python
numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0:
    print("Debes introducir un número mayor que 0")
else:
    for i in range(0, numero):
        print("Python mola!")
```

Resultado:

```console
Introduce un número: 3
Python mola!
Python mola!
Python mola!
```

### 9.2.3    Cambiar el rango

Por defecto, range(4) está devolviendo una lista de 0 a 3, es decir: 0, 1, 2, 3. Son un total de cuatro elementos y por tanto el bucle dará cuatro vueltas.

Obviamente, se puede crear cualquier tipo de rango. Si no se indica nada, el rango comienza en 0. Pero se puede indicar un rango entre dos números:

```Python
range(0, 4) # 0, 1, 2, 3
range(2, 6) # 2, 3, 4, 5
```

Por ejemplo:

```Python
for i in range(5, 9):
    print("Hola", i)
```

El resultado sería:

```console
Hola 5
Hola 6
Hola 7
Hola 8
```

También se puede indicar un tercer parámetro para indicar cómo se salta de un valor a otro. Por ejemplo de 2 en 2:

```Python
range(1, 11, 2) \# 1, 3, 5, 7, 9
```

En el siguiente ejemplo, el bucle se haría con números pares.

```Python
for i in range(0, 6, 2):
    print("Hola", i)
```

El resultado sería:

```console
Hola 0
Hola 2
Hola 4
```

### 9.2.4    Hacia atrás

También se podría recorrer el bucle hacia atrás, utilizando un salto negativo:

```Python
print("Iniciando cuenta atrás: ")
for i in range(5, 0, -1):
    print(i)
```

El resultado sería:

```console
5
4
3
2
1
```

### 9.2.5    Ejercicio 2.4

Escribe un programa que pida un número al usuario. Luego debe mostrar todos los números pares desde 0 hasta el número que haya metido el usuario. Utiliza un bucle for y salta de dos en dos.

```Python
valor = input("Introduce un número: ")
valor = int(valor)

for i in range(0, valor, 2):
    print(i)
```

Resultado:

```console
Introduce un número: 5
0
2
4
```

### 9.2.6    Bucles sobre listas

Los bucles for son especialmente útiles cuando queremos recorrer todos los elementos de una lista, para mostrarlos, procesarlos o lo que sea. La forma es muy sencilla:

```Python
objetos = ["estrella", "seta", "flor"]
for objeto in objetos:
    print(objetos)
```

En cada vuelta del bucle la variable objeto tomara un valor de la lista objetos, así que el resultado sería el siguiente:

```console
estrella
seta
flor
```

### 9.2.7    Saliendo del bucle

En ocasiones puede que nos interese salir de un bucle y no seguir procesando nada más. Supongamos que tenemos un programa para buscar un nombre dentro de una lista:

```Python
nombres = ["Mia", "Jon", "Arya", "Ane", "Bug", "Ada", "Lisp"]
for nombre in nombres:
    if nombre == "Ane":
        print("Ane está en la lista")
```

El problema de ese programa es que aunque encuentre a Ane, el bucle seguirá hasta el final de la lista. Si esa lista es muy grande, ¡nuestro programa será ineficiente! Como decíamos al principio, los ordenadores son muy tontos. Si no les decimos que paren, seguirán adelante.

Por suerte, en los bucles podemos usar la instrucción break, la cual conseguirá que el bucle termine de golpe:

```Python
nombres = ["Mia", "Jon", "Arya", "Ane", "Bug", "Ada", "Lisp"]
for nombre in nombres:
    if nombre == "Ane":
        print("Ane está en la lista")
        break
```

### 9.2.8    Ejercicio 2.5

Escribe un programa que defina una lista con 3 números. Luego crea un bucle for que recorra la lista y repita la palabra Python tantas veces como indique el número.

```Python
repetir = [3, 6, 2]

for veces in repetir:
    for i in range(veces):
        print("Python")
```

Resultado:

```console
Python
Python
Python
Python
...
```

9.3  ¿Cuándo usar while o for?
------------------------------

Aunque con los dos podrías hacer lo mismo, realmente cada uno tiene un uso más lógico.

El bucle for se utiliza claramente cuando se quiere ejecutar algo un número concreto de veces, ni más ni menos. O bien, como veremos más adelante, cuando se quieren recorrer estructuras de datos como listas de principio a fin.

El bucle while se puede utilizar cuando las condiciones no son muy concretas. Por ejemplo, si queremos que el usuario introduzca un dato, lo podemos hacer en un bucle. El bucle no terminará hasta que el usuario no introduzca un dato bueno (esa sería la condición).