13.8 Ejercicios propuestos
--------------------------

### 13.8.1 Ejercicio 5.0

Escribe un programa que defina una clase llamada Instrumento. El constructor debe tener los parámetros nombre y tipo, que se asignarán a los atributos  _nombre y  _tipo respectivamente. Además debes añadir una función llamada tocar que simplemente sacará un mensaje y otra llamada info que devolver un texto con la información de los atributos. Crea una instancia de la clase y llama a sus funciones.

```Python
class Instrumento:
    def  _ _init _ _(self, nombre, tipo):
        self. _nombre = nombre
        self. _tipo = tipo

    def tocar (self):
        print("Tocando ", self. _nombre)

    def info (self):
        return f"{self. _nombre} {self. _tipo}"


miGuitarra = Instrumento("Guitarra", "cuerda")
miGuitarra.tocar()
print(miGuitarra.info())
```

Resultado:

```console
Tocando Guitarra
Guitarra cuerda
```

### 13.8.2 Ejercicio 5.1

Escribe un programa que defina una clase llamada NombreFormateado, con un constructor que recibe un nombre y un apellido y una función llamada formatear que debe devolver el nombre y el apellido en este formato: "Nombre Apellido", es decir con la primera letra en mayúscula, el resto en minúscula y separados por comas. Crea las funciones auxiliares que consideres oportunas.

```Python
class NombreFormateado:
    def  _ _init _ _(self, nombre, apellido):
        self. _nombre = nombre
        self. _apellido = apellido

    def formatear (self):
        return self. _corregir(self. _nombre) + " " + self. _corregir(self. _apellido)

    def  _corregir (self, cadena):
        return self. _primero(cadena) + self. _resto(cadena)

    def  _primero (self, cadena):
        return cadena [0 ].upper()

    def  _resto (self, cadena):
        return cadena [1:len(cadena) ].lower()


formateador = NombreFormateado("JUAN", "PÉREZ")
print(formateador.formatear())
```

Resultado:

```console
Juan Pérez
```

### 13.8.3 Ejercicio 5.2

Escribe un programa que defina una clase llamada Sumador, la cual se instancia con dos números. Incluye funciones get y set para ambos, y debes controlar que si se les intenta asignar un valor negativo se asigne 0. Además tendrán la función sumar que devolverá la suma de ambos números.

```Python
class Sumador:
    def  _ _init _ _(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    @property
    def valor1 (self):
        return self. _valor1

    @valor1.setter
    def valor1 (self, valor1):
        if valor1 > 0:
            self. _valor1 = valor1
        else:
            self. _valor1 = 0

    @property
    def valor2 (self):
        return self. _valor2

    @valor2.setter
    def valor2 (self, valor2):
        if valor2 > 0:
            self. _valor2 = valor2
        else:
            self. _valor2 = 0

    def sumar (self):
        return self. _valor1 + self. _valor2


sumador = Sumador(28, 14)
print(sumador.sumar())

sumador.valor1 = 600
sumador.valor2 = 66
print(sumador.sumar())
```

Resultado:

```console
42
666
```

### 13.8.4 Ejercicio 5.3

Crea un programa con una clase llamada Moneda. La clase debe tener un constructor vacío y una única función llamado tirar cuyo resultado debe ser un string elegido al azar entre "cara" o "cruz". Crea una instancia de la clase para probarla.

```Python
import random

def aleatorio (max):
    return random.randint(0, max)

class Moneda:
    def tirar (self):
        lados =  ["cara", "cruz" ]
        numero = aleatorio(1)

        return lados [numero ]

moneda = Moneda()

for i in range(10):
    print(moneda.tirar())
```

Resultado:

```console
cara
cara
cruz
cruz
cruz
...
```

### 13.8.5 Ejercicio 5.4

Crea un programa con una clase llamada Dado para simular el comportamiento de un dado de N caras. Crea una instancia de la clase para probarla.

 - ​constructor def  _ _init _ _(self, lados, admiteCero=False): con el atributo lados: atributo que guarda el número de caras y el atributo admiteCero = False: atributo que nos dice si el dado puede devolver el valor 0. Por defecto vale False.

 - ​setter def lados (self, lados) : función setter con parámetro, establece el atributo lados.

 - ​setter def admiteCero (self, lados, admiteCero): función con parámetros, establece los dos atributos.

 - ​def tirar (self): función que simula el lanzamiento del dado y retorna un el resultado. Debe tener en cuenta al atributo admiteCero. Crea instancias que genere un dado de 6 caras, un dado de 10 caras y un dado de 20 que permita ceros, y haz 100 lanzamientos de cada uno:

```Python
import random

def aleatorio (max):
    return random.randint(0, max)

class Dado:
    def  _ _init _ _(self, lados = 6, admiteCero = False):
        self. _lados = lados
        self. _admiteCero = admiteCero

    @property
    def lados (self):
        return self. _lados

    @lados.setter
    def lados (self, lados):
        self. _lados = lados

    @property
    def admiteCero (self):
        return self. _admiteCero

    @admiteCero.setter
    def admiteCero (self, admiteCero):
        self. _admiteCero = admiteCero

    def tirar (self):
        numero =  aleatorio(self. _lados)

        if not self. _admiteCero:
            numero = numero + 1

        return numero


dado = Dado()
for i in range(10):
    print(dado.tirar())
```

Resultado:

```console
4
3
2
4
3
...
```

### 13.8.6 Ejercicio 5.5

Crea un programa que contenga dos clases:

*   Clase Jugador, que contiene los atributos nombre, puesto y dorsal. También tiene un constructor con todos esos parámetros y una función llamada informe que retorne todos los atributos.
*   Clase Equipo, que contiene los atributos nombre, fundacion, presupuesto y una lista para guardar instancias de la clase Jugador. Debe tener un constructor con los atributos nombre, fundacion, presupuesto, sus get/set, una función informe y otras dos funciones:

*   def fichar(self, jugador) para añadir jugadores a la lista.
*   def mostrarJugadores(self), para devolver una cadena con todos los datos de los jugadores Además, añade el código necesario para crear dos jugadores y un equipo, al que añadirás los jugadores y los mostrarás.

```Python
class Jugador:
    def  _ _init _ _(self, nombre, posicion, dorsal):
        self. _nombre = nombre
        self. _posicion = posicion
        self. _dorsal = dorsal

    def informe (self):
        return f"{self. _nombre} {self. _posicion} {self. _dorsal}"


class Equipo:
    def  _ _init _ _ (self, nombre, fundacion, presupuesto):
        self. _nombre = nombre
        self. _fundacion = fundacion
        self. _presupuesto = presupuesto
        self. _jugadores =  [ ]

    def ficharJugador (self, jugador):
        self. _jugadores.append(jugador)

    def mostrarJugadores (self):
        for jugador in self. _jugadores:
            print(jugador.informe())


jugador1 = Jugador("Maradona", "Delantero", 10)
jugador2 = Jugador("Beckenbauer", "Defensa", 4)

print(jugador1.informe())

equipo = Equipo("New Team", 1983, 39944.45)
equipo.ficharJugador(jugador1)
equipo.ficharJugador(jugador2)

equipo.mostrarJugadores()
```

Resultado:

```console
Maradona Delantero 10
Beckenbauer Defensa 4
```

### 13.8.7 Ejercicio 5.6

Crea un programa que incluya una serie de clases.

 - 1 - Clase Dispositivo: tiene los atributos nombre, marca y precio. Un constructor usando los atributos, los set y get y una función toString mostrando los atributos.

 - 2 - Clase Movil: es una subclase de Dispositivo, hay que añadir el atributo numero. Crea el constructor y el método def toString (self) aprovechando los de la superclase. Añade la función def llamar (self, numero), que saque por pantalla una cadena diciendo "llamando numero".

 - 3 - Clase Ordenador: es una subclase de Dispositivo, hay que añadir el atributo procesador. Crea el constructor y la función def toString (self) aprovechando los de la superclase Además, añade el código necesario para crear un móvil y un ordenador y los muestras.

```Python
class Dispositivo:
    def  _ _init _ _(self, nombre, precio):
        self. _nombre = nombre
        self. _precio = precio

    def get _nombre ():
        return self. _nombre

    def set _nombre (nombre):
        self. _nombre = nombre

    def get _precio ():
        return self. _precio

    def set _precio (precio):
        self. _precio = precio

    def toString (self):
        return f"{self. _nombre} {self. _precio}";


class Movil(Dispositivo):
    def  _ _init _ _(self, nombre, precio, numero):
        super(). _ _init _ _(nombre, precio)
        self. _numero = numero

    @property
    def numero (self):
        return self. _numero

    @numero.setter
    def numero (self, numero):
        self. _numero = numero

    def toString (self):
        return f"{super().toString()} {self. _numero}"

    def llamar (numero):
        print("Llamando a", numero)


class Ordenador(Dispositivo):
    def  _ _init _ _(self, nombre, precio, procesador):
        super(). _ _init _ _(nombre, precio)
        self. _procesador = procesador

    @property
    def procesador (self):
        return self. _procesador

    @procesador.setter
    def procesador (self, procesador):
        self. _procesador = procesador

    def toString (self):
        return f"{super().toString()} {self. _procesador}"


ordenador = Ordenador("Dell", 4553.4, "Lentium 4")
telefono = Movil("Chanmhung", 434.4, 665745345)

print("Ordenador: ", ordenador.toString())
print("Teléfono: ", telefono.toString())
```

Resultado:

```console
Ordenador Dell 4553.4 Lentium 4
Teléfono Chanmhung 434.4 665745345
```

### 13.8.8 Ejercicio 5.7

Vamos a crear el proyecto Caperucita en el que la protagonista gestiona una Cesta de comida. La comida será de varios tipos. Estas son las clases que se deben hacer,

 - 1 - Clase Comida: tiene los atributos nombre y peso. Un constructor usando los atributos, los set y get y una función toString mostrando los atributos.

 - 2 - Clase Fruta: es una subclase de Comida, y hay que añadir el atributo vitamina. Crea el constructor y la función toString aprovechando los de la superclase.

 - 3 - Clase Caramelo: es una subclase de Comida y hay que añadir el atributo calorias. Crea el constructor y la funciñon toString aprovechando los de la superclase.

 - 4 - Clase Cesta, tiene un atributo llamado alimentos que es un array de elementos tipo Comida (Fruta o Caramelo). Se inicia en el constructor. Tiene tres funciones:

*   def meterComida(self, comida) para meter una comida en la cesta,
*   def pesoTotal(self) devuelve el peso total de la comida de la cesta.
*   def toString(self) para mostrar toda la comida de la cesta. Además, añade el código necesario para crear instancias de Fruta, Caramelo y añádelos a la instancia de Cesta.

```Python
class Comida:
    def  _ _init _ _(self, nombre, peso):
        self. _nombre = nombre
        self. _peso = peso

    @property
    def nombre (self):
        return self. _nombre

    @nombre.setter
    def nombre (self, nombre):
        self. _nombre = nombre

    @property
    def peso (self):
        return self. _peso

    @peso.setter
    def peso (self, peso):
        self. _peso = peso

    def toString (self):
        return f"{self. _nombre} {self. _peso}"


class Fruta(Comida):
    def  _ _init _ _(self, nombre, peso, vitamina):
        super(). _ _init _ _(nombre, peso)
        self. _vitamina = vitamina

    @property
    def vitamina (self):
        return self. _vitamina

    @vitamina.setter
    def vitamina (self, vitamina):
        self. _vitamina = vitamina

    def toString (self):
        return f"{super().toString()} {self. _vitamina}"


class Caramelo(Comida):
    def  _ _init _ _(self, nombre, peso, calorias):
        super(). _ _init _ _(nombre, peso)
        self. _calorias = calorias

    @property
    def calorias (self):
        return self. _calorias

    @calorias.setter
    def calorias (self, alorias):
        self. _calorias = calorias

    def toString (self):
        return f"{super().toString()} {self. _calorias}"


class Cesta:
    def  _ _init _ _(self):
        self. _alimentos =  [ ]

    def meterComida (self, comida):
        self. _alimentos.append(comida)

    def pesoTotal (self):
        total = 0
        for alimento in self. _alimentos:
            total += alimento.peso

        return total

    def toString (self):
        info = ""
        for alimento in self. _alimentos:
            info = info + alimento.toString() + "  n"

        return info


chicle = Caramelo("Cheiw", 0.2, 100)
gominola = Caramelo("Fresa", 0.3, 210)
pera = Fruta("Pera", 0.1, "B")
manzana = Fruta("Manzana", 0.15, "A")

cesta = Cesta()
cesta.meterComida(chicle)
cesta.meterComida(gominola)
cesta.meterComida(pera)
cesta.meterComida(manzana)

print("Contenido cesta: ", cesta.toString())
print("Peso total:", cesta.pesoTotal())
```

14         Excepciones
======================

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.020.jpeg)

A estas alturas puede que ya seas excelente en programación. Pero aún así, tus programas pueden seguir fallando, porque hay cosas que escapan al control de tu programa y hacen que tu programa deje de funcionar. Por ejemplo, si tu programa espera que el usuario escriba un número pero este escribe letras o no escribe nada, tu programa fallará. Si tu programa tiene que leer un fichero pero este fichero no existe, tu programa fallará. Si tu programa necesita conectarse a la red pero tu ordenador no está conectado, tu programa fallará. Como puedes ver, hay situaciones sobre las que el programa no puede tener control. Por suerte tenemos un mecanismo que nos permite que si se produce una de esas sesiones, al menos nuestro programa no falle y termine sin más. Y ese mecanismo son las Excepciones.

14.1 Excepciones en Python
--------------------------

Por ejemplo, supongamos que tenemos un programa muy simple como el siguiente, en el que se le pide un número al usuario y se hace una multiplicación:

```Python
valor = input("Introduce un número: ")
valor = int(valor)
cuadrado = valor  * valor
print("El cuadrado es: ", cuadrado)
```

Si el usuario introduce lo que no debe, veremos lo siguiente:

```Python
Introduce un número: x
Traceback (most recent call last):
  File "saltaexcepcion.py", line 2, in <module>
    valor = int(valor)
ValueError: invalid literal for int() with base 10: 'x'
```

Mediante una excepción, podemos evitar que el programa falle estrepitosamente y al menos mostrar un mensaje de error al usuario. La excepción es una estructura más en el lenguaje, y tiene la siguiente forma:

```Python
try:
    código _que _puede _fallar
except:
    código _que _se _ejecuta _si _hay _error
```

Veamos el ejemplo anterior, protegiendo el código sensible dentro del bloque de excepción:

```Python
valor = input("Introduce un número: ")

try:
    valor = int(valor)
    cuadrado = valor  * valor
    print("El cuadrado es: ", cuadrado)
except:
    print("Error al convertir dato!")
```

Ahora si se mete un dato incorrecto, veremos lo siguiente:

```console
Introduce un número: x
Error al convertir dato!
```

También se podría mejorar el programa para que volviera a intentar solicitar el valor y no terminar.

Existen excepciones específicas según el tipo de error, las cuales se pueden usar para mostrar un mensaje de error más específico.

15         Manejo de ficheros
=============================

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.021.jpeg)

Hasta ahora hemos manejado pocos datos, lo que el usuario escribe por pantalla o lo que tenemos en variables. Pero si queremos utilizar cantidades más grandes de datos, podemos leer y escribir en ficheros. Existen toda clase de ficheros, desde texto, multimedia (música, vídeo) hasta binarios. Todos ellos se pueden manejar desde un programa. Como una introducción, vamos a ver cómo podemos manejar ficheros de texto.

15.1 Lectura de ficheros
------------------------

Para poder leer un fichero, necesitamos por un lado que exista ese fichero, luego ya lo podemos abrir y leer. En el siguiente código, se lee un fichero que está en el mismo sitio que el propio programa:

```Python
fichero = open("texto.txt", "r")
contenido = fichero.read()
print(contenido)
fichero.close()
```

A tener en cuenta:

 - Para leer el fichero, primero hay que abrirlo con open

 - Al abrir el fichero hay que indicar su nombre y si está en otro directorio, la ruta hacia el mismo. Si estuviera dentro de carpeta fichero, la ruta sería fichero/texto.txt.

 - El parámetro "r" indica que el fichero lo leemos solo en modo lectura o read. El fichero de texto podría ser algo así, y el programa mostraría eso mismo por pantalla.

```console
Este es un texto
de varias líneas
Y se puede leer
muy fácilmente
```

### 15.1.1 ¿Leyendo línea a línea?

En el ejemplo anterior, hemos leído todo el contenido del fichero de golpe, guardándolo en una variable de texto. Pero a veces, puede que nos interese leer el fichero línea a línea. Para ello debemos utilizar la función readline como se ve a continuación:

```Python
fichero = open("texto.txt", "r")
lineas = fichero.readline()
for linea in lineas:
    print(linea)

fichero.close()
```

15.2 Ficheros JSON
------------------

Los ficheros de texto simples como el anterior pueden contener información, pero no son datos muy manejables para un programa. Si queremos leer o guardar datos que un programa pueda manipular fácilmente, conviene usar algún formato concreto. Uno de los formatos más populares en programación es el formato JSON. Es un formato que se parece a las estructuras de diccionario en Python. Incluso también tiene la opción de representar listas como las del lenguaje. El siguiente contenido está en formato JSON. Se trata de una lista que contiene varios objetos. Si te fijas, los objetos en JSON ¡son iguales a los diccionarios en Python!

```Python
 [
    {"id": 66, "nombre": "Ada"},
    {"id": 2, "nombre": "Neko"},
    {"id": 4, "nombre" : "Bug"}
 ]
```

Lo bueno de ese formato es que se puede importar a nuestro programa Python fácilmente, siempre que sea correcto, claro.

Para poder leer ese contenido y convertir esos datos en una lista de diccionarios, utilizaremos la librería json. Mediante la función json.load podremos cargar de forma automática el contenido de ese fichero en una variable. A partir de ahí podremos manejar todo ese contenido como una lista, ¡donde cada elemento es un diccionario!:

```Python
import json

fichero = open("texto.json", "r")
contenido = json.load(fichero)

for personaje in contenido:
    print(personaje ["nombre" ])

fichero.close()
```

Por pantalla veríamos:

```console
Ada
Neko
Bug
```

15.3 Escritura de ficheros
--------------------------

Para escribir ficheros, el proceso es similar pero debemos hacer dos cosas:

 - Abrir el fichero en modo escritura.

 - Utilizar la función write para escribir contenido.

Con el siguiente código, escribiremos un par de líneas de texto en el fichero:

```Python
fichero = open("texto.txt", "w")
fichero.write("Escribo una línea  n")
fichero.write("Escribo otra línea  n")
fichero.close()
```