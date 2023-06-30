
¡OJO!

Si escribimos de esa manera, estaremos machacando el contenido del fichero. Contenido del fichero:

```console
Escribo una línea
Escribo otra línea
```


Si queremos escribir añadiendo contenido, debemos abrir el fichero en modo "a":

```Python
fichero = open("texto.txt", "a")
fichero.write("Añado una línean")
fichero.write("Añado otra línean")
fichero.close()
```

Ahora el contenido del fichero sería:

```console
Escribo una línea
Escribo otra línea
Añado una línea
Añado otra línea
```

15.4 Escribir en un fichero json
--------------------------------

En el caso de un fichero en formato JSON, lo que nos tiene que preocupar es que al momento de escribir, convirtamos nuestros datos a texto. Por suerte para eso hay una función que lo hace de forma automática: json.dumps()

En el siguiente ejemplo, se carga el contenido de un fichero json dentro de una variable. Luego añadimos un elemento a esa lista. Abrimos el fichero otra vez, en modo escritura, y hacemos un write utilizando json.dumps para convertir el contenido en texto:

```Python
import json

fichero = open("texto.json", "r")
contenido = json.load(fichero)
fichero.close()

personaje = { "id": 666, "nombre": "Gumball" }
contenido.append(personaje)

fichero = open("texto.json", "w")
fichero.write(json.dumps(contenido))
fichero.close()
```

16         Librerías
====================

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.022.jpeg)

Conforme los programas se hacen más y más complejos, es probable que tengamos que definir muchas funciones, o separar el diseño en clases, etc. Pese a que podríamos tener todo dentro del mismo fichero, no sería la mejor forma de organizar nuestro código. Lo ideal es que separemos cada clase en su propio fichero y cada función o grupo de funciones en su propio fichero.

Una vez organizado el código en ficheros e incluso en carpetas, ya podemos reutilizarlos en otros ficheros. Veamos un ejemplo simple.

Definimos la siguiente función en un fichero llamado mates.py:

```Python
def sumar (a, b):  -
    return a + b

def restar (a, b):
    return a - b

def incrementar (a):
    return a - 1
```

Ahora podemos incluir ese fichero en otro programa mediante la orden import. Si están en el mismo directorio se puede hacer simplemente:

```Python
import mates

valor1 = 5
valor2 = 10

resultado = mates.sumar(valor1, valor2)
print(resultado)  # 15
```

### 16.1.1                       Ejercicio 6.0

En un ejercicio anterior, se proponía hacer un generador de contraseñas. Utiliza el mismo código pero créalo dentro de un fichero. Crea otro fichero donde debes importar ese código y utilizarlo.

Fichero generar.py:

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
```

Y lo usamos en fichero 1.py:

```Python
import generar

password = generar.generarPassword(8)

print(password)
```

Resultado:

```console
g3ep-ahx
```

Con las clases se puede hacer exactamente lo mismo. Supongamos que tenemos una clase llamada LectorPantalla en un fichero llamado lector_pantalla.py. Es una clase que nos permite leer datos desde la consola:

```Python
class LectorPantalla:
    def leerEntero (self, mensaje = "Introduce un número: "):
        numero = input(mensaje)
        return int(numero)

    def leerTexto (self, mensaje = "Introduce texto: ")
        texto = input(mensaje)
        return texto
```

Ahora podemos reutilizar esa clase en otro fichero, junto con nuestro fichero mates.

```Python
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
