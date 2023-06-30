### 12.3.1 Ejercicio 4.3

Escribe un programa con una función llamada dividir que reciba los parámetros a y b. La función debe retornar la división entre los dos números.

```Python
def dividir (a, b):
    return a / b


print(dividir(32, 4))
```

Resultado:

```console
8
```

Otro ejemplo, una función que multiplique un valor varias veces. Si el número de veces es menor que 1 devolverá un 0:

```Python
def multiplica(numero, veces):
    if (veces > 0):
        total = 1
        for i in range(veces):
            total = total * numero
    else:
        return 0

multiplica(2, 3) # 8
```

Nota:

La función anterior queda más clara así.

```Python
def multiplica(numero, veces):
    if (veces < 1): return 0

    total = 1
    for i in range(veces):
        total = total * numero
```

12.4 Llamadas anidadas
----------------------

No tengas miedo a anidar las llamadas de funciones. Es algo muy natural en programación. Imagina que tenemos esta función que se encarga de solicitar un número al usuario y devuelve el ńumero introducido:

```Python
def leeNumero():
    numero = input("Escribe número: ")
    return int(numero)
```

Supongamos que también tenemos otra función para restar números:

```Python
def restar (a, b)
    return a - b
```

Si queremos hacer un programa que solicite dos números al usuario y los reste podríamos hacerlo así:

```Python
print(restar(leeNumero(), leeNumero()))
```

En lugar de poner un número o una variable como parámetro, podemos poner una llamada a una función.

Esas funciones leeNumero(), devolverán algún valor. En cuanto se llame al primer leeNumero() será como tener:

```Python
print(restar(5, leeNumero()))
```

Y luego tras llamar al segundo leeNumero() :

```Python
print(restar(5, 2)
```

Luego se llamará a restar y devolverá un valor:

```Python
print(3)
```

Y finalmente se llamará a print y veremos el resultado:

```console
3
```

### 12.4.1                       Ejercicio 4.4

Escribe dos funciones. Una que reciba un número y devuelva el mismo número en positivo.

```Python
def positivo(valor)
```

Y otra función que reciba dos números y calcule la potencia entre ellos.

```Python
def potencia(valor1, valor2)
```

Debes llamar a la segunda función pasando como parámetros:

```Python
potencia(positivo(-5), positivo(4))
```

Nota:

No utilices funciones preexistentes.

```Python
def positivo (valor):
    if valor < 0:
        return -valor

    return valor
```

```Python
def potencia (valor1, valor2):
    return valor1 \*\* valor2

print(positivo(-1))
print(potencia(2, 3))
print(potencia(positivo(2), positivo(4)))
potencia(positivo(-5), positivo(4))
```

Resultado:

```console
1
8
16
```

12.5 ¿Por qué usar funciones?
-----------------------------

Ok, ¿para qué necesitamos crear funciones? Pues lo cierto es... que son fundamentales.

Hasta ahora hemos visto programas que son una simple secuencia de órdenes, las cuales se ejecutan desde el principio hasta el final.

Eso está bien cuando los programas son simples y tienen que hacer pocas cosas, pero cuando el programa tiene que hacer algo más complejo es muy probable que tengas que usar funciones, por varios motivos.

### 12.5.1                       Motivo 0: divide y vencerás

Los programas tratan de resolver problemas ofreciendo una solución. En ocasiones los problemas pueden ser muy complejos de afrontar. Las funciones te permiten abordar esos problemas por partes. Cada función te puede dar la solución para una parte del problema. Por lo tanto, puedes dividir el problema en muchos pequeños problemas y solucionar cada problema con una función. Escribir el código en funciones es el primer paso que te permitirá diseñar programas más complejos.

### 12.5.2                       Motivo 1: no repetir el código

Si tu programa tiene que hacer alguna cosa varias veces, tendrías que repetir el código tantas veces como fuera necesario. Imagina que tienes que recibir varios datos del usuario, y que cada vez que lo haces tienes que comprobar que el dato no está vacío:

```Python
dato = ""

while dato == "":
    dato = input("Por favor, introduce un dato: ")
    if dato == "":
        print("¡El dato está vacío!)
```

Si solicitas al usuario 3 datos, ¡tendrías que repetir ese código 3 veces! En cambio si creas una función con ese mismo código, solo lo tendrás que escribir una vez y luego podrás usarlo tantas veces como necesites.

Nota:

NO repetir el código es una de las reglas más importantes que debe seguir todo buen programador. Incluso puedes aplicar la regla del 3: a la tercera vez que tengas que repetir algo, tienes que automatizarlo.

### 12.5.3                       Motivo 2: reutilizar código

Además de no repetir el código, una función nos permite que un mismo código sirva para distintos tipos de datos. ¡Para eso se utilizan los parámetros!

```Python
def saludar(saludo, veces):
    for i in range(veces):
        print(saludo)
```

Se le puede llamar con distintos valores:

```Python
saludar("Holi", 3)
saludar("Aupa", 1)
```

Sería:

```console
Holi
Holi
Holi
Aupa
```

### 12.5.4                       Motivo 3: facilitar el mantenimiento

Si el código está en un único sitio, es más fácil corregirlo, cambiarlo, mejorarlo y mantenerlo en general. Crear un programa desde cero es muy bonito, pero el verdadero trabajo es mantener el código a lo largo del tiempo. Si tenemos nuestras funciones bien definidas, nos ahorraremos muuuuucho trabajo.

### 12.5.5                       Motivo 4: permite hacer tests

Quizá seas un poco joven para esto, pero las verdaderas pros como yo testeamos nuestros programas. ¿Qué significa eso? Que escribimos programas cuya única función es comprobar que nuestros programas hacen lo que deben. Si tu código tiene funciones, podrás escribir tests para comprobar que esas funciones hacen lo que deben.

En realidad, cuando ya eres una experta, lo suyo es que escribas el test ¡antes que la función en si misma! Veremos un poco más sobre los test más adelante.

12.6 Cómo hacer buenas funciones
--------------------------------

Cualquiera puede escribir funciones y agrupar el código en pequeñas partes. Pero si quieres escribir funciones como un pro, tienes que procurar lo siguiente:

- Una función debe hacer solo una cosa. Es mejor tener muchas pequeñas funciones que pocas funciones haciendo muchas cosas. Si tu función no cabe en la pantalla o pasa de 24 líneas, quizá debas dividirla en pequeñas partes.

- Una función no debería cambiar nada que haya fuera. Si no quieres tener sorpresas, una función no debería liarla dentro del programa.

- Una función debería retornar algo, y ese algo siempre debería ser lo mismo para determinados parámetros.