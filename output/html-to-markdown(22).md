### 16.1.2                       Ejercicio 6.1

Define una clase llamada Menu que tenga las siguientes funciones:

- def init__(self): recibe como parámetro una lista de opciones (strings).

- def mostrar (self): muestra las opciones precedidas de un número llamando a print.

- def seleccionar(self, numero): devuelve True si el número seleccionado está en el menú, en caso contrario devuelve False. Luego importa esa clase en el fichero 2.py y utilízala.

Fichero menu.py:

```Python
class Menu:
    def __init__ (self, opciones):
        self._opciones = opciones

    def mostrar (self):
        for i in range(len(self._opciones)):
            print(f"{i+1} {self._opciones[i]}")

    def seleccionar (self, numero):
        return numero > 0 and numero <= len(self._opciones)
```

Fichero 2.py:

```Python
import menu
miMenu = menu.Menu(["Mostrar", "Eliminar", "Salir"])

miMenu.mostrar()

if miMenu.seleccionar(1):
    print("Opción 1 presente")
else:
    print("Opción 1 no presente")
```

Resultado:

```console
1 Mostrar
2 Eliminar
3 Salir
Opción 1 presente
```
