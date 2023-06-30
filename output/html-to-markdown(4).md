### 5.5.1    Ejercicio 0.2

Escribe un programa que defina una variable de cada tipo visto aquí, y los muestre por la consola.

```Python
nombre = "Ada"
edad = 42
peso = 101.54
vivo = True
riquezas = None
amigas = ["Ada", "Ruby", "Miranda"]

print(nombre)
print(edad)
print(peso)
print(vivo)
print(riquezas)
print(amigas)
```

Resultado:

```console
Ada
42
101.54
true
null
["Ada", "Ruby", "Miranda"]
```

6       Leyendo datos
=====================

Para que un programa pueda hacer algo, muchas veces necesita que el usuario introduzca un dato. Por ejemplo, si queremos que un programa nos diga cuántas letras tiene nuestro nombre, o cuánto falta para nuestro cumpleaños, lo primero que tendrá que hacer el programa es pedir un dato.

Los programas básicos como los que estamos viendo de momento, utilizan la consola para ejecutarse. Son esas pantallas negras donde se ponen órdenes escritas ;)

Para poder pedirle al usuario un dato y guardarlo en una variable, se utiliza la función input:

```Python
nombre = input("Dime tu nombre: ")
print("Hola ", nombre)
```

En la pantalla verías lo siguiente:

```console
Dime tu nombre:
```

La función input hace que el mensaje Dime tu nombre: aparezca en pantalla. También hace que el programa se pare a la espera de que el usuario escriba algo. Si el usuario escribe Rosa en la consola, se vería:

```console
Dime tu nombre: Rosa
Hola Rosa
```

### 6.1.1    Ejercicio 0.3

Escribe un programa que solicite un nombre al usuario y lo guarde en una variable. A continuación debe mostrar un saludo por consola.

```Python
nombre = input("Introduce tu nombre: ")
print("Hola, qué tal estás ", nombre)

# Alternativa:
# print("Hola, qué tal estás %s" % nombre)
```

Resultado:

```console
Introduce tu nombre: Juan
Hola, qué tal estás Juan
```

6.2  Cuidado con los datos
--------------------------

Cada vez que uses la función input para que el usuario escriba algo, sea lo que sea se guardará como texto. Aunque se escriba un número:

```Python
valor = input("Dame un número: ")
doble = valor + valor
print(doble)
```

Si el usuario introduce un número como 4 este sería el resultado:

```console
Dame un número: 4
44
```

En lugar de sumar 4 + 4 y mostrar 8, lo que ha hecho es unir 4 y 4, porque en realidad, cuando se ha leído a través de input ese 4 es texto: "4"

Para evitarlo, tenemos que usar otra función para convertir ese dato en número entero: int()

```Python
valor = input("Dame un número: ")
doble = int(valor) + int(valor)
print(doble)
```

O incluso lo podemos convertir antes:

```Python
valor = input("Dame un número: ")
valor = int(valor)
doble = valor + valor
print(doble)
```

O incluso aplicarlo a input:

```Python
valor = int(input("Dame un número: "))
doble = valor + valor
print(doble)
```

Ahora sí, la suma será numérica:

```console
Dame un número: 4
8
```

### 6.2.1    Ejercicio 0.4

Escribe un programa que solicite un número al usuario y le sume 10. A continuación debe mostrar el resultado por la consola. Recuerda que conviene hacer un int del valor introducido para convertirlo a número entero.

```Python
valor = input("Introduce un número: ")
resultado = int(valor) + 10

print("La suma es:", resultado)
```

Resultado:

```console
Introduce un número: 32
La suma es: 42
```

6.3  Otras conversiones
-----------------------

Aunque en el lenguaje no tengamos que declarar los tipos de variables, los tipos (texto, número, etc...) sí se tienen en cuenta a la hora de ejecutarse el programa.

Por ejemplo si tenemos una variable que contiene un número, y la queremos concatenar en un texto, obtendríamos un error:

```Python
valor = 66
texto = "Mi edad es " + valor
```

El error sería:

```console
TypeError: cannot concatenate 'str' and 'int' objects
```

Para evitarlo, tenemos que forzar el tipo a texto con str():

```Python
valor = 66
texto = "Mi edad es " + str(valor)
```

Por tanto, hay ocasiones en los que tendremos que convertir un valor en determinado tipo. Las funciones para convertir son las siguientes:

*   str(): convierte un valor a texto. str(5) devolvería "5".
*   int(): convierte un valor a número entero. int("5") devolvería 5.
*   float(): convierte un valor a número con decimales. float("5.5") devolvería 5.5
*   bool(): convierte un valor a un booleano. bool("False") devolvería False.

¡OJO!

Si tratas de convertir un valor que no es compatible, el programa fallará y terminará de golpe.

7       Operadores
==================

Los programas necesitan hacer cálculos con números, procesar datos, tomar decisiones según los valores. Para ello necesitamos los operadores.

7.1  Operadores aritméticos
---------------------------

Son todos aquellos que te permitirán hacer sumas, restas y todas los cálculos básicos con valores y con aquello que se guarde en variables, como por ejemplo, la suma:

```Python
chicles = 4
chicles = chicles + 2
```

El programa calcula que de tener 4 chicles, has pasado a tener 6. Las operaciones básicas en programación son:

- suma: +

- resta: -

- multiplicación: *

- división: /

Por ejemplo para calcular el total de segundos que tiene un día:

```console
minutos = 60
segundos = 60
horas = 24
```

totalSegundos = segundos * minutos * horas

Puedes hacer operaciones tan complejas como hagan falta. Para que estas sean más fáciles de leer se pueden utilizar paréntesis como se hace en mates:

```Python
ada = 14
bug = 10
neko = 2
media = (ada + bug + neko) / 3
```

### 7.1.1    Ejercicio 0.5

Escribe un programa que solicite un número al usuario y le reste 5. A continuación debe mostrar el resultado por la consola.

```Python
valor = input("Introduce un número: ")
resultado = int(valor) - 5

print("La resta es:", resultado)
```

Resultado:

```console
Introduce un número: 30
La resta es: 25
```

### 7.1.2    Módulo y exponencial

Hay una operación muy importante en programación, que quizá no sea tan frecuente en tu clase de mates: se trata del módulo. Es una división que devuelve el residuo en lugar del resultado de la división:

```Python
valor = 8
resultado = valor % 3
```

El valor de resultado será: 2.

El exponencial es el resultado de multiplicar un número por sí mismo varias veces. En Python se puede hacer esta operación con el operador **:

```Python
valor = 2
resultado = valor ** 3 # equivale a: 2 * 2 * 2
```

El resultado sería 8.

### 7.1.3    Cambio de signo

Como bien sabes, hay números menores que cero llamados negativos, que se representan con un - por delante:

```
-5, -248, -1.87, ...
```

Si queremos cambiar el signo de un número podemos poner un - por delante:

```Python
temperatura = -11
cuenta = 200

temperatura = -temperatura   11
cuenta = -cuenta    # -200
```

### 7.1.4    Operadores abreviados

En muchas ocasiones, tendrás que operar sobre una variable y guardar el resultado en la propia variable:

```Python
contador = 0
contador = contador + 2
```

En ese tipo de situaciones, puedes usar un operador abreviado, el cual hace la operación y asigna al mismo tiempo. Esto sería equivalente al anterior código:

```console
contador = 0
contador += 2
```

Lo mismo se puede hacer con todos los operadores:

|Operación|Es lo mismo que|Abreviada|
|--|--|--|
|`a = a + 1`| |`a += 1`|
|`a = a - 1`| |`a -= 1`|
|`a = a * 1`| |`a *= 1`|
|`a = a / 1`| |`a /= 1`|
|`a = a % 1`| |`a %= 1`|
 

### 7.1.5    Ejercicio 0.6

Escribe un programa que solicite un número al usuario y lo incremente. A continuación debe mostrar el resultado por la consola. Luego debe decrementar el valor y mostrar el resultado por consola.

¡Utiliza operadores abreviados!

```Python
valor = input("Introduce un número: ")
valor += 1

print("El incremento es", valor)

valor -= 1

print("El decremento es", valor)
```

Resultado:

```console
Introduce un número: 6
El incremento es 7
El decremento es 6
```

7.2  Operadores de comparación
------------------------------

Se trata de operadores que nos permiten comparar un valor con otro. Generalmente se usa con números y el resultado de estas operaciones es Trueo False.

Por ejemplo, para comprobar si un valor es igual a otro usamos el operador: ==

```Python
valor = 5
resultado = valor == 5
```

El resultado sería True.

Los operadores de comparación serían:

•            Igual: ==

•            Distinto: !=

•            Mayor que: >

•            Menor que: <

•            Mayor o igual: >=

•            Menor o igual: <=

También puede utilizarse este operador con texto, tanto para comprobar la igualdad:

```Python
nombre = "Ada"
resultado = nombre == "Bug"
```

El resultado sería False.

También nos permite comparar si un texto es mayor o menor en orden alfabético:

```Python
nombre = "Ada"
resultado = "Ada" < "Bug"
```

El resultado sería True.