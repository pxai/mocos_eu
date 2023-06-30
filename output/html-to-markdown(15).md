### 10.4.1                       Ejercicio 3.3

Define un diccionario llamado telefonos donde guardarás los teléfonos de un par de amigos. La clave será el nombre del amigo y el valor el número de teléfono.

```Python
telefonos = {"Ada": 666555333, "Bug": 111000111 }


print(telefonos)

for nombre in telefonos.keys():
    print(nombre, telefonos[nombre])
```

Resultado:

```console
{'Bug': 111000111, 'Ada': 666555333}
Bug 111000111
Ada 666555333
```

Para añadir nuevos elementos, se puede asignar un nuevo valor:

```Python
edades = {"Ada": 14, "Bug": 10, "Neko": 2}

print(edades)  # {'Bug': 10, 'Neko': 2, 'Ada': 14}

edades["Miranda"] = 23;

print(edades) # {'Bug': 10, 'Neko': 2, 'Ada': 14, 'Miranda': 23}

del edades["Bug"]

print(edades) # {'Neko': 2, 'Ada': 14, 'Miranda': 23}

for nombre in edades.keys():
    print(nombre, edades[nombre])
```

### 10.4.2                       Ejercicio 3.4

Utiliza el diccionario telefonos del ejercicio anterior. Solicita al usuario datos para meter una nueva entrada en el diccionario: tendrás que pedir un nombre y un teléfono y luego añadirlo al diccionario. Al finalizar, muestra todos los elementos del diccionario.

```Python
telefonos = {"Ada": 666555333, "Bug": 111000111 }

nombre = input("Introduce un nombre: ")
telefono = input("Introduce un número: ")

telefonos[nombre] = int(telefono)

for nombre in telefonos.keys():
    print(nombre, telefonos[nombre])
```

Resultado:

```console
Introduce un nombre: Neko
Introduce un número: 333222000
Ada 666555333
Neko 333222000
Bug 111000111
```

Podemos eliminar valores del diccionario con la función del:

```Python
edades = {"Ada": 14, "Bug": 10, "Neko": 2}
print(edades)  # {'Bug': 10, 'Neko': 2, 'Ada': 14}
del edades["Bug"]
print(edades) # {'Neko': 2, 'Ada': 14}
```

¿Y si queremos recorrer todos los valores del diccionario? No hay problema, pero tendremos que utilizar una función que nos devuelva todas las claves del diccionario: keys(). Sería así:

```Python
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

### 10.4.3 Ejercicio 3.5

Utiliza el diccionario telefonos del ejercicio anterior. Solicita al usuario un nombre, y luego elimina ese elemento del diccionario. Al finalizar, muestra todos los elementos del diccionario.

```Python
telefonos = {"Ada": 666555333, "Bug": 111000111 }

nombre = input("Introduce un nombre: ")

del telefonos[nombre]

for nombre in telefonos.keys():
    print(nombre, telefonos[nombre])
```

Resultado:

```Python
Introduce un nombre: Bug
Ada 666555333
```

Nota:

En otros lenguajes, a los diccionarios se les llama hash o hashtables.

10.5 Estructuras de datos combinadas
------------------------------------

¡Las estructuras básicas como listas y diccionarios pueden contener valores que también sean listas y diccionarios!

Se pueden crear estructuras de datos anidadas, tan complejas como necesites. Por ejemplo, supongamos que quieres representar los datos de un amigo con el siguiente diccionario:

```Python
amigo =  {"nombre": "Neko", "edad": 2}
```

¿Y si quieres tener una estructura de datos que contenga varios amigos? En ese caso, puedes hacer una lista de diccionarios:

```Python
amigos = [
    {"nombre": "Neko", "edad": 2},
    {"nombre": "Bug", "edad": 10},
    {"nombre": "Ada", "edad": 14}
]
print(amigos[1]) # {"nombre": "Bug", "edad": 10}
print(amigos[2]["nombre"]) # Ada
```

### 10.5.1 Ejercicio 3.6

Escribe un programa que defina una lista de diccionarios llamada cliente que contenga las claves: nombre, email y edad. El programa debe recorrer la lista y mostrar el nombre y edad de cada cliente.

```Python
clientes = [
    {
        "nombre": "Juan",
        "email": "jj@terra.com",
        "edad": 39
    },
    {
        "nombre": "Pedro",
        "email": "pp@ozu.es",
        "edad": 42
    },
    {
        "nombre": "Ana",
        "email": "ana@ole.com",
        "edad": 37
    }
]

for cliente in clientes:
    print(f"{cliente['nombre']} {cliente['edad']}")
```

Resultado:

```console
Juan 39
Pedro 42
Ana 37
```

¿Y si quieres una estructura de datos que contenga el estado de un juego, con sus personajes y sus objetos? Podría hacer un diccionario anidado, donde la clave es el nombre del personaje:

```Python
pantalla = {
    "Mario": { "vida": 10, "objetos": ["seta", "estrella"]},
    "Luigi": { "vida": 7, "objetos": []},
    "Toad": { "vida": 15, "objetos": ["seta"]},
}

print(pantalla["Luigi"]["vida"])  # 7
```

Pero ¿Cómo sé que tipo de estructura debo diseñar? Depende de cómo la vayas a usar. A veces necesitarás recorrer todos, otras veces necesitarás acceder a un elemento concreto,... según lo que requiera tu programa tendrás que diseñar una estructura concreta.

11         Textos
=================

El tipo de dato texto, también llamado cadena o string, es fundamental en los programas. Por eso dispone de muchas utilidades para facilitarnos el manejo de este tipo de datos. A continuación, veremos algunas funciones útiles para los textos, pero antes, conviene revelar algo sobre el texto:

11.1 Los textos son listas
--------------------------

Efectivamente, para el ordenador, un texto es como una lista. Una lista o cadena de letras, y la podemos tratar como tal:

```Python
texto = "Hola soy Ada"
texto[1] # "o"
```

Incluso podemos recorrer el texto como si fuera una lista:

```Python
texto = "Ada"

for caracter in texto:
    print(caracter)
```

La salida sería:

```console
A
d
a
```

También podemos saber la longitud de un texto con la función len():

```Python
texto = "Neko maulla"
len(texto)  # 11
```

Pero si duda, lo más interesante es que podemos extraer la parte que queramos del texto indicando el inicio y el final:

```Python
texto = "Python mola"
texto[0:6]  # "Python"
texto[7:12]  # "mola"
```

También se pueden sacar los primeros caracteres

```Python
texto = "Python mola"
texto[:6] # "Python"
```

O los últimos caracteres

```Python
texto = "Python mola"
texto[-4:] # "mola"
```

O simplemente el último de todos:

```Python
texto = "Python mola"
texto[-1] # "a"
```

11.2 Mayúsculas/Minúsculas
--------------------------

Tenemos una serie de funciones para convertir texto a mayúsculas o minúsculas:

```Python
texto = "Profesora Ada"
texto.upper() # PROFESORA ADA
texto.lower() # Profesora Ada
```

También tenemos una función llamada title(), la cual cambia cada palabra dentro de un texto, poniendo la primera letra en mayúsculas.

```Python
texto = "esto es una frase"
texto.title() # Esto Es Una Frase
```

11.3 split: de texto a lista
----------------------------

split es una interesante función que parte un texto en cachos y lo convierte en una lista:

```Python
texto = "ven conmigo si quieres vivir"
palabras = texto.split() # ["ven", "conmigo", "si", "quieres", "vivir"]
```

Por defecto el corte del split se hace en los espacios del texto. Pero se puede indicar cualquier otro separador, por ejemplo el punto y coma ;:

```Python
texto = "Ada;Neko;Bug"
nombres = texto.split(";") # ["Ada", "Neko", "Bug" ]
```

11.4 Búsquedas
--------------

En ocasiones nos interesará buscar una palabra dentro de un texto. Para eso podemos usar la función find. En caso de encontrar la palabra, muestra la posición en la que se empieza esa palabra. Si no lo encuentra, devuelve -1.

```Python
palabras = "La mejor profesora es Ada, sin duda"
encontrado = palabras.find("mejor")  # 3
encontrado = palabras.find("Ada")  # 22
noEncontrado = palabras.find("xxx")  # -1
```

Si queremos saber si un texto empieza de alguna manera, se puede usar startswith()

```Python
palabras = "Python es un buen lenguaje"
empieza = palabras.startswith("Py") # True
empieza = palabras.startswith("es") # False
```

Mientras que si queremos saber si un texto acaba de una manera, se puede usar endswith():

```Python
palabras = "Python es un buen lenguaje"
acaba = palabras.endswith("aje") # True
acaba = palabras.startswith("ajes") # False
```

11.5 Eliminar sobrantes
-----------------------

Los textos pueden empezar o terminar con espacios en blanco u otros caracteres que quizá nos interese eliminar, como los saltos de línea. Para quitar esas partes sobrantes de un texto, se pueden usar las siguientes funciones.

Con lstrip() se eliminan los espacios al inicio del texto:

```Python
texto = "  Tengo espacios      "
limpio = texto.lstrip() # "Tengo espacios      "
```

Con rstrip() se eliminan los espacios al inicio del texto:

```Python
texto = "  Tengo espacios      "
limpio = texto.rstrip()  # "  Tengo espacios"
```

Y con strip() quitamos los espacios de ambos lados:

```Python
texto = "  Tengo espacios      "
limpio = texto.strip()  # "Tengo espacios"
```

Por defecto se quitan espacios, pero podemos indicar cualquier texto que queramos quitar:

```Python
texto = "--Texto con guión"
limpio = texto.lstrip("-") # "Texto con guión"
```

También los saltos de línea cuando leemos texto desde un fichero o desde la consola:

```Python
texto = "Esto tiene un salto de línean"
limpio = texto.rstrip("n")
```