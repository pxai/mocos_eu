16.2 Ejercicios propuestos
--------------------------

### 16.2.1 Ejercicio 6.0

Crea una clase llamada Fichero con las siguientes funciones:

- def __init__(self, fichero): recibe como parámetro el fichero a abrir.

- def leer(self): devuelve una cadena con el contenido del fichero.

- def escribir(self, contenido): escribe en el fichero el contenido que se le pasa como parámetro. Luego debes utilizar la clase importándola en otro fichero.

Fichero fichero.py:

```Python
class Fichero:
    def __init__ (self, nombreFichero):
        self._nombreFichero = nombreFichero

    def leer (self):
        fichero = open(self._nombreFichero, "r")
        datos = fichero.read()
        fichero.close()

        return datos

    def escribir (self, contenido):
        fichero = open(self._nombreFichero, "w+")
        fichero.write(contenido)
        fichero.close()
```

Fichero 6.0.py:

```Python
from datetime import date

import fichero

miFichero = fichero.Fichero("6.0.txt")

print("Contenido anterior: ", miFichero.leer())

miFichero.escribir("Contenido cambiado!!! " + str(date.today()))
print("Contenido: ", miFichero.leer())
```

Fichero de texto 3.txt:

Este es el contenido actual.

Resultado:

```console
Contenido anterior:  Contenido cambiado!!! 2020-08-18
Contenido: Contenido cambiado!!! 2020-08-23
```

### 16.2.2 Ejercicio 6.1

Crea una clase llamada Listado con las siguientes funciones:

- def __init__(self, fichero): recibe como parámetro el nombre de un fichero json cuyo contenido debe cargar en una lista llamada _datos que se definirá como atributo. El contenido debe ser una lista de diccionarios con el formato {"id": 1, "nombre": "Juan"}

- def existe(self, nombre): debe devolver True/False si el nombre que se pasa como parámetro existe en la lista.

- def aMinusculas(self): debe pasar todos los nombres de la lista a minúsculas.

- def posicion(self, nombre): debe devolver la posición donde se encuentra ese nombre. Luego debes utilizar la clase importándola en otro fichero.

Fichero listado.py:

```Python
import json

class Listado:
    def __init__ (self, nombreFichero):
        contenido = open(nombreFichero, "r")
        self._datos = json.load(contenido)
        contenido.close()

    def existe (self, nombre):
        for dato in self._datos:
            if dato["nombre"] == nombre:
                return True

        return False

    def aMinusculas (self):
        self._datos = list(map(lambda dato: { "id": dato["id"], "nombre": dato["nombre"].lower() }, self._datos))

    def posicion (self, nombre):
        i = 0
        for dato in self._datos:
            if dato["nombre"] == nombre:
                return i
            i += 1
        return -1

    def print (self):
        for dato in self._datos:
            print(dato)
```

Fichero 6.1.py:

```Python
import listado
miListado = listado.Listado("6.1.json")

if miListado.existe("eugene"):
    print("Existe!")

miListado.aMinusculas()
miListado.print()

if miListado.existe("eugene"):
    print("Existe!")
    print(miListado.posicion('eugene'))
```

Fichero 6.1.json:

```JavaScript
[
    {
        "id": 3,
        "nombre": "Juan"
    },
    {
        "id": 5,
        "nombre": "Eugene"
    },
    {
        "id": 10,
        "nombre": "Paul"
    }
]
```

Resultado:

```console
{'id': 3, 'nombre': 'juan'}
{'id': 5, 'nombre': 'eugene'}
{'id': 10, 'nombre': 'paul'}
Existe!
1
```

### 16.2.3 Ejercicio 6.2

Crea una clase llamada Tareas con las siguientes funciones:

- def __init__(self): debe abrir el fichero llamado tareas.json y cargar en una lista los diccionarios que tendrán el siguiente formato: {id: 1, tarea: "Aprende algo"}. Esa lista será un atributo.

- def crear(self, tarea): genera un nuevo objeto y lo guarda en la lista.

- def eliminar(self, id): elimina una tarea de la lista que tenga ese id.

- def guardar(self): guarda la lista en el fichero tareas.json.

- def mostrar(self): devuelve todas las tareas en un string Luego debes utilizar la clase importándola en otro fichero.

Fichero tareas.py

```Python
import json

class Tareas:
    def __init__ (self):
        fichero = open("tareas.json", "r")
        self._tareas = json.load(fichero)
        fichero.close()

    def crear (self, id, tarea):
        nueva = { "id": id, "tarea": tarea };
        self._tareas.append(nueva)

    def guardar (self):
        fichero = open("tareas.json", "w")
        fichero.write(json.dumps(self._tareas))
        fichero.close()

    def eliminar(self, id):
        self._tareas = list(filter(lambda dato: dato["id"] != id, self._tareas))

    def mostrar (self):
        resultado = ""
        for dato in self._tareas:
            resultado += json.dumps(dato) + "n"

        return resultado
```

Fichero tareas.json:
```JavaScript
 [     {"tarea": "Aprender Go", "id": 3},      {"tarea": "Investigar Rust", "id": 5},      {"tarea": "Dormir más", "id": 10} ]
```

Fichero 6.2.py:

```Python
import tareas
misTareas = tareas.Tareas()

print(misTareas.mostrar(), "n---")

misTareas.crear(2, "Comer")
print(misTareas.mostrar(), "n---")

misTareas.eliminar(2)
print(misTareas.mostrar(), "n---")

misTareas.crear(66, "Leer")
print(misTareas.mostrar(), "n---")
misTareas.guardar()
```

Resultado:

```console
{"tarea": "Aprender Go", "id": 3}
{"tarea": "Investigar Rust", "id": 5}
{"tarea": "Dormir mu00e1s", "id": 10}

---
{"tarea": "Aprender Go", "id": 3}
{"tarea": "Investigar Rust", "id": 5}
{"tarea": "Dormir mu00e1s", "id": 10}
{"tarea": "Comer", "id": 2}

---
{"tarea": "Aprender Go", "id": 3}
{"tarea": "Investigar Rust", "id": 5}
{"tarea": "Dormir mu00e1s", "id": 10}

---
{"tarea": "Aprender Go", "id": 3}
{"tarea": "Investigar Rust", "id": 5}
{"tarea": "Dormir mu00e1s", "id": 10}
{"tarea": "Leer", "id": 66}

---
```

### 16.2.4 Ejercicio 6.3

Crea una clase llamada Jugador que contenga lo siguiente:

- def __init__(self, nombre, dorsal): asigna los parámetros a los atributos _nombre y _dorsal.

- Métodos get/set para nombre y dorsal.

- def info(self): devuelve un string con la información del jugador.

Crea una clase llamada Equipo que contenga lo siguiente:

- def cargar(self): debe abrir un fichero llamado jugadores.json que contendrá una lista de diccionarios de jugador [{nombre: "Pele", dorsal: 10},{…},…]. Y debe crear por cada objeto del fichero una instancia de la clase Jugador y meterla en una lista llamado this._jugadores.

- def mostrar(self): debe mostrar toda la lista de jugadores.

- def fichaje(self, nombre, dorsal): debe introducir un jugador nuevo en la lista, creando una instancia de Jugador. En la clase Equipo tendrás que importar la clase Jugador para poder utilizarla.

Fichero jugador.py:

```Python
class Jugador:
    def __init__ (self, nombre, dorsal):
        self._nombre = nombre
        self._dorsal = dorsal

    @property
    def nombre (self):
        return self._nombre

    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre

    @property
    def dorsal (self):
        return self._dorsal

    @dorsal.setter
    def dorsal (self, dorsal):
        self._dorsal = dorsal

    def toString (self):
        return f"{self._nombre} {self._dorsal}"
```

Fichero equipo.py:

```Python
import json
import jugador

class Equipo:
    def cargar (self):
        contenido = open("./jugadores.json")
        jugadores = json.load(contenido)
        print("Loaded: ", jugadores)
        self._jugadores = []
        for j in jugadores:
            self._jugadores.append(jugador.Jugador(j["nombre"], j["dorsal"]))

    def fichaje (self, nombre, dorsal):
        nuevoFichaje = jugador.Jugador(nombre, dorsal)
        self._jugadores.append(nuevoFichaje)

    def mostrar (self):
        for jugador in self._jugadores:
            print(jugador.toString())
```

Fichero jugadores.json:

```JavaScript
[
    {
        "nombre": "Maradona",
        "dorsal": 10
    },
    {
        "nombre": "Pele",
        "dorsal": 8
    }
]
```

Fichero 6.3.py:

```Python
import equipo
miEquipo = equipo.Equipo()

miEquipo.cargar()
miEquipo.mostrar()
miEquipo.fichaje("Gento", 11)
miEquipo.mostrar()
```

Resultado:

```console
console Loaded:  [{'dorsal': 10, 'nombre': 'Maradona'}, {'dorsal': 8, 'nombre': 'Pele'}]
Maradona 10 Pele 8 Maradona 10 Pele 8 Gento 11
```

# Apéndices

17         ![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.023.png)Sobre Python
===========================================================================================

¿Por qué hemos elegido Python? Por sus muchas virtudes. Es un lenguaje interpretado y con una sintaxis muy sencilla, lo cual lo hace muy sencillo de aprender. No hay que preocuparse (mucho) de los tipos y de las rigideces del lenguaje. La única que debemos tener en cuenta es el de respetar las tabulaciones en cada bloque.

El objetivo no es aprender el lenguaje en si, lo esencial es aprender a programar, y Python facilita esa tarea.

Además, se trata de un lenguaje muy útil, muy extendido y utilizado profesionalmente. Por si eso fuera poco, es muy apreciado por los desarrolladores, lo cual supone una comunidad inmensa de personas aportando código, librerías y ayuda en la web.

Python tiene dos versiones algo diferenciadas, la 2 y la 3. En este libro hemos procurado utilizar la sintaxis y el estilo de la 3, por utilizar la que está más al día y porque la 2 está en desuso.

17.1 Instalando Python localmente
---------------------------------

Basta con ir al [site de python](https://www.python.org) (https://python.org) y descargar el instalador de la versión 3. La instalación varía un poco en función de tu sistema pero básicamente sería la siguiente:

- Windows: descargar el instalador, ejecutarlo y confirmar cada paso.

- Mac: exactamente igual.

- Linux: probablemente lo tengas instalado de serie o probablemente no necesites que te digan cómo instalarlo ;)

17.2 Editores de código
-----------------------

Si quieres utilizar un editor para el código, dispones de muchos donde elegir pero destacaremos los siguientes:

- [pycharm](http://www.jetbrains.com/pycharm/) Un editor profesional y gratuíto.

- [atom](https://atom.io/) Editor ligero de Github.

- [code](https://vscode.io) Editor ligero de Microsoft.

- [pydev](http://pydev.org)

- [sublime](http://www.sublimetext.com) Editor ligero.

17.3 Test unitarios
-------------------

Los test unitarios son programas que comprueban que las funciones están bien hechas. Básicamente son programas que ejecutan las funciones y comprueban que el resultado que tienen es el correcto. Existen diferentes librerías para hacer tests, aunque en Python existe unittest por defecto, por tanto no hace falta instalar nada.

Supongamos que tenemos la siguiente clase que representa una calculadora:

```Python
class Calculadora:
    def sumar (self, a, b):
        return a + b
   
    def restar (self, a, b):
        return a - b
   
    def multiplicar (self, a, b):
        return a * b
   
    def dividir (self, a, b):
        return a / b
```

Para hacer los test unitarios de esa clase, bastaría con crear esta otra clase, la cual hereda de una clase de testeo de la librería unittest. También tenemos que importar la propia clase calculadora ya que la tenemos que poner a prueba.

Cada función de la clase hace una comprobación de cada función de calculadora. Se pueden hacer tantos tests como creas conveniente para probar que las funciones hacen lo que deben. Como puedes ver, cada test básicamente ejecuta una función y comprueba que el resultado es el esperado con assertEqual:

```Python
    def test_sumar(self):
        c = calculadora.Calculadora()
        self.assertEqual(c.sumar(40, 2), 42)
```

Fichero calculadora.test.py:

```Python
import unittest
import calculadora

class TestStringMethods(unittest.TestCase):
    def test_sumar(self):
        c = calculadora.Calculadora()
        self.assertEqual(c.sumar(40, 2), 42)

    def test_restar(self):
        c = calculadora.Calculadora()
        self.assertEqual(c.restar(40, 2), 38)

    def test_multiplicar(self):
        c = calculadora.Calculadora()
        self.assertEqual(c.multiplicar(40, 2), 80)

    def test_dividir(self):
        c = calculadora.Calculadora()
        self.assertEqual(c.dividir(40, 2), 20)

if __name__ == '__main__':
    unittest.main()
```

Ahora basta con ejecutar el fichero de tests y veremos lo siguiente:

```console
python3 calculadora.test.py

....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

17.4 Iniciando un proyecto Python localmente
--------------------------------------------

Una forma recomendada de iniciar un proyecto python sería utilizar el paquete virtualenv, el cual instalaremos con el gestor de paquetes pip3. virtualenv crea una carpeta de proyecto que puede funcionar independientemente de nuestro sistema. Eso hace que el proyecto sea más flexible y más fácil de portar a otros ordenadores.

Los siguientes comandos deberás escribirlos en la consola del sistema.

```console
pip3 install virtualenv
 

Defaulting to user installation because normal site-packages is not writeable
Collecting virtualenv
  Downloading virtualenv-20.0.31-py2.py3-none-any.whl (4.9 MB)
     |████████████████████████████████| 4.9 MB 447 kB/s
Collecting distlib<1,>=0.3.1
...
```

Con virtualenv ya podemos crear un nuevo proyecto:

```console
virtualenv proyecto
```

Lo cual creará una carpeta llamada proyecto. A continuación debemos activar el entorno virtual del proyecto ejecutando:

```console
source proyecto/bin/activate
```

Ahora ya podemos añadir código fuente o instalar dependencias. Para ello conviene crear un fichero de texto llamado requirements.txt que debe tener el siguiente formato:

```console
# Para instalar una versión concreta 
# nombre_paquete==version

# Para instalar una versión igual o superior
# nombre_paquete>=version

# Para instalar la versión más reciente
# nombre_paquete
```

Por ejemplo, si queremos instalar pygame y un paquete de testing podríamos poner:

```console
pygame==1.9.6
unittest
```

Y luego podríamos instalar ese y otros paquetes que ahí indiquemos con el comando:

```console
source bin/activate
pip3 install -r requirements.txt
```

Otra opción es instalar los paquetes necesarios con pip3:

```console
pip3 install pygame
```

Comprobamos que está instalado:

```console
pip3 list


Package    Version
---------- -------
pip        20.2.2
pygame     1.9.6
setuptools 49.6.0
wheel      0.35.1
```

Y mediante freeze lo guardamos en el fichero requirements.txt:

```console
pip3 freeze > requirements.txt
```

Ahora ya podemos crear un fichero que utilice pygame:

```Python
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
```

Ejecutaríamos el juego así:

```console
python3 game.py
```

Y para terminar el entorno virtual de Python, bastaría con hacer:

```console
deactivate
```