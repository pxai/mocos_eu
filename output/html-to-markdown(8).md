   @page Section1 { size:432.05pt 432.05pt; margin:28.35pt 42.55pt 36pt } div.Section1 { page:Section1 }

### 8.2.1    Ejercicio 1.1

Escribe un programa que solicite un texto al usuario. Si el texto es "saluda" debe mostrar un saludo, en caso contrario debe mostrar un mensaje que diga "no entiendo".

```Python
texto = input("Introduce un texto: ")

if texto == "saludo":
    print("Hola!")
else:
    print("No entiendo.")
```

Resultado:

```console
Introduce un texto: no sé
No entiendo.
```

8.3  if elif else
-----------------

Existe otra variante cuando necesitamos comprobar varias condiciones. Para eso existe la estructura if-elif-else:

```Python
if *condición1*:
    *instrucciones*
elif: *condición2*:
    *instrucciones*
elif *condición3*
    *instrucciones*
else:
    *instrucciones*
```

Supongamos que queremos un programa que sea capaz de saludar en distintos idiomas. Podríamos crear un programa como el siguiente:

```Python
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

Podemos tener tantos elif como hagan falta.