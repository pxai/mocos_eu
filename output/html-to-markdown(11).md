   @page Section1 { size:432.05pt 432.05pt; margin:28.35pt 42.55pt 36pt } div.Section1 { page:Section1 }

8.4  Ejercicios propuestos
--------------------------

### 8.4.1    Ejercicio 1.0

Crea un programa que solicite al usuario dos valores enteros y muestre por pantalla si el primero es múltiplo del segundo. Para saber si un número es múltiplo del otro, debes hacer la operación módulo (%) entre ellos: si es 0, será múltiplo.

```Python
numero1 = input("Introduce un número: ")
numero2 = input("Introduce otro número: ")

resto = int(numero1) % int(numero2)

if resto == 0:
  print(numero1, " es múltiplo de ", numero2)
else:
  print(numero1, " NO es múltiplo de ", numero2)
```

Resultado:

```console
Introduce un número: 40
Introduce otro número: 4
40 es múltiplo de 4
```

### 8.4.2    Ejercicio 1.1

Crea un programa que solicite al usuario un número entero y haga lo siguiente: primero debe mostrar por pantalla si el número es negativo o positivo. Luego, si el número es positivo lo debe convertir a negativo y si es negativo lo debe convertir a positivo.

```Python
numero = input("Introduce un número: ")
numero = int(numero)

if numero >= 0:
    print(numero, " es positivo")
else:
    print(numero, " es negativo")

numero = -numero

print("Conversión: ", numero)
```

Resultado:

```console
Introduce un número: -6
-6 es negativo
Conversión: 6
```

### 8.4.3    Ejercicio 1.3

Escribe un programa que solicite un número un mes del año y muestre el número de días que tiene. En caso de introducir un mes desconocido, mostrar un mensaje de Mes desconocido.

```Python
mes = input("Introduce un mes del año: ")

if mes == "Enero":
    print("31 días")
elif mes == "Febrero":
    print("28/29 días")
elif mes == "Marzo":
    print("31 días")
elif mes == "Abril":
    print("30 días")
elif mes == "Mayo":
    print("31 días")
elif mes == "Junio":
    print("30 días")
elif mes == "Julio":
    print("31 días")
elif mes == "Agosto":
    print("31 días")
elif mes == "Septiembre":
    print("30 días")
elif mes == "Octubre":
    print("31 días")
elif mes == "Noviembre":
    print("30 días")
elif mes == "Diciembre":
    print("31 días")
else:
    print("Mes desconocido")
```

Resultado:

```console
Introduce un mes del año: Junio
30 días
```

### 8.4.4    Ejercicio 1.3

Crea un programa que solicite al usuario un número entero y muestre por pantalla si ese número es par y positivo. En caso contrario debe indicar si es negativo, impar o ambos.

```Python
numero = input("Introduce un número: ")
numero = int(numero)

if numero >= 0 and numero % 2 == 0:
    print(numero, " es par y positivo")
elif numero < 0 and numero % 2 != 0:
    print(numero, " es impar y negativo")
elif numero < 0:
    print(numero, " es negativo")
else:
    print(numero, " es impar")
```

Resultado:

```console
Introduce un número: -9
-9 es impar y negativo
```

### 8.4.5    Ejercicio 1.4

Crea un programa que solicite al usuario su peso en kilos y su altura en centímetros y calcule el IMC (peso / altura2); debe mostrar el resultado y luego mostrar un mensaje:

- Si el IMC es menor que 16 se muestra el mensaje: "Necesitas comer".

- Si el IMC está entre (>=)16 y 25(<) se muestra el mensaje: "Estás bien".

- Si el IMC está entre 25 y 30(<) se muestra el mensaje: "Tienes sobrepeso".

- Si el IMC es superior a 30 se muestra el mensaje: "Tienes un problema de obesidad".

```Python
peso = input("Introduce tu peso: ")
altura = input("Introduce tu altura: ")
peso = int(peso)
altura = int(altura)

imc = peso / (altura * altura)

imc = (imc * 10000)
print("Tu imc: ", imc)

if imc < 16 :
  print("Necesitas comer más")
elif imc >= 16 and imc < 25:
  print("Estás bien")
elif imc >= 25 and imc < 30:
  print("Tienes sobrepeso")
else:
  print("Tienes un problema de obesidad")
```

Resultado:

```console
Introduce tu peso: 70
Introduce tu altura: 172
Tu imc: 23.66143861546782
Estás bien
```

### 8.4.6    Ejercicio 1.5

Crea un programa que solicite al usuario un dorsal de jugador y haga lo siguiente: comprobar que ese número está entre 0 y 99. Si no lo está, entonces el programa debe terminar con un mensaje de error. Si el número está entre 0 y 99 el programa debe mostrar un texto con la posición que corresponde a cada dorsal:

- Si el usuario ha tecleado 1 el texto será "Portero"

- Si el usuario ha tecleado algo entre 1 y 5 el texto será "Defensa"

- Si el usuario ha tecleado algo entre 6 y 8, u 11 el texto será "Centrocampista"

- Si el usuario ha tecleado 9 el texto será "Delantero".

- Para cualquier otra opción el texto será "Cualquiera".

```Python
dorsal = input("Introduce dorsal: ")
dorsal = int(dorsal)

if dorsal >= 0 and dorsal <= 99:
  if dorsal == 1:
      print("Portero")
  elif dorsal >= 1 and dorsal <= 5:
      print("Defensa")
  elif dorsal >= 6 and dorsal <= 8 or dorsal == 11:
      print("Centrocampista")
  elif dorsal == 9:
      print("Delantero")
  else:
      print("Cualquiera")
else:
    print("Error, el dorsal no está entre 0 y 99")
```

Resultado:

```console
Introduce dorsal: 11
Centrocampista
```

9       Bucles
==============

![](e20514ca-a096-442d-8ee5-3f2997bc2ec72106301532469382130.015.jpeg)

Como decíamos al principio, los ordenadores son muy muy tontos. Solo hacen lo que se les diga. Pero por contra, tienen enormes capacidades y una paciencia infinita. No les importará lo más mínimo hacer lo que sea tantas veces como sea necesario.

Una de las tareas más típicas para un ordenador es repetir una instrucción. Esto es algo que se puede conseguir mediante estructuras de bucle. Un bucle es una acción que se repite. Generalmente un bucle tiene una condición para ejecutarse: si esas condiciones se cumplen, entonces se ejecutarán las órdenes que contenga ese bucle. Puedes ver un bucle como una montaña rusa en la que das varias vueltas. A continuación veremos distintos tipos de bucle.

9.1  Bucle while
----------------

Un bucle while se ejecuta mientras una condición se cumpla. Su estructura es muy simple:

```Python
while *condición*:
    *instrucciones*
```

Por ejemplo, vamos a ejecutar un bucle mientras el valor de una variable sea mayor que 0.

```Python
contador = 4
while contador > 0:
    print("Estoy dentro del bucle")
    contador = contador - 1
```

El resulto en pantalla sería:

```console
Estoy dentro del bucle
Estoy dentro del bucle
Estoy dentro del bucle
Estoy dentro del bucle
```

Nota:

¿Te has fijado en que dentro del bucle estamos restando un valor a contador? Si no tenemos cuidado y nos olvidamos de hacer eso, el valor de contador nunca cambiaría y crearíamos un bucle infinito. ¡El programa nunca terminaría y se quedaría atascado para siempre!

### 9.1.1    Ejercicio 2.0

Crea un programa que defina una variable contador iniciada a 0. Luego escribe un bucle while que mientras contador sea menor que 5 muestre el mensaje Estoy dentro del bucle y que incremente contador en 1.

```Python
contador = 0
while contador < 5:
    print("Estoy dentro del bucle")
    contador = contador + 1
```

Resultado:

```console
Estoy dentro del bucle
Estoy dentro del bucle
Estoy dentro del bucle
Estoy dentro del bucle
Estoy dentro del bucle
```

Veamos otro ejemplo. El siguiente programa solicita un dato al usuario en un bucle. El programa no saldrá del bucle mientras el usuario no meta un dato distinto de vacío "":

```Python
nombre = ""
while nombre == "":
    nombre = input("¿Cómo te llamas?")

print("Hola", nombre)
```

### 9.1.2    Ejercicio 2.1

Escribe un programa que solicite dos números al usuario. El primero debe ser menor que el segundo. El bucle debe mostrar los números que hay en el intervalo entre esos dos números.

```Python
min = input("Introduce un mínimo: ")
min = int(min)

max = input("Introduce un máximo: ")
max = int(max)

while min < max:
    print(min)
    min = min + 1
```

Resultado:

```console
Introduce un mínimo: 3
Introduce un máximo: 8
3
4
5
6
7
```

9.2  Bucle For
--------------

El bucle for lo utilizamos para repetir una acción un número concreto de veces. Más que una condición, utiliza una especie de contador:

```Python
for *variable* in *rango*:
    *instrucciones*
```

Por ejemplo, el siguiente bucle mostrará el mensaje hola 4 veces:

```Python
for i in range(4):
    print("Hola")
```

El resultado sería:

```console
Hola
Hola
Hola
Hola
```

Algo muy interesante en los bucles for es que la variable i, la cual podría tener el nombre que queramos, tendrá el valor correspondiente a cada vuelta del bucle. Para verlo mejor, basta con cambiar un poco el programa anterior:

```Python
for i in range(4):
    print("Hola", i)
```

Y comprobar el resultado:

```console
Hola 0
Hola 1
Hola 2
Hola 3
```

Eso nos puede ser útil en muchos programas.