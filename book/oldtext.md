# Mocos
Los ordenadores, son rápidos y tienen una memoria enorme: son máquinas capaces de ejecutar millones de instrucciones por segundo y de gestionar cantidades inimaginables de datos. Pero eso no significa que sean listos. De hecho no saben hacer nada por sí solos. Para que un ordenador, o una tablet, un móvil,
hagan algo concreto, deben ejecutar un programa. Y un programa es un conjunto de órdenes escritas por los programadores.

Lo interesante de la programación es que podemos tomar el control de la máquina para que esta haga lo que nosotros queramos: desde una instrucción simple, hasta programás muy complejos como navegadores o juegos. La programación engancha porque puedes crear lo que quieras, sin más límite que tu imaginación y tus habilidades.

Pero ¿en qué lenguaje nos podemos comunicar con los ordenadores? Existen infinidad de ellos. Internamente, el ordenador utiliza el lenguaje binario, es decir, una secuencia de unos y ceros
que es capaz de interpretar para hacer algo. Sin embargo, para facilitar la tarea de programación, hay lenguajes más simples, que se parecen mucho al lenguaje de las personas.

Python es uno de esos lenguajes, y tiene muchas virtudes: es sencillo, muy fácil de aprender, permite hacer cualquier cosa, dispone de infinidad de librerías y encima se utiliza de manera profesional. En este libro aprenderás a programar utilizando Python. De forma progresiva, irás conociendo nuevas herramientas que te ofrece el lenguaje para aprender a crear programas más complejos.

¿Qué necesitas para empezar ya mismo? Un navegador. Desde el primer capítulo nos dedicaremos a programar. La mejor forma de apreder a programar es... ¡programando! No hay que tener ningún miedo, y además, es lo más divertido. Así que basta de cháchara. ¡Pasa al siguiente capítulo para escribir tu primer programa!

Nota:
Quizá hayas oido que los ordenadores pueden tener inteligencia artificial o puede que te hayas
enfrentado a juegos en los que los enemigos parecen ser muy listos. En realidad, lo que hace el ordenador es ejecutar programas.

Nota2:
Si quieres instalarte un entorno de programación convencional, ve al apéndice X.

# Hola mundo
El primer programa que suelen escribir los programadores es uno que simplemente saque un mensaje por pantalla. Y ese mensaje suele ser un saludo al mundo: "¡Hola mundo!"
Se hace así:
```python
print("¡Hola mundo!")
```
Si pruebas esto deberías ver por la pantalla algo así:

```console
¡Hola mundo!
```

`print` es una función del lenguaje Python que nos permite mostrar mensajes por pantalla y la utillizaremos a menudo para mostrar mensajes, resultados, etc.

## Comentarios

En un programa, se pueden poner comentarios. Se trata de texto que no se ejecuta y que el ordenador ignora completamente. ¿para qué se utiliza? Generalmente los comentarios se utilizan para explicar determinadas partes del programa.

```Python
# Este programa dice Hola
print("Hola")
```
Python ignora el comentario y mostrará `Hola` por pantalla.
También se pueden hacer comentarios de varias líneas:

```Python
"""
Este es un programa Python
creado por Ada
y revisado por Neko
"""
```
A veces, los comentarios se utilizan de manera temporal para "desactivar" una parte del código que no queremos que se ejecute.

Nota: en general tienes que evitar los comentarios. Un buen programador tiene que intentar escribir programas tan fáciles de entender que no necesiten comentario alguno.

# Variables
Las variables sirven para guardar datos. Los programas de ordenador se dedican, básicamente, a manejar datos para solucionar un problema y ofrecer un resultado. En todo ese proceso es necesario guardar datos, y para eso se utilizan las variables. Las variables son como contenedores de datos. En cierto modo es como los vasos, platos, fuentes que se utilizan para cocinar: contienen algo, se trabajo con ello, se mezcla, se procesa y se consigue un resultado. Con un poco de suerte algo rico.
Para definir una variable en python basta con indicar su nombre y darla algún valor. Por ejemplo:
```Python
nombre = "Ada"
```

Acabamos de crear una variable que contiene el valor "Ada". "Ada" es un dato, de tipo texto. Ahora podemos mostrar el valor de esa variable por la pantalla:

```Python
print(nombre)
```
Que por pantalla sería

```console
Ada
```
En cualquier momento, podríamos cambiar el valor de esa variable:
```Python
nombre = "Ada"
print(nombre)
nombre = "Neko"
print(nombre)
```
Y por pantalla veríamos:
```console
Ada
Neko
```

Nota:
También se puede mostrar el contenido de una variable como parte del mensaje.
Existen varias opciones para ello:

## Separar por comas
Basta con intercalar las variables y el texto con comas:
```Python
nombre = "Bug"
edad = 10
print("Hola, me llamo", nombre)
print("Soy", nombre, "tengo", edad, "años")
```
Que por pantalla sería

```console
Hola, me llamo Bug
Soy Bug tengo 10 años
```

## String de formato
Un mensaje que precedido de la letra `f` y las variables entre llaves:
```Python
nombre = "Bug"
edad = 10
print(f"Hola, me llamo {nombre}")
print(f"Soy {nombre} tengo {edad} años")
```
Que por pantalla sería

```console
Hola, me llamo Bug
Soy Bug tengo 10 años
```

## Sustitución de porcentaje
Se crea un mensaje donde los elementos %s son sustituidos por variables.
```Python
print("Hola, me llamo %s" % nombre)
```
Que por pantalla sería

```console
Hola, me llamo Ada
```

Puedes hacer lo mismo con varias variables
```Python
nombre = "Neko"
edad = 5

print("Hola, me llamo %s y tengo %d años" % (nombre, edad))
```
Que por pantalla sería:

```console
Hola, me llamo Neko y tengo 5 años
```
# Tipos de datos
¡Datos! Es la materia prima con la que trabajan los programas. Son el elemento que transforman. Un programa recibe datos, los transforma y los devuelve como un resultado.
Los datos pueden ser de distinto tipo, según lo que nuestro programa tenga que hacer. Pueden ser números, puedes ser palabras o textos, pueden incluso ser nulos o vacíos.
Para guardar los datos, generalmente usamos variables.
Si comparamos la programación con la cocina, el azúcar, la harina y los huevos serían datos, los recipientes serían variables: la tarta sería otro dato, el resultado y la receta sería el programa.
¿Cómo sabe Python que tipo de dato maneja? No hace falta indicarselo como en otros lenguajes. Por eso es un lenguaje más simple y flexible. Aunque tampoco podremos hacer lo que nos de la gana con los datos.

A continuación, vamos a ver los tipos básicos de datos

## Números
Se trata de todos los tipos de números:
- Enteros:
1, 2, 3, 4,...

```python
contador = 10
edad = 12
```

- Con decimales:
Los números con decimales se expresan utilizando un `.` para separar la parte entera de la decimal, como 4.5 o 3.1415. Es probable que en clase de mates utilices una coma para separar las decimales, pero en programación se usa el formato inglés y debemos usar un `.`.

```python
peso = 34.67
precio = 242.9943
```

- Negativos:
Los números menores que 0 se expresan con un guión por delante: -4, -5, -3.1415,...

```python
nota = -5
temperaturaEnMarte = -50.676
```

## Texto
El texto, también llamados cadenas o *strings* son cualquier conjunto de palabras entre comillas dobles o simples.

```python
nombre = "Ada"
frase = ""
palabras = 'Voy a trabajar'
novia = 'Solo quiero que seamos "amigos"'
```
En el caso del texto, podemos meter una serie de caracteres especiales que nos permiten efectos interesantes. Esos caracteres se escriben con una contrabarra o backslash por delante: `\`

- Salto de linea
Esto añade un salto de línea al texto si este se muestra por pantalla:

```python
frase = "Hola,\n qué tal"
```
se mostrará así:
```shell
Hola,
qué tal
```

También se puede definir un texto de varias líneas así:

```python
cancion = """Era un domingo
a la tarde
fui a los coches 
de choque"""
```

- Tabulaciones
Esto añade una tabulación (varios espacios) al texto si este se muestra por pantalla:

```python
frase = "Nombre\tApellido\tEdad"
```
se mostrará así:
```shell
Nombre	Apellido	Edad
```
Otros caracteres especiales:

- \\ Para mostrar la contrabarra en un texto.
- \" Para mostrar una comilla doble en un texto.
- \' Para mostrar una comilla simple en un texto.
- \a Para hacer sonar un pitido.

## Booleanos
El tipo booleano solo puede tener dos valores posibles:
`True` o `False`, es decir verdadero o false. Se trata de un tipo de dato fundamental en programación ya que se utiliza para tomar decisiones.

```python
terminado = False
esMayor = True
pythonMola = True
```

## Listas
Las listas son conjuntos de datos, que se definen de la siguiente manera:

```python
amigas = ["Ada", "Miranda", "Ruby"]
```
Pueden ser de cualquier tipo, pero lo normal es que todos los elementos de una lista sean del mismo tipo:

```python
enemigas = []
edades = [12, 16, 30, 0, 22, 1, 1, 12]
verdades = [True, False, False, True]
```
Para poder referirnos a un valor concreto de la lista, tenemos que indicar la posición del elemento de la lista que nos interesa, empezando desde 0:

```python
nombres = ["Ada", "Neko", "Bug"]
print(nombres[0])  # "Ada"
```
En el caso de la lista `nombres`, las posiciones posibles serán 0, 1 y 2.
¡Pero ojo! si pasas una posición demasiado grande, el programa terminará con error:
```python
nombres = ["Ada", "Neko", "Bug"]
print(nombres[4])  # ¡ERROR!
```
Volveremos sobre las listas y otras estructuras más adelante. 

## None
Aunque suene un poco raro, en los programas a veces hay que tratar con algo que representa el vacío, la nada. 
Existe una palabra que nos permite representar la nada en Python, y esa es: `None`

```python
valorInicial = None
dato = None
```
En realidad no se suele utilizar para crear variables. None representa un valor en situaciones especiales. Por ejemplo, si se trata de sacar información de un sitio en el que no hay nada como un fichero, o un dato que el usuario no nos da.

# Leyendo datos
Para que un programa pueda hacer algo, muchas veces necesita que el usuario introduzca un dato. Por ejemplo, si queremos que un programa nos diga cuantas letras tiene nuestro nombre, o cuanto falta para nuestro cumpleaños, lo primero que tendrá que hacer el programa es pedir un dato.

Los programas básicos como los que estamos viendo de momento, utilizan la consola para ejecutarse. Son esas pantallas negras donde se ponen órdenes escritas ;)

Para poder pedirle al usuario un dato y guardarlo en una variable, se utiliza la función `input`:

```python
nombre = input("Dime tu nombre: ")
print("Hola ", nombre)
```

En la pantalla verías lo siguiente:

```code
Dime tu nombre: 
```
La función input hace que el mensaje `Dime tu nombre: ` aparezca en pantalla. También hace que el programa se pare a la espera de que el usuario escriba algo.
Si el usuario escribe `Rosa` en la consola, se vería:

```code
Dime tu nombre: Rosa
Hola Rosa
```

## Cuidado con los datos
Cada vez que uses la funcion `input` para que el usuario escriba algo, sea lo que sea **se guardará como texto**. Aunque se escriba un número:


```python
valor = input("Dame un número: ")
doble = valor + valor
print(doble)
```

Si el usuario introduce un número como `4` este sería el resultado:

```console
Dame un número: 4
44
```
En lugar de sumar `4 + 4` y mostrar `8`, lo que ha hecho es unir `4` y `4`, porque en realidad, cuando se ha leido a través de `input` ese `4` es texto: `"4"`

Para evitarlo, tenemos que usar otra función para convertir ese dato en número entero: `int()`

```python
valor = input("Dame un número: ")
doble = int(valor) + int(valor)
print(doble)
```

O incluso lo podemos convertir antes:

```python
valor = input("Dame un número: ")
valor = int(valor)
doble = valor + valor
print(doble)
```

O incluso aplicarlo a `input`: 


```python
valor = int(input("Dame un número: "))
doble = valor + valor
print(doble)
```

Ahora sí:
```console
Dame un número: 4
8
```

# Operadores
Los programas necesitan hacer cálculos con números, procesar datos, tomar decisiones según los valores. Para ello necesitamos los operadores.

## Operadores aritméticos
Son todos aquellos que te permitirán hacer sumas, restas y todas los cálculos básicos con valores y con aquello que se guarde en variables, como por ejemplo, la suma:

```python
chicles = 4
chicles = chicles + 2
```
El programa calcula que de tener 4 chicles, has pasado a tener 6.
Las operaciones básicas en programación son:
- suma: `+`
- resta: `-`
- multiplicación: `*`
- división: `/`

Por ejemplo para calcular el total de segundos que tiene un día:
```python
minutos = 60
segundos = 60
horas = 24

totalSegundos = segundos * minutos * horas
```

Puedes hacer operaciones tan complejas como hagan falta. Para que estas sean más fáciles de leer se pueden utillizar paréntesis como se hace en mates:

```python
ada = 14
bug = 10
neko = 2
media = (ada + bug + neko) / 3
```

### Módulo y exponencial
Hay una operación muy importante en programación, que quizá no sea tan frecuente en las mates: se trata del **módulo**. Es una división que devuelve el residuo en lugar del resultado de la división:

```python
valor = 8
resultado = valor % 3
```
El valor de resultado será: `2`.

El exponencial es el resultado de multiplicar un número por sí mismo varias veces. En Python se puede hacer esta operación con el operador `**`:

```python
valor = 2
resultado = valor ** 3 # equivale a: 2 * 2 * 2
```

El resultado sería `8`.

### Operadores abreviados
En muchas ocasiones, tendrás que operar sobre una variable y guardar el resultado en la propia variable:

```python
contador = 0
contador = contador + 2
```
En ese tipo de situaciones, puedes usar un operador abreviado, el cual hace la operación y asigna al mismo tiempo. Esto sería equivalente al anterior código:

```python
contador = 0
contador += 2
```
Lo mismo se puede hacer con todos los operadores:

|Operación|Es lo mismo que|Abreviada|
|--|--|--|
|a = a + 1||a += 1|
|a = a - 1||a -= 1|
|a = a * 1||a *= 1|
|a = a / 1||a /= 1|
|a = a % 1||a %= 1|
|a = a ** 1|| a **= 1|

## Operadores de comparación
Se trata de operadores que nos permiten comparar un valor con otro. Generalmente se usa con números y el resultado de estas operaciones es `True`o `False`.

Por ejemplo, para comprobar si un valor es igual a otro usamos el operador: `==`

```python
valor = 5
resultado = valor == 5
```

El resultado sería `True`.

Los operadores de comparación serían:

- Igual: `==`
- Distinto: `!=`
- Mayor que: `>`
- Menor que: `<`
- Mayor o igual: `>=`
- Menor o igual: `<=`

También puede utilizarse este operador con texto, tanto para comprobar igualdad:

```python
nombre = "Ada"
resultado = nombre == "Bug"
```
El resultado sería `False`.
También nos permite comparar si un texto es mayor o menor en orden alfabético:

```python
nombre = "Ada"
resultado = "Ada" < "Bug"
```

El resultado sería `True`.

## Operadores booleanos
Los operadores booleanos nos permiten hacer operaciones con valores booleanos `True`o `False`. 

### and
Este operador solo devuelve `True` si los dos operandos también son `True`:

```python
valor = 5
resultado = (valor == 5) and True;
```

El resultado sería `True`.
Para resumir todas las posibles opciones, esta sería lo que se denomina tabla de la verdad del operador `and`.

|a | | b| resultado |
|--|--|--|--|
|`False` | `and` |`False` |`False` |
|`False` | `and` |`True` |`False` |
|`True` | `and` |`False` |`False` |
|`True` | `and` |`True` |`True` |

### or
Este operador solo devuelve `True` si cualquiera de los dos operandos también son `True`:

```python
valor = 5
resultado = (valor == 5) or True;
```

El resultado sería `True`.
Para resumir todas las posibles opciones, esta sería lo que se denomina tabla de la verdad del operador `or`.

|a | | b| resultado |
|--|--|--|--|
|`False` | `or` |`False` |`False` |
|`False` | `or` |`True` |`True` |
|`True` | `or` |`False` |`True` |
|`True` | `or` |`True` |`True` |

### not
Este operador solo devuelve `True` si los dos operandos también son `True`:

```python
valor = True
resultado = not valor;
```

El resultado sería `False`.
Para resumir todas las posibles opciones, esta sería lo que se denomina tabla de la verdad del operador `not`.

| | a| resultado |
|--|--|--|
| `not` |`False` |`False` |
| `not` |`True` |`False` |

### Combinando operadores
Podemos combinar los operadores tanto como necesitemos:

```python
jubilado = 65
if edad > 17 and edad < (jubilado + 1):
	print("Ya puedes trabajar")
```

Generalmente, los operadores condicionales se utilizan dentro de las condiciones de los bloques condicionales, bucles, etc.

# Ejercicios propuestos1

## Ejercicio 1.0
Escribe un programa que muestre por consola el texto “Hola Mundo!”.

```python
print("Hola Mundo!")
```
Resultado:

```console
Hola Mundo!
```

## Ejercicio 1.1
Luego define las asigna un valor a las variables nombre y edad y muestra su valor por pantalla.
```python
nombre = "Ada"
edad = 14
print("Tu nombre es", nombre, ", tienes", edad, "años")

# Alternativa:
# print("Tu nombre es %s, tienes %d años" % (nombre, edad))
```
Resultado:

```console
Tu nombre es Ada y tienes 14 años.
```

## Ejercicio 1.2
Escribe un programa que solicite un nombre al usuario y lo guarde en una variable. A continuación debe mostrar un saludo por consola.


```python
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

## Ejercicio 1.3
Escribe un programa que defina una variable de cada tipo visto aquí, y los muestre por la consola.

```python
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

## Ejercicio 1.4
Escribe un programa que solicite un número al usuario y le sume 10. A continuación debe mostrar el resultado por la consola. Recuerda que conviene hacer un `int` del valor introducido para convertirlo a número entero.

```python
valor = input("Introduce un número: ")
resultado = int(valor) + 10

print("La suma es:", resultado)
```
Resultado:

```console
Introduce un número: 32
La suma es: 42
```

## Ejercicio 1.5
Escribe un programa que solicite un número al usuario y le reste 5. A continuación debe mostrar el resultado por la consola.

```python
valor = input("Introduce un número: ")
resultado = int(valor) - 5

print("La resta es:", resultado)
```
Resultado:

```console
Introduce un número: 30
La resta es: 25
```

## Ejercicio 1.6
Escribe un programa que solicite un número al usuario y le multiplique 7. A continuación debe mostrar el resultado por la consola.

```python
valor = input("Introduce un número: ")
resultado = int(valor) * 7

print("La multiplicación es:", resultado)
```

Resultado:

```console
Introduce un número: 3
La multiplicación es: 21
```

## Ejercicio 1.7
Escribe un programa que solicite un número al usuario y lo divida por 2. A continuación debe mostrar el resultado por la consola.

```python
valor = input("Introduce un número: ")
resultado = int(valor) / 2

print("La división es:", resultado)
```
Resultado:

```console
Introduce un número: 60
La división es: 30
```

## Ejercicio 1.8
Escribe un programa que solicite un número al usuario y haga módulo 3. A continuación debe mostrar el resultado por la consola.

```python
valor = input("Introduce un número: ")
resultado = int(valor) % 3

print("El módulo es:", resultado)
```

Resultado:

```console
Introduce un número: 7
El módulo es: 1
```

## Ejercicio 1.9
Escribe un programa que solicite un número al usuario y le aplique un exponencial de 2. A continuación debe mostrar el resultado por la consola.

```python
valor = input("Introduce un número: ")
resultado = int(valor) ** 2

print("El exponencial es:", resultado)

```
Resultado:

```console
Introduce un número: 4
El exponencial es: 16
```

## Ejercicio 1.10
Escribe un programa que solicite un número al usuario y lo incremente. A continuación debe mostrar el resultado por la consola. Luego debe decrementar el valor y mostrar el resultado por consola.

```python
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

## Ejercicio 1.11
Escribe un programa que solicite un número al usuario y le reste 5. A continuación debe cambiarle el signo y mostrar el resultado por la consola.

```python
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
## Ejercicio 1.11
Escribe un programa que solicite un número al usuario. Después debe comprobar si la operación % 2 es igual a 0 y mostrar el resultado. Si se divide un número por 2 y la resta es 0, significa que ese número es par.

```python
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

## Ejercicio 1.11
Escribe un programa que solicite dos números al usuario. Después debe comparar su desigualdad y debe mostrar el resultado por la consola.

```python
valor1 = input("Introduce un número: ")
valor2 = input("Introduce otro número: ")

resultado = valor1 != valor2

print("¿Son distintos?", resultado)
```
Resultado:

```console
Introduce un número: 42
Introduce otro número: 42
¿Son distintos? False
```

## Ejercicio 1.12
Escribe un programa que solicite un número al usuario. Después debes comprobar si ese número es mayor o igual que 0, es decir, positivo.

```python
valor = input("Introduce un número: ")

resultado = int(valor) >= 0

print("¿Es positivo?", resultado)
```
Resultado:

```console
Introduce un número: 6
¿Es positivo? True
```

## Ejercicio 1.13
Escribe un programa que solicite un número al usuario. Después debe comparar si el primero es menor que 0 y mostrar el resultado por la consola. Estaríamos detectando si el número es negativo.

```python
valor = input("Introduce un número: ")

resultado = int(valor) < 0

print("¿Es negativo?", resultado)
```
Resultad:

```console
Introduce un número: -3
¿Es negativo? True
```

## Ejercicio 1.14
Escribe un programa que solicite un número al usuario. Después debe comparar si el primero es mayor que 0 y además es par.

```python
valor = input("Introduce un número: ")
valor = int(valor)
resultado = (valor >= 0) and (valor % 2 == 0)

print("¿Es par y positivo?", resultado)
```
Resultado:

```console
Introduce un número: 14
¿Es par y positivo? True
```

## Ejercicio 1.15
Escribe un programa que solicite dos números al usuario y compruebe si alguno de los dos es positivo. A continuación debe mostrar el resultado por la consola.

```python
valor1 = input("Introduce un número: ")
valor2 = input("Introduce otro número: ")

resultado = (int(valor1) >= 0) or (int(valor2) >= 0)

print("¿Es alguno de los dos positivo?", resultado)
```
Resultado:

```console
Introduce un número: -4
Introduce otro número: 6
¿Es alguno de los dos positivo? True
```

## Ejercicio 1.16
Escribe un programa que solicite un número al usuario y compruebe que nos es ni positivo ni par.

```python
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

## Ejercicio 1.17
Define una lista de nombres y muéstralas por pantalla

```python
nombres = ["Ada", "Bug", "Neko"]

print(nombres) # ["Ada", "Bug", "Neko"]

```
Resultado:

```console
["Ada", "Bug", "Neko"]
```

# Condiciones
En algún momento, los programas necesitan hacer una cosa u otra dependiendo de una condición. Por ejemplo, si un usuario introduce un dato incorrecto, el programa se acaba.
Si un dato tiene determinado valor, se procesa de una forma y si no, de otra. ¿Cómo se consigue ese comportamiento? Mediante condiciones.

Las condiciones son estructuras de programación que nos permiten que un código se ejecute solo cuando se cumplan unas condiciones.

## if
La estructura más simple para hacer una condición es el `if`, el cual tiene este aspecto:

```python
if *condicion*:
	*instrucciones*
	*instrucciones*
	*...*
```

Como puedes observar, `if` comienza con una condición. La condición puede ser cualquier expresión que devuelva un booleano, es decir, será True o False, verdadero o falso.
Si es True, las instrucciones dentro del `if` se ejecutarán, y si no se saltarán.
Por ejemplo

```python
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

```python
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
También debes observar algo muy importante: las instrucciones dentro del `if` van detrás de unos espacios o una tabulación. Esa es una peculiaridad del lenguaje de programación Python: en cualquier bloque como una condicón, un bucle, una función, su contenido debe ir tabulado. Esa es una forma que facilita la lectura y permite reconocer fácilmente la estructura de un programa para otros programadores. Incluso para ti mismo si lo has creado.

## if else
Con el if podemos crear un bloque que solo se ejecute si se cumple una condición. Pero ¿Qué pasa si queremos que el programa haga una cosa u otra según una condición?
Para poder meter "la otra" opción, utilizamos una estructura if-else:

```python
if *condicion*:
	*instrucciones*
else:
	*instrucciones*
```

Por ejemplo:

```python
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

## if elif else
Existe otra variante cuando necesitamos comprobar varias condiciones. Para eso existe la estructura if-elif-else:

```python
if *condicion1*:
	*instrucciones*
elif: *condicion2*:
	*instrucciones*
elif *condicion3*
	*instrucciones*
else:
	*instrucciones*
```

Supongamos que queremos un programa que sea capaz de saludar en distintos idiomas. Podriamos crear un programa como el siguiente:

```python
idioma = input("¿Qué idioma hablas?")

if idioma == "Español":
	print("Hola"):
elif idioma == "Inglés":
	print("Hello"):
elif idioma == "Francés":
	print("Salut")
else:
	print("No conozco ese idioma")
```

Podemos tener tantos `elif` como hagan falta.

# Bucles
Como decíamos al principio, los ordenadores son muy muy tontos. Solo hacen lo que se les diga. Pero por contra, tienen enormes capacidades y una paciencia infinita. No les importará lo más mínimo hacer lo que sea tantas veces como sea necesario.

Una de las tareas más típicas para un ordenador es repetir una instrucción. Esto es algo que se puede conseguir mediante estructuras de bucle. Un bucle es una acción que se repite. Generalmente un bucle tiene una condición para ejecutarse. Si esas condiciones se cumplen, entonces se ejecutarán las órdenes que contenga ese bucle.
Puedes ver un bucle como una montaña rusa en la que das varias vueltas. 
A continuación veremos distintos tipos de bucle.

## Bucle while
Un bucle while se ejecuta mientras una condición se cumpla. Su estructura es muy simple:

```python
while *condicion*:
	*instrucciones*
```
Por ejemplo, vamos a ejecutar un bucle mientras el valor de una variable sea mayor que 0.

```python
contador = 10
while contador > 0:
	print("Estoy dentro del bucle")
	contador = contador - 1
```

Nota: ¡Ojo! ¿Te has fijado en que dentro del bucle estamos restando un valor a `contador`? Si no tenemos cuidado y nos olvidamos de hacer eso, el valor de contador nunca cambiaría y crearíamos un bucle infinito. ¡El programa nunca terminaría y se quedaría atascado para siempre!

Veamos otro ejemplo. El siguiente programa solicita un dato al usuario en un bucle. El programa no saldrá del bucle mientras el usuario no meta un dato distinto de vacío `""`:

```python
nombre = ""
while nombre == "":
	nombre = input("¿Cómo te llamas?")

print("Hola", nombre)
```

## Bucle For
El bucle for lo utilizamos para repetir una acción un número concreto de veces. Más que una condición, utiliza una especie de contador:

```python
for *variable* in *rango*:
	*instrucciones*
```

Por ejemplo, el siguiente bucle mostrará el mensaje `hola` 5 veces:

```python:
for i in range(4):
	print("Hola")
```
El resultado sería:
```code
Hola
Hola
Hola
Hola
```

Algo muy interesante en los bucles for es que la variable `i`, la cual podría tener el nombre que queramos, tendrá el valor correspondiente a cada vuelta del bucle. Para verlo mejor, basta con cambiar un poco el programa anterior:

```python:
for i in range(4):
	print("Hola", i)
```

Y comprobar el resultado:

```code
Hola 0
Hola 1
Hola 2
Hola 3
```

### Cambiar el rango
Por defecto, `range(4)` está devolviendo una lista de 0 a 3, es decir: 0, 1, 2, 3. Son un total de cuatro elementos y por tanto el bucle dará cuatro vueltas.

Obviamente, se puede crear cualquier tipo de rango. Si no se indica nada, el rango comienza en 0. Pero se puede indicar un rango entre dos números:
range(0, 4) # 0, 1, 2, 3
range(2, 6) # 2, 3, 4, 5

Por ejemplo:

```python:
for i in range(5, 9):
	print("Hola", i)
```
El resultado sería:
```code
Hola 5
Hola 6
Hola 7
Hola 8
```

También se puede indicar un tercer parámetro para indicar cómo se salta de un valor a otro. Por ejemplo de 2 en 2:
```python
range(1, 11, 2) # 1, 3,
```

En el siguiente ejemplo, el bucle se haría con números pares.
```python:
for i in range(0, 6, 2):
	print("Hola", i)
```
El resultado sería:
```code
Hola 0
Hola 2
Hola 4
```

### Hacia atrás
También se podría recorrer el bucle hacia atrás, utilizando un salto negativo

```python:
print("Iniciando cuenta atrás: ")
for i in range(5, 0, -1):
	print(i)
```

El resultado sería:

```code
5
4 
3
2
1
```

### Bucles sobre listas
Los bucles `for` son especialmente útiles cuando queremos recorrer todos los elementos de una lista, para mostrarlos, procesarlos o lo que sea. La forma es muy sencilla:

```python
objetos = ["estrella", "seta", "flor"]
for objeto in objetos:
	print(objetos)
```
En cada vuelta del bucle la varialbe `objeto` tomara un valor de la lista `objetos`, así que el resultado sería el siguiente:

```console
estrella
seta
flor
```

### Saliendo del bucle
En ocasiones puede que nos interese salir de un bucle y no seguir procesando nada más. Supongamos que tenemos un programa para buscar un nombre dentro de una lista:

```python
nombres = ["Mia", "Jon", "Arya", "Ane", "Bug", "Ada", "Lisp"]
for nombre in nombres:
	if nombre == "Ane":
		print("Ane está en la lista")
```
El problema de ese programa es que aunque encuentre a `Ane`, el bucle seguirá hasta el final de la lista. Si esa lista es muy grande, nuestro programa será ineficiente! Como decíamos al principio, los ordenadores son muy tontos. Si no les decimos que paren, seguirán adelante.

Por suerte, en los bucles podemos usar la instrucción `break`, la cual conseguirá que el bucle termine de golpe:

```python
nombres = ["Mia", "Jon", "Arya", "Ane", "Bug", "Ada", "Lisp"]
for nombre in nombres:
	if nombre == "Ane":
		print("Ane está en la lista")
		break
```

## ¿Cuándo usar while o for?
Aunque con los dos podrías hacer lo mismo, realmente cada uno tiene un uso más lógico.

El bucle for se utiliza claramente cuando se quiere ejecutar algo un número concreto de veces, ni más ni menos. O bien, como veremos más adelante, cuando se quieren recorrer estructuras de datos como listas de principio a fin.

El bucle while se puede utilizar cuando las condiciones no son muy concretas. Por ejemplo, si queremos que el usuario introduzca un dato, lo podemos hacer en un bucle. El bucle no terminará hasta que el usuario no introduzca un dato bueno (esa sería la condición).

# Estructuras de datos
Hasta ahora hemos estado jugando con datos simples, variables que contienen un número, un texto, etc. Pero existen otros tipos que nos permiten crear datos más complejos. No es que sean difíciles, simplemente pueden contener algo más que un simple número.

Los programas de ordenador pueden hacer cosas muy complicadas, pero en esencia, todo lo que hacen es procesar datos. A continuación vamos a ver algunos tipos de datos.

## Listas
Las listas son un conjunto de datos indexados numéricamente. Esa es la definición formal, pero su propio nombre ya te dice lo que son: ¡una lista! En el capítulo sobre tipos de datos ya presentamos las listas y vimos cómo se crean:

```python
idiomas = ["Inglés", "Español", "Francés"]
``` 
Recuerda que puedes acceder a los elementos a través de un índice:

```python
idiomas = ["Inglés", "Español", "Francés"]
print(idiomas[2]) # Francés
``` 
La lista se puede representar así:

|0|1|2|
|--|--|--|
|"Inglés"|"Español"|"Francés"|

Si queremos añadir un elemento a una lista, basta con utilizar la función `append`:

```python
idiomas = ["Inglés", "Español", "Francés"]
idiomas.append("Italiano")
print(idiomas) # ["Inglés", "Español", "Francés", "Italiano"]
```

Y si queremos eliminar un elemento del array, se puede usar la orden del:

```python
idiomas = ["Inglés", "Español", "Francés"]
del idiomas[1]
print(idiomas) # ["Inglés", "Francés"]
```

¡Pero OJO!
En Python **NO** se puede cambiar el valor de un elemento del array:

```python
idiomas = ["Inglés", "Español", "Francés"]
idiomas[2] = "Italiano" # ¡ERROR!
```

Y recuerda, para recorrer la lista, podemos usar un bucle `for`:

```python
idiomas = ["Inglés", "Español", "Francés"]
for idioma in idiomas:
	print(idioma)
```

También se puede recorrer la lista utilizando el índice. Para eso tendremos que utilizar la función `range`, pasándole la longitud de la lista con `len`:

```python
idiomas = ["Inglés", "Español", "Francés"]
for i in range(len(idiomas)):
	print(idiomas[i])
```
De todas formas, si no se necesita el índice dentro del bucle, es mejor recorrer la lista sin índice tal y como se hace en el ejemplo anterior.

En otros lenguajes, a las listas se les llama arrays.
Ya los deberías conocer, pero te lo volvemos a recordar.

## Diccionarios
Los diccionarios son conjuntos de datos donde cada elemento tiene una clave y un valor.
Dichos de otra manera, son como una lista, pero en lugar de tener un índice numérico como 0,1, 2,... tienen el valor que tú quieras.

Por ejemplo, podemos definir un diccionario que contenga las edades de varias personas, donde el nombre es la clave y la edad el valor:

```python
edades = { "Ada": 14, "Bug": 10, "Neko": 2 }
print(edades["Ada"])  #  14
```
El diccionario se puede representar así:

|"Ada"|"Bug"|"Neko"|
|--|--|--|
|14|10|2|

Para añadir nuevos elementos, se puede asignar un nuevo valor:

```python
edades = {"Ada": 14, "Bug": 10, "Neko": 2}

print(edades)  # {'Bug': 10, 'Neko': 2, 'Ada': 14}

edades["Miranda"] = 23;

print(edades) # {'Bug': 10, 'Neko': 2, 'Ada': 14, 'Miranda': 23}

del edades["Bug"]

print(edades) # {'Neko': 2, 'Ada': 14, 'Miranda': 23}

for nombre in edades.keys():
    print(nombre, edades[nombre])
```

Podemos eliminar valores del diccionario con la función `del`:
```python
edades = {"Ada": 14, "Bug": 10, "Neko": 2}
print(edades)  # {'Bug': 10, 'Neko': 2, 'Ada': 14}
del edades["Bug"]
print(edades) # {'Neko': 2, 'Ada': 14}
```

¿Y si queremos recorrer todos los valores del diccionario?
No hay problema, pero tendremos que utilizar una función que nos devuelva todas las claves del diccionario: `keys()`. Sería así:

```python
edades = {"Ada": 14, "Bug": 10, "Neko": 2}
for nombre in edades.keys():
    print(nombre, edades[nombre])
```
Por pantalla ser vería:

```console
Ada 14
Bug 10
Neko 2
```

Nota:
En otros lenguajes, a los diccionarios se les llama `hash` o `hashtables`

## Estructuras de datos combinadas
¡Las estructuras básicas como listas y diccionarios pueden contener valores que también sean listas y diccionarios!

Se pueden crear estructuras de datos anidadas, tan complejas como necesites. Por ejemplo, supongamos que quieres representar los datos de un amigo con el siguiente diccionario:

```python
amigo =  {"nombre": "Neko", "edad": 2}
```

¿Y si quieres tener una estructura de datos que contenga varios amigos? En ese caso, puedes hacer una lista de diccionarios:

```python
amigos = [
	{"nombre": "Neko", "edad": 2},
	{"nombre": "Bug", "edad": 10},
	{"nombre": "Ada", "edad": 14}
]
print(amigos[1]) # {"nombre": "Bug", "edad": 10}
print(amigos[2]["nombre"]) # Ada
```

¿Y si quieres una estructura de datos que contenga el estado de un juego, con sus personajes y sus objetos? Podría hacer un diccionario anidado, donde la clave es el nombre del personaje:

```python
pantalla = {
	"Mario": { "vida": 10, "objetos": ["seta", "estrella"]},
	"Luigi": { "vida": 7, "objetos": []},
	"Toad": { "vida": 15, "objetos": ["seta"]},
}

print(pantalla["Luigi"]["vida"])  # 7
```

Pero ¿Cómo sé que tipo de estructura debo diseñar? Depende de cómo la vayas a usar. A veces necesitarás recorrer todos, otras veces necesitarás acceder a un elemento concreto,... según lo que requiera tu programa tendrás que diseñar una estructura concreta.


# Funciones
Las funciones son pequeños programas dentro de los programas. Esta sería una función que simplemente saca un saludo por pantalla:

```python
def saludo ():
	print "Hola"
```
Como se puede ver, una función se define utilizando la palabra `def` seguida del nombre de la función, en este caso `saludo` y la lista de parámetros `()`, la cual está vacía en este caso.
En el cuerpo de la función, podemos poner las instrucciones que queramos

Una vez definida esa función, cada vez que la utilicemos se ejecutará el código que hay en ella:

```python
saludo()
```
Lo cual mostrará:
```console
Hola
```

## Parámetros
Las funciones pueden recibir parámetros. Estos se convierten en variables dentro de la función y nos permiten que la función haga cosas diferentes según lo que les pasemos.

Por ejemplo, podemos crear una función que salude a alguien:

```python
def saluda(persona):
	print("Hola", persona)
```
Dentro de la función, el valor de `persona` será distinto según lo que se le pase en la llamada
Se podría usar así:

```python
saluda("Neko")  # persona será "Neko"
saluda("Ada")   # persona será "Ada"
```
Lo que resultaría en:

```
Hola Neko
Hola Ada
```

### Parámetro con valor por defecto
Los parámetros de una función pueden tener un valor por defecto. Es decir, se les puede asignar un valor concreto y si no se pasa ese parámetro en la llamada, el parámetro tomará ese valor por defecto.


```python
def saluda(persona, veces = 3):
	for i in range(veces):
		print("Hola", persona)
```
Si se le llama con:
```python
saluda("Neko", 2)
```

Se vería:
```
Hola Neko
Hola Neko
```

En cambio
```python
saluda("Bug")
```

Sería:
```console
Hola Bug
Hola Bug
Hola Bug
```


## Retorno
Las funciones pueden hacer todas las operaciones que sean necesarias, pero son más útiles cuando devuelven un resultado.

Para eso se utiliza la instrucción `return`, la cual solo puede devolver un dato concreto o una estructura de datos.

Por ejemplo, una función que calcule la suma de dos valores:

```python
def suma(a, b):
	resultado = a + b
	return resultado
```
Se puede abreviar un poco haciendo directamente:

```python
def suma(a, b):
	return a + b
```

Se podría usar la función así:

```python
print(suma(40, 2))  # 42
```

Debes tener en cuenta un par de cosas con el `return`:
1- Una vez se hace `return`, el programa sale de la función.
2- Puedes tener más de un `return` en la función, pero solo se ejecutará uno de ellos. 

Otro ejemplo, una función que multiplique un valor varias veces. Si el número de veces es menor que 1 devolverá un 0:

```python
def multiplica(numero, veces):
	if (veces > 0): 
		total = 1
		for i in range(veces):
			total = total * numero
	else:
		return 0

multiplica(2, 3) # 8
```

Nota: la función anterior queda más clara así.
```python
def multiplica(numero, veces):
	if (veces < 1): return 0 

	total = 1
	for i in range(veces):
		total = total * numero
```
## ¿Por qué usar funciones?

Ok, ¿para qué necesitamos crear funciones? Pues lo cierto es... que son fundamentales.

Hasta ahora hemos visto programas que son una simple secuencia de órdenes, las cuales se ejecutan desde el principio hasta el final.

Eso está bien cuando los programas son simples y tienen que hacer pocas cosas, pero cuando el programa tiene que hacer algo más complejo es muy probable que tengas que usar funciones, por varios motivos.

### Motivo 0: divide y vencerás
Los programas tratan de resolver problemas ofreciendo una solución. En ocasiones los problemas pueden ser muy complejos de afrontar. Las funciones te permiten abordad esos problemas por partes. Cada función te puede dar la solución para una parte del problema. Por lo tanto, puedes dividir el problema en muchos pequeños problemas y solucionar cada problema con una función.
Escribir el código en funciones es el primer paso que te permite¡irá diseñar programas más complejos.

### Motivo 1: no repetir el código
Si tu programa tiene que hacer alguna cosa varias veces, tendrías que repetir el código tantas veces como fuera necesario. Imagina que tienes que recibir varios datos del usuario, y que cada vez que lo haces tienes que comprobar que el dato no está vacío:

```python
dato = ""

while dato == "":
	dato = input("Por favor, introduce un dato: ")
	if dato == "":
		print("¡El dato está vacío!)
```

Si solicitas al usuario 3 datos, ¡tendrías que repetir ese código 3 veces! En cambio si creas una función con ese mismo código, solo lo tendrás que escribir una vez y luego podrás usarlo tantas veces como necesites.

Nota: NO repetir el código es una de las reglas más importantes que debe seguir todo buen programador.

### Motivo 2: reutilizar código
Además de no repetir el código, una función nos permite que un mismo código sirva para distintos tipos de datos. ¡Para eso se utilizan los parámetros!

```python
def saludar(saludo, veces):
	for i in range(veces):
		print(saludo)
```
Se le puede llamar con distintos valores:

```python
saludar("Holi", 3)
saludar("Aupa", 1)
```
Sería:

```console
Holi
Holi
Holi
Aupa
```

## Motivo 3: facilitar el mantenimiento
Si el código solo está en un sitio, es más fácil corregirlo, cambiarlo, mejorarlo y mantenerlo en general. Crear un programa desde cero es muy bonito, pero el verdadero trabajo es mantener el código a lo largo del tiempo.
Si tenemos nuestras funciones bien definidas, nos ahorraremos muuuuucho trabajo.

### Motivo 4: permite hacer tests
Quiza seas un poco joven para esto, pero las verdaderas pros como yo testeamos nuestros programas. ¿Qué significa eso? Que escribimos programas cuya única función es comprobar que nuestros programas hacen lo que deben.
Si tu código tiene funciones, podrás escribir tests para comprobar que esas funciones hacen lo que deben.

En realidad, cuando ya eres un experto, lo suyo es que escribas el test antes que la función en si misma!

## Cómo hacer buenas funciones
Cualquiera puede escribir funciones y agrupar el código en pequeñas partes. Pero si quieres escribir funciones como un pro, tienes que procurar lo siguiente:
- Una función debe hacer solo una cosa. Es mejor tener muchas pequeñas funciones que pocas funciones haciendo muchas cosas. Si tu función no cabe en la pantalla o pasa de 24 líneas, quizá debas dividirla en pequeás partes.
- Una función no debería cambiar nada que haya fuera. Si no quieres tener sorpresas, una función no debería liarla dentro del programa.
- Una función debería retornar algo, y ese algo siempre debería ser lo mismo para determinados parámetros.

# Clases

Una clase es una estructura de programación que nos permite representar una entidad con sus propiedades y métodos. Es decir, una clase:
- Tiene propiedades (variables propias)
- Hace cosas (funciones)

Por ejemplo, la siguiente clase representa a un gato muy simple, con una función para maullar:

```python
class Gato:
	def maulla(self):
		print("Miau")
```
Como se puede ver, para definir la clase utilizamos la palabra `class` seguida del nombre de la clase, con la primera letra en mayúscula. Todo lo que vaya dentro de ese bloque será parte de la clase.

Por otro lado, debes tener en cuenta de que **todas** las funciones de una clase deben tener el parámetros `self`, aunque no se use. Ese parámetro se refiere a la propia clase, y se utiliza para referirse a las propiedades y funciones de ella misma, como veremos ahora.

La clase no es más que la definición del gato. Pero para crear un gato en nuestro programa, debemos crear una instancia. Se hace así:

```python
gato = Gato()
gato.maulla()
```
Por pantalla veremos:

```console
Miau
```

## Función constructora
Ese gato hace más bien poco. Vamos a darle una propiedad `nombre`. Además, vamos a crear una función especial que debe llamarse `__init__`.

`__init__` es lo que se conoce como **función constructora**. Esta función se llama cuando se crea un objeto de la clase, y por tanto es el lugar ideal para iniciar las propiedades de la clase:

```python
class Gato:
	def __init__(self, nombre):
		self.nombre = nombre
	
	def maulla(self):
		print("Miau, soy", self.nombre)
```

Ahora, cuando creemos objetos de la clase Gato le pasaremos un nombre y este se quedará como propiedad:

```python
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

## Herencia
La herencia es un mecanismo que tienen las clases para la reutilización de código. Supongamos que queremos hacer una clase que represente a un cachorro de gato. Queremos que haga lo mismo que la clase Gato pero que además ronronee.
La clase cachorro podría heredar de la clase Gato, de la siguiente manera:

```python
class Cachorro(Gato):
	def ronronea(self):
		print("Purrrr")
```
Ahora podemos hacer lo siguiente. Crear un objeto Cachorro, con las mismas propiedades que la clase Gato. De forma automática, heredará la propiedad `nombre` y el método `maulla`:

```python
gatito = Cachorro("Lucifur") 
gatito.ronronea()
gatito.maulla()
```
Se vería como:

```console
Purrrr
Miau, soy Lucifur
```

## Encapsulación

En el ejemplo del gato, se puede hacer acceder a la propiedad nombre de forma directa.
Para eso, en los objetos basta con poner algo así:

```python
objeto.nombrePropiedad
```

El gato tiene una propiedad llamada `nombre`.
```python
miGato = Gato("Pixi")
print(miGato.nombre)  # Pixi
miGato.nombre = "Pixel"
miGato.maulla() # Miau, soy Pixel
```
Acceder a una propiedad de forma tan directa no está mal, pero las buenas programadoras como yo tratamos de encapsular la clase. ¿Qué significa eso? Que no se permite que se pueda acceder o cambiar directamente las propiedades o métodos de la misma. Solo aquello que sea necesario para quienes usen la clase.
Dicho de otra forma, los programadores deben tratar de crear clases que parezcan "cajas negras". En el caso de las propiedades como el nombre, en Python se puede añadir los siguientes métodos:
Un método para devolver el valor de la propiedad nombre, también conocido como "getter":
```python
	@property 
	def nombre ():
		return self._nombre
```

Un método para poder modificar el valor del nombre, también conocido como "setter":
```python
	@nombre.setter
	def nombre (nombre):
		if nombre != "":
			self._nombre = nombre
```

La clase quedaría así:
```python
class Gato:
	def __init__(self, nombre):
		self._nombre = nombre
	
	@property 
	def nombre ():
		return self._nombre
	
	@nombre.setter
	def nombre (nombre):
		if nombre != "":
			self._nombre = nombre

	def maulla(self):
		print("Miau, soy", self.nombre)
```
Observa que la propiedad `nombre` es ahora `_nombre`. Es una manera de expresar que esa propiedad es "privada", y que no se debería acceder a ella desde fuera de la clase.

Ahora cuando usemos la clase `Gato` e intentemos acceder a la propiedad `. nombre`, se hará a través de esas nuevas funciones.
```python
miGato = Gato("Pixi")
print(miGato.nombre)  # llama al método `def nombre ():`
miGato.nombre = "Pixel" # llama al método `def nombre (nombre):`
miGato.maulla() # Miau, soy Pixel
```

¿Qué ventaja puede tener la encapsulación?
Básicamente que desde "fuera" no se pueda manipular la clase sin control. De ahí que sea como una caja negra, como una videoconsola. Si para jugar un juego tuvieras que abrirla y soldar las conexiones a mano probablemente te acabarías cargando la consola. Por eso los aparatos se diseñan como cajas negras, solo te permiten manipularlas desde fuera.

En el caso de la clase Gato, no permitimos que el nombre se pueda cambiar directamente. A través del método "setter" podemos controlar que el nombre que se quiera asignar sea correcto.

## ¿Por qué usar clases?
Las clases nos permiten aplicar una técnica llamada programación orientada a objetos. Es otra estrategia para resolver problemas complejos. 
Con las funciones, dividimos un problema en pequeños problemas. En cambio, con la programación orientada a objetos, lo que tratamos de hacer es dividir el problema en clases. ¿Pero cómo?  representando todo aquello que forma parte del problema utilizando clases.

Imagina que tuvieramos que hacer el programa de un juego de carreras como Mario Kart. Utilizando la programación orientada a objetos podriamos representar los elementos del juego con clases como:
- Personaje, con su nombre y otras propiedades.
- Coche, con sus características de velocidad, resistencia, funciones de aceleración, etc.
- Circuito, con su longitud, sus túneles, sus premios, etc.

# Librerías
Conforme los programas se hacen más y más complejos, es probable que tengamos que definir muchas funciones, o separar el diseño en clases, etc.
Pese a que podríamos tener todo dentro del mismo fichero, no sería la mejor forma de organizar nuestro código. Lo ideal es que separemos cada clase en su propio fichero y cada función o grupo de funciones en su propio fichero.

Una vez organizado el código en ficheros e incluso en carpetas, ya podemos reutilizarlos en otros ficheros. Veamos un ejemplo simple.

Definimos la siguiente función en un fichero llamado `mates.py`:
```python
def sumar (a, b):
	return a + b

def restar (a, b):
	return a - b

def incrementar (a):
	return a - 1
```

Ahora podemos incluir ese fichero en otro programa mediante la orden `import`. Si están en el mismo directorio se puede hacer simplemente:

```python
import mates

valor1 = 5
valor2 = 10

resultado = mates.sumar(valor1, valor2)
print(resultado)  # 15
```

Con las clases se puede hacer exactamente lo mismo. Supongamos que tenemos una clase llamada LectorPantalla en un fichero llamado lector_pantalla.py. Es una clase que nos permite leer datos desde la consola:

```python
class LectorPantalla:
	def leerEntero (self, mensaje = "Introduce un número: "):
		numero = input(mensaje)
		return int(numero)

	def leerTexto (self, mensaje = "Introduce texto: ")
		texto = input(mensaje)
		return texto
```

Ahora podemos reutilizar esa clase en otro fichero, junto con nuestro fichero mates.

```python
import lector_pantalla
import mates

lector = lector_pantalla.LectorPantalla()
valor1 = lector.leerEntero()

print(mates.incrementar(valor1))
```

Por pantalla se podría ver algo así:

```console
Introduce un número: 6
7
```
# Apéndices

## Sobre Python

¿Por qué hemos elegido Python? Por sus muchas virtudes. Es un lenguaje interpretado y con una sintaxis muy sencilla, lo cual lo hace muy sencillo de aprender. No hay que preocuparse (mucho) de los tipos y de las rigideces del lenguaje. La única que debemos tener en cuenta es el de respetar las tabulaciones en cada bloque.

El objetivo no es aprender el lenguaje en si, lo esencial es aprender a programar, y Python facilita esa tarea.

Además, se trata de un lenguaje muy útil, muy extendido y utilizado profesionalmente. Por si eso fuera poco, es muy apreciado por los desarrolladores, lo cual supone una comunidad inmensa de personas aportando código, librerías y ayuda en la web.

Python tiene dos versiones algo diferenciadas, la 2 y la 3. En este libro hemos procurado utillizar la sintaxis y el estilo de la 3, por utilizar la que está más al día.

## Instalando Python localmente

Basta con ir al [site de python](https://www.python.org) y descargar el instalador de la versión 3. La instalación varía un poco en función de tu sistema pero básicamente sería la siguiente:
- Windows: descargar el instalador, ejecutarlo y confirmar cada paso.
- Mac: exactamente igual.
- Linux: probablemente lo tengas instalado de serie o probablemente no necesites que te digan cómo instalarlo.

## Editores de código

Si quieres utilizar un editor para el código, dispones de muchos donde elegir pero destacaremos los siguientes:

- [pycharm](http://www.jetbrains.com/pycharm/) Un editor profesional y gratuíto.
- [atom](https://atom.io/)
- [code](https://vscode.io)
- [pydev](http://pydev.org)
- [sublime](http://www.sublimetext.com)
