   @page Section1 { size:432.05pt 432.05pt; margin:28.35pt 42.55pt 36pt } div.Section1 { page:Section1 }

### 8.3.1    Ejercicio 1.2

Escribe un programa que solicite un texto al usuario. Si el texto es "mañana", debe mostrar el mensaje "Buenos días", si el texto es "tarde" debe mostrar el mensaje "Buenas tardes", y si no debe mostrar el mensaje "Buenas noches"

```Python
texto = input("Introduce un texto: ")

if texto == "mañana":
    print("Buenos días.")
elif texto == "tarde":
    print("Buenas tardes.")
elif texto == "noche":
    print("Buenas noches.")
else:
    print("No entiendo.")
```

Resultado:

```console
Introduce un texto: tarde
Buenas tardes.
```