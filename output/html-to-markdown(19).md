### 13.4.2 Ejercicio 5.2

Escribe un programa que defina la clase Comida con el atributo nombre. Crea una subclase llamada Fruta que extienda la clase Comida con un constructor que recibe nombre y vitaminas, y un método llamado info que devuelva toda su información. vitaminas es una lista de nombres. Crea una instancia para probar la clase Fruta.

```Python
class Comida:
    def __init__(self, nombre):
        self.nombre = nombre


class Fruta(Comida):
    def __init__(self, nombre, vitaminas):
        super().__init__(nombre)
        self.vitaminas = vitaminas

    def info (self):
        # return f"{self.nombre} {self.vitaminas}";
        return self.nombre + " " + str(self.vitaminas)

postre = Fruta("Kiwi", ["A", "C"])
print(postre.info())
```

Resultado:

```console
Kiwi ['A', 'C']
```

13.5 Encapsulación
------------------

En el ejemplo del gato, se puede hacer acceder a la propiedad nombre de forma directa. Para eso, en los objetos basta con poner algo así:

```Python
objeto.nombrePropiedad
```

El gato tiene una propiedad llamada nombre.

```Python
miGato = Gato("Pixi")
print(miGato.nombre)  # Pixi
miGato.nombre = "Pixel"
miGato.maulla() # Miau, soy Pixel
```

Acceder a una propiedad de forma tan directa no está mal, pero las buenas programadoras como yo tratamos de encapsular la clase. ¿Qué significa eso? Que no se permite que se pueda acceder o cambiar directamente las propiedades o métodos de la misma. Solo aquello que sea necesario para quienes usen la clase. Dicho de otra forma, los programadores deben tratar de crear clases que parezcan "cajas negras". En el caso de las propiedades como el nombre, en Python se puede añadir los siguientes métodos:

*   Un método para devolver el valor de la propiedad nombre, también conocido como "getter":

```Python
    @property
    def nombre ():
        return self._nombre
```

*   Un método para poder modificar el valor del nombre, también conocido como "setter":

```Python
    @nombre.setter
    def nombre (nombre):
        if nombre != "":
            self._nombre = nombre
```

La clase quedaría así:

```Python
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

Observa que la propiedad nombre es ahora _nombre. Es una manera de expresar que esa propiedad es "privada", y que no se debería acceder a ella desde fuera de la clase.

Ahora cuando usemos la clase Gato e intentemos acceder a la propiedad . nombre, se hará a través de esas nuevas funciones.

```Python
miGato = Gato("Pixi")
print(miGato.nombre)  # llama al método `def nombre ():`
miGato.nombre = "Pixel" # llama al método `def nombre (nombre):`
miGato.maulla() # Miau, soy Pixel
```

### 13.5.1 Ejercicio 5.3

Escribe un programa que defina la clase Vehiculo con el atributo matricula, con métodos get/set y otro método llamado arrancar. Crea una subclase llamada Coche que extienda la clase Vehículo con un constructor que recibe matricula, modelo y color, y una función llamada info que devuelva toda su información. Crea una instancia para probar la clase Coche.

```Python
class Vehiculo:
    def __init__(self, matricula):
        self._matricula = matricula

    @property
    def matricula (self):
        return self._matricula

    @matricula.setter
    def matricula (self, matricula):
        self._matricula = matricula

    def arrancar (self):
        print("Arrancando ", self._matricula)


class Coche(Vehiculo):
    def __init__(self, matricula, modelo, color):
        super().__init__(matricula)
        self._modelo = modelo
        self._color = color

    def info (self):
        return f"{self.matricula} {self._modelo} {self._color}";


coche = Coche("0042ASI", "Opel Corsa", "Blanco")
coche.arrancar()
print(coche.info())
```

Resultado:

```console
Arrancando 0042ASI
0042ASI Opel Corsa Blanco
```

¿Qué ventaja puede tener la encapsulación? Básicamente que desde "fuera" no se pueda manipular la clase sin control. De ahí que sea como una caja negra, como una videoconsola. Si para jugar un juego tuvieras que abrirla y soldar las conexiones a mano probablemente te acabarías cargando la consola. Por eso los aparatos se diseñan como cajas negras, solo te permiten manipularlas desde fuera.

En el caso de la clase Gato, no permitimos que el nombre se pueda cambiar directamente. A través de la función "setter" podemos controlar que el nombre que se quiera asignar sea correcto.

13.6 Clases que contiene otras clases
-------------------------------------

Con la programación orientada a objetos, tratamos de representar cosas del mundo real a través de clases. Y esas clases pueden estar relacionadas unas con otras.

Por ejemplo, un Colegio puede tener Aulas, un aula puede tener Alumnos y un Profesor, etc. Las clases pueden contener por tanto, propiedades que en realidad son otras clases o incluso listas de otras clases.

```Python
class Alumno:
    def __init__ (self, nombre):
        self._nombre = nombre

class Aula:
    def __init__ (self):
        self._alumnos = []
   
    def meteAlumno (self, alumno):
        self._alumnos.append(alumno)

    def pasarLista (self):
        for alumno in self._alumnos:
            print(alumno._nombre)

alumno1 = Alumno("Gumball")
alumno2 = Alumno("Darwin")

aula = Aula()

aula.meteAlumno(alumno1)
aula.meteAlumno(alumno2)
aula.pasarLista()
```

Los diseños pueden ser tan complejos como sea necesario para representar lo que necesitemos.

### 13.6.1 Ejercicio 5.4

Escribe un programa que defina la clase Piloto con el atributo nombre y las funciones get/set. Crea también una clase llamada Aeroplano con el atributo modelo, piloto y copiloto, con funciones get/set para el modelo y otro método llamado volar. Crea una instancia para probar ambas clases.

```Python
class Piloto:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre (self):
        return self._nombre

    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre

class Aeroplano:
    def __init__(self, modelo, piloto, copiloto):
        self._modelo = modelo
        self._piloto = piloto
        self._copiloto = copiloto

    @property
    def modelo (self):
        return self._modelo

    @modelo.setter
    def modelo (self, modelo):
        self._modelo = modelo

    def volar (self):
        return f"Volando {self._modelo} {self._piloto.nombre} con {self._copiloto.nombre}"


piloto1 = Piloto("Han Solo")
piloto2 = Piloto("Murdock")
avioneta = Aeroplano("AirBluff 727", piloto1, piloto2)

print(avioneta.volar())
```

Resultado:

```console
Volando AirBluff 727 Han Solo con Murdock
```

13.7 Métodos estáticos
----------------------

Normalmente, para poder utilizar una clase siempre creamos una instancia de la misma, como hacíamos en el ejemplo anterior:

```Python
alumno1 = Alumno("Gumball")
```

En determinadas ocasiones, puede que nos interese crear una clase de la que no queramos hacer copias y que solo sirva para hacer una tarea concreta, como si fuera una función.

Por ejemplo, podemos hacer una clase que dado un nombre, le dé un formato correcto, con la primera letra mayúscula y el resto de letras en minúsculas:

```Python
class Formato:
    @staticmethod
    def formato (nombre):
        return nombre[0].upper() + nombre[1:].lower()

print(Formato.formato("gUmBaLl"))
```

Resultado:

```console
Gumball
```

### 13.7.1 Ejercicio 5.5

Escribe un programa que defina una clase llamada Numero y una función estática llamado aleatorio(max). Esta función debe devolver un número dentro del intervalo 0 y max.

```Python
import random

class Numero:
    @staticmethod
    def aleatorio (max):
      return random.randint(0, max)

for i in range(5):
    print(Numero.aleatorio(10))
```

Resultado:

```console
4
3
0
9
1
```

Meter métodos estáticos en una clase puede resultar útil cuando queremos agrupar unas funciones en una única clase, y no queremos crear distintas instancias, sino utilizar funciones concretas.