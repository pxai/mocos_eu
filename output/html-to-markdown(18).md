12.7 Ejercicios propuestos
--------------------------

### 12.7.1 Ejercicio 4.0

Escribe una función que reciba dos números, detecte cuál es más grande y muestre la diferencia entre ellos.

```Python
def diferencia (valor1, valor2):
    diferencia = 0

    if valor1 > valor2:
        diferencia = valor1 - valor2
    else:
        diferencia = valor2 - valor1

    print("La diferencia es: ", diferencia)

diferencia(10, 5)
diferencia(4, 12)
```

Resultado:

```console
La diferencia es: 5
La diferencia es: 8
```

### 12.7.2 Ejercicio 4.1

Escribe un programa que reciba dos números y un signo de operación aritmética: +, -, *, /. La función debe retornar el resultado de esa operación entre los dos números.

```Python
def calcular (valor1, valor2, op):
    if op ==  "+": return valor1 + valor2
    elif op == "-": return valor1 - valor2
    elif op == "*": return valor1 * valor2
    elif op == "/": return valor1 / valor2
    else: return "Operación desconocida"

resultado = calcular(4, 6, "*")
print(resultado)

resultado = calcular(5, 5, "-")
print(resultado)

resultado = calcular(4, 3, "@")
print(resultado)
```

Resultado:

```console
24
0
Operación desconocida
```

### 12.7.3 Ejercicio 4.2

`def saludo(momentoDelDia)` Esta función recibe como parámetro un momento del día: "mañana", "tarde" o "noche" y debe devolver el correspondiente saludo: "Buenos días", "Buenas tardes", y "Buenas noches" respectivamente.

```Python
def saludo (momento):
    if  momento == "mañana": return "Buenos días"
    elif momento == "tarde": return "Buenas tardes"
    elif momento == "noche": return "Buenas noches"
    else: return ""

print(saludo("tarde"))

def saludo2 (momento):
    return {
        "mañana": "Buenos Días",
        "tarde": "Buenas tardes",
        "noche":"Buenas noches"
    }[momento]

print(saludo2("tarde"))
```

Resultado:

```console
Buenas tardes
Buenas tardes
```

### 12.7.4 Ejercicio 4.3

def iniciarConNumero (numeros, numero)

Esta función debe iniciar todos los elementos del array números con el número que pasamos como parámetro.

```Python
def iniciarConNumero (longitud, numero):
    numeros = []
    for i in range(longitud):
        numeros.append(numero)
    return numeros

def iniciarConNumero1 (longitud, numero): return [numero] * longitud

print(iniciarConNumero(10, 3))
print(iniciarConNumero1(10, 3))
```

Resultado:

```console
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
```

### 12.7.5 Ejercicio 4.4

`def aleatorio (max)` Esta función debe devolver un número aleatorio entre 0 y el valor máximo que se pasa como parámetro.

```Python
import random

def aleatorio (max):
    return random.randint(0, max)

print(aleatorio(5))
```

Resultado:

```console
3
```

### 12.7.6 Ejercicio 4.5

def generarNombre (silabas)

Una función que dado un número de sílabas genere un nombre (alternar consonantes y vocales) aleatorio. Puedes utilizar la función del ejercicio anterior.

```Python
import random

def aleatorio (max):
    return random.randint(0, max - 1)


def generarNombre (silabas):
    vocales = ["a", "e", "i", "o", "u"]
    consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
    nombre = ""

    for i in range(silabas):
        consonante = consonantes[aleatorio(len(consonantes))]
        vocal = vocales[aleatorio(len(vocales))]
        nombre = nombre + consonante + vocal

    return nombre


print(generarNombre(3))
```

Resultado:

```console
xamozu
```

### 12.7.7 Ejercicio 4.6

`def generarPassword(length)`

Una función que dada una longitud genere una cadena o string con caracteres aleatorios. Puedes usar un array de strings con caracteres e ir sacando caracteres aleatorios del array para generar un nombre. Para generar números aleatorios:

```Python
import random

def aleatorio (max):
    return random.randint(0, max - 1)

def generarPassword (longitud):
    caracteres = ["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",
        "0","1","2","3","4","5","6","7","8","9",".","-","_","!","$"]
    password = ""

    for i in range(longitud):
        caracter = caracteres[aleatorio(len(caracteres))]
        password = password + caracter

    return password


print(generarPassword(8))
```

Resultado:

```console
_!5_flg$
```

### 12.7.8 Ejercicio 4.7

Crea una función llamada factura(productos, cantidades, precios) que recibe tres arrays del mismo tamaño con los siguientes contenidos:

1. productos: nombres de productos.

2. cantidades: números enteros indicando cantidad.

3. precios: números con decimales indicando el precio de cada producto.

La función debe recorrer cada producto y calcular el precio total según su cantidad y precio. Se debe mostrar ese precio total de cada producto y al final del programa, se debe mostrar el precio total.

```Python
def factura(productos, cantidades, precios):
    factura = "FACTURAn-------------------n"
    total = 0

    for i in range(len(productos)):
        factura = factura + productos[i]
        factura = factura + " x " + str(cantidades[i])
        factura = factura + " : " + str(precios[i]) + "n"

        total = total + (cantidades[i] * precios[i])

    factura = factura + "n-----------------------n"
    factura = factura + "Total: " + str(total)

    return factura


# Ejemplo de llamada
totalFactura = factura(["Pan","Huevos","Harina"],[1,6,2],[1.2, 0.2, 0.8])
print(totalFactura)
```

Resultado:

```console
FACTURA
-------------------
Pan x 1 : 1.2
Huevos x 6 : 0.2
Harina x 2 : 0.8

-----------------------
Total: 4.0
```

### 12.7.9 Ejercicio 4.8

Este va a ser más complicado. Crea un programa con una función para generar personajes de juegos.

`def generarAtributos (nivelCompensacion)`

Esta función debe definir tres variables: fuerza, velocidad e inteligencia. El programa lo que debe hacer es repartir 20 puntos entre las tres variables. O dicho de otra forma, entre las tres variables deben sumar 20. El parámetro nivelCompensacion debe servir para indicar si se reparten puntos muy diferenciados o igualados, cuanto más alto el valor más descompensado, es decir, la diferencia entre atributos es mayor; cómo hacerlo es cosa del programador.

Al final el programa debe mostrar un resumen de los puntos asignados.

```Python
import random

def aleatorio (max):
    return random.randint(0, max)

def generarAtributos (nivelCompensacion):
    darPuntosA = 0
    inteligencia = 0
    fuerza = 0
    velocidad = 0

    puntosRestantes = 20
    puntos = 0

    while puntosRestantes > 0:
        if nivelCompensacion > puntosRestantes:
            puntos = puntosRestantes
            puntosRestantes = 0
        else:
            puntos = aleatorio(nivelCompensacion+1)
            puntosRestantes = puntosRestantes - puntos

        darPuntosA = aleatorio(3)

        if darPuntosA == 0:
            inteligencia = inteligencia + puntos
        elif darPuntosA == 1:
            fuerza = fuerza + puntos
        elif darPuntosA == 2:
            velocidad = velocidad + puntos

    print("nValores asignados por compensación: ", nivelCompensacion)
    print("Inteligencia: ", inteligencia)
    print("Fuerza: ", fuerza)
    print("Velocidad: ", velocidad)


generarAtributos(3)
```

Resultado:

```console
Valores asignados por compensación:  3
Inteligencia:  3
Fuerza:  1
Velocidad:  10
```

13         Clases
=================

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.019.jpeg)

Las clases nos permiten aplicar una técnica llamada programación orientada a objetos. Es otra estrategia para resolver problemas complejos. Con las funciones, dividimos un problema en pequeños problemas. En cambio, con la programación orientada a objetos, lo que tratamos de hacer es dividir el problema en clases. ¿Pero cómo? representando todo aquello que forma parte del problema utilizando clases.

Imagina que tuviéramos que hacer el programa de un juego de carreras como Mario Kart. Utilizando la programación orientada a objetos podríamos representar los elementos del juego con clases como:

- Personaje, con su nombre y otras propiedades.

- Coche, con sus características de velocidad, resistencia, funciones de aceleración, etc.

- Circuito, con su longitud, sus túneles, sus premios, etc.

13.1 Cómo crear clases
----------------------

Una clase es una estructura de programación que nos permite representar una entidad con sus propiedades y métodos. Es decir, una clase:

- Tiene propiedades: variables propias.

- Hace cosas: funciones.

Por ejemplo, la siguiente clase representa a un gato muy simple, con una función para maullar:

```Python
class Gato:
    def maulla(self):
        print("Miau")
```

Como se puede ver, para definir la clase utilizamos la palabra class seguida del nombre de la clase, con la primera letra en mayúscula. Todo lo que vaya dentro de ese bloque será parte de la clase.

Por otro lado, debes tener en cuenta de que todas las funciones de una clase deben tener el parámetros self, aunque no se use. Ese parámetro se refiere a la propia clase, y se utiliza para referirse a las propiedades y funciones de ella misma, como veremos ahora.

13.2 Clase vs instancia
-----------------------

La clase no es más que la definición del gato. Pero para crear un gato en nuestro programa, debemos crear una instancia. Se hace así:

```Python
gato = Gato()
gato.maulla()
```

Por pantalla veremos:

```console
Miau
```

La instancia es un objeto concreto. La clase solamente es solamente la definición: un gato tiene un nombre y maulla. La instancia es un objeto concreto: Neko.

### 13.2.1 Ejercicio 5.0

Escribe un programa que defina una clase llamada Persona que contenga los métodos dormir, comer y saludar. Dentro de cada método debe sacar algún texto por consola. Crea una instancia de la clase y llama a los distintos métodos.

```Python
class Persona:
    def dormir (self):
        print("ZZZZZ...")

    def comer (self):
        print("Ñam, Ñam...")

    def saludar (self):
        print("Hola, qué tal!")


persona = Persona()

persona.dormir()
persona.comer()
persona.saludar()
```

Resultado:

```console
ZZZZZ...
Ñam, Ñam...
Hola, qué tal!
```

13.3 Función constructora
-------------------------

Ese gato que hemos definido antes hace más bien poco. Vamos a darle una propiedad nombre. Además, vamos a crear una función especial que debe llamarse __init__.

__init__ es lo que se conoce como función constructora. Esta función se llama cuando se crea un objeto de la clase, y por tanto es el lugar ideal para iniciar las propiedades de la clase:

```Python
class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
   
    def maulla(self):
        print("Miau, soy", self.nombre)
```

Ahora, cuando creemos objetos de la clase Gato le pasaremos un nombre y este se quedará como propiedad:

```Python
gato = Gato("Pixi")
gato.maulla()

otroGato = Gato("Cheto")
otroGato.maulla()
```

Y en este caso veremos:

```console
Miau, soy Pixi
Miau, soy Cheto
```

### 13.3.1 Ejercicio 5.1

Escribe un programa que defina una clase llamada Hola. La clase debe tener una función constructora con una propiedad llamada saludo. Esa propiedad se iniciará con la palabra "Hola". Además añadirás un método llamado decirHola, el cual mostrará por pantalla el contenido de la propiedad saludo.

```Python
class Hola:
    def __init__(self):
        self.saludo = "Hola"

    def decirHola (self):
        print(self.saludo)


hola = Hola()
hola.decirHola()
```

Resultado:

```console
Hola
```

13.4 Herencia
-------------

La herencia es un mecanismo que tienen las clases para reutilizar código. Supongamos que queremos hacer una clase que represente a un cachorro de gato. Queremos que haga lo mismo que la clase Gato pero que además ronronee. La clase cachorro podría heredar de la clase Gato, de la siguiente manera:

```Python
class Cachorro(Gato):
    def ronronea(self):
        print("Purrrr")

Ahora podemos hacer lo siguiente. Crear un objeto Cachorro, con las mismas propiedades que la clase Gato. De forma automática, heredará la propiedad nombre y el método maulla:

gatito = Cachorro("Lucifur")
gatito.ronronea()
gatito.maulla()
```

Se vería como:

```console
Purrrr
Miau, soy Lucifur
```

### 13.4.1 super()

Cuando creas una subclase o una clase hija de otra, desde la clase que hereda puedes utilizar la función super() para llamar a funciones de la clase heredada.

Por ejemplo, en el caso anterior, desde la subclase Cachorro podríamos añadir un constructor propio y también llamar al constructor de la super-clase Gato:

```Python
class Cachorro(Gato):
    def __init__(self, nombre):
        super().__init__(nombre)
        print("Gatete creado")

    def ronronea(self):
        print("Purrrr")
```