   @page Section1 { size:432.05pt 432.05pt; margin:28.35pt 42.55pt 36pt } div.Section1 { page:Section1 }

### 3.1.1    ¡Te toca! Ejercicio 0.0

Escribe un programa que muestre por pantalla tu nombre.

```Python
print("Hola soy Ada")
```

Resultado:

```console
Hola soy Ada
```

¡OJO!

En el lenguaje Python es muy importante que no utilices tabulaciones o espacios al principio de la línea (salvo que utilices bloques que veremos en los siguientes capítulos). Esto, daría un error:

```Python
   print("¡Hola mundo!")
```

3.2  Comentarios
----------------

En un programa, se pueden poner comentarios. Se trata de texto que no se ejecuta y que el ordenador ignora completamente. ¿para qué se utiliza? Generalmente los comentarios se utilizan para explicar determinadas partes del programa.

```Python
# Este programa dice Hola
print("Hola")
```

Python ignora el comentario y mostrará Hola por pantalla. También se pueden hacer comentarios de varias líneas:

```Python
"""
Este es un programa Python
creado por Ada
y revisado por Neko
"""
```

A veces, los comentarios se utilizan de manera temporal para "desactivar" una parte del código que no queremos que se ejecute.

Nota:

En general tienes que evitar los comentarios. Un buen programador tiene que intentar escribir programas tan fáciles de entender que no necesiten comentario alguno.

4       Variables
=================

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.009.jpeg)

Las variables sirven para guardar datos. Los programas de ordenador se dedican, básicamente, a manejar datos para solucionar un problema y ofrecer un resultado. En todo ese proceso es necesario guardar datos, y para eso se utilizan las variables. Las variables son como contenedores de datos. En cierto modo es como los vasos, platos, fuentes que se utilizan para cocinar: contienen algo, se trabajo con ello, se mezcla, se procesa y se consigue un resultado: con un poco de suerte algo rico.

Para definir una variable en python basta con indicar su nombre y darla algún valor. Por ejemplo:

```Python
nombre = "Ada"
```

Acabamos de crear una variable que contiene el valor "Ada". "Ada" es un dato, y es de tipo texto. Ahora podemos mostrar el valor de esa variable por la pantalla:

```Python
print(nombre)
```

Que por pantalla sería:

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

También se puede mostrar el contenido de una variable como parte del mensaje. Existen varias opciones que veremos a continuación.

4.1  Mostrar variables por pantalla
-----------------------------------

### 4.1.1    Separar por comas

Basta con intercalar las variables y el texto con comas:

```Python
nombre = "Bug"
edad = 10
print("Hola, me llamo", nombre)
print("Soy", nombre, "tengo", edad, "años")
```

Que por pantalla sería:

```console
Hola, me llamo Bug
Soy Bug tengo 10 años
```

### 4.1.2    ¡Ahora tú! Ejercicio 0.1

Crea dos variables nombre y edad y muestra su valor por pantalla.

```Python
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

### 4.1.3    String de formato

Otra forma de mostrar varias variables es con un mensaje que precedido de la letra f y las variables entre llaves:

```Python
nombre = "Bug"
edad = 10
print(f"Hola, me llamo {nombre}")
print(f"Soy {nombre} tengo {edad} años")
```

Que por pantalla sería:

```console
Hola, me llamo Bug
Soy Bug tengo 10 años
```

¡OJO!

Ésta opción solo está disponible desde Python 3.6

### 4.1.4    Sustitución de porcentaje

Otra alternativa para mostrar variables por pantalla: se crea un mensaje donde los elementos %s son sustituidos por variables.

```Python
print("Hola, me llamo %s" % nombre)
```

Que por pantalla sería:

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

5       Tipos de datos
======================

¡Datos!

Es la materia prima con la que trabajan los programas. Son el elemento que nuestros programas transforman. Un programa recibe datos, los transforma y los devuelve como un resultado. Los datos pueden ser de distinto tipo, según lo que nuestro programa tenga que hacer. Pueden ser números, puedes ser palabras o textos, pueden incluso ser nulos o vacíos. Para guardar los datos, generalmente usamos variables. Si comparamos la programación con la cocina, entonces el azúcar, la harina y los huevos serían datos, los recipientes serían variables: la tarta sería otro dato, el resultado y la receta sería el programa. ¿Cómo sabe Python que tipo de dato maneja? No hace falta indicárselo como en otros lenguajes. Por eso es un lenguaje más simple y flexible. Aunque tampoco podremos hacer lo que nos de la gana con los datos.

A continuación, vamos a ver los tipos básicos de datos.

5.1  Números
------------

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.010.jpeg)

Se trata de todos los tipos de números:

*   Enteros: 1, 2, 3, 4,...

```Python
contador = 10
edad = 12
```

*   Con decimales: Los números con decimales se expresan utilizando un . para separar la parte entera de la decimal, como 4.5 o 3.1415. Es probable que en clase de mates utilices una coma para separar las decimales, pero en programación se usa el formato inglés y debemos usar un ..

```Python
peso = 34.67
precio = 242.9943
```

•            Negativos: Los números menores que 0 se expresan con un guión por delante: -4, -5, -3.1415,...

```Python
nota = -5
temperaturaEnMarte = -50.676
```

5.2  Texto
----------

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.011.jpeg)

El texto, también llamados cadenas o strings son cualquier conjunto de palabras entre comillas dobles o simples.

```Python
nombre = "Ada"
frase = ""
palabras = 'Voy a trabajar'
novia = 'Solo quiero que seamos "amigos"'
```

En el caso del texto, podemos meter una serie de caracteres especiales que nos permiten efectos interesantes. Esos caracteres se escriben con una contra-barra o backslash por delante:

•            Salto de linea Esto añade un salto de línea al texto si este se muestra por pantalla:

```Python
frase = "Hola,\n qué tal"
```

se mostrará así:

```console
Hola,
qué tal
```

También se puede definir un texto de varias líneas así:

```Python
cancion = """Era un domingo
a la tarde
fui a los coches
de choque"""
```

•            Tabulaciones Esto añade una tabulación (varios espacios) al texto si este se muestra por pantalla:

```Python
frase = "NombretApellidotEdad"
```

se mostrará así:

```console
Nombre  Apellido   
```

Otros caracteres especiales:

•             Para mostrar la contra-barra en un texto.

•            " Para mostrar una comilla doble en un texto.

•            ' Para mostrar una comilla simple en un texto.

•            a Para hacer sonar un pitido.

5.3  Booleanos
--------------

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.012.jpeg)

El tipo booleano solo puede tener dos valores posibles: True o False, es decir verdadero o false. Se trata de un tipo de dato fundamental en programación ya que se utiliza para tomar decisiones.

```Python
terminado = False
esMayor = True
pythonMola = True
```

5.4  Listas
-----------

Las listas son conjuntos de datos, que se definen de la siguiente manera:

```Python
amigas = ["Ada", "Miranda", "Ruby"]
```

Pueden ser de cualquier tipo, pero lo normal es que todos los elementos de una lista sean del mismo tipo:

```Python
enemigas = []  # lista vacía
edades = [12, 16, 30, 0, 22, 1, 1, 12]
verdades = [True, False, False, True]
```

Para poder referirnos a un valor concreto de la lista, tenemos que indicar la posición del elemento de la lista que nos interesa, empezando desde 0:

```Python
nombres = ["Ada", "Neko", "Bug"]
print(nombres[0])  # "Ada"
```

En el caso de la lista nombres, las posiciones posibles serán 0, 1 y 2. ¡Pero ojo! si pasas una posición demasiado grande, el programa terminará con error:

```Python
nombres = ["Ada", "Neko", "Bug"]
print(nombres[4])  # ¡ERROR!
```

Volveremos sobre las listas y otras estructuras más adelante.

5.5  None
---------

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.013.jpeg)

Aunque suene un poco raro, en los programas a veces hay que tratar con algo que representa el vacío, la nada. Existe una palabra que nos permite representar la nada en Python, y esa es: None

```console
valorInicial = None
dato = None
```

En realidad no se suele utilizar para crear variables. None representa un valor en situaciones especiales. Por ejemplo, si se trata de sacar información de un sitio en el que no hay nada como un fichero, o un dato que el usuario no nos da.