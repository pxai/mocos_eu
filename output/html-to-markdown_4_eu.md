5.5.1    Ariketa 0.2

Idatzi programa batean ikusitako mota bakoitzeko aldagai bat adierazten duena, eta lehio bidez erakutsi.
```Python
nombre = "Ada"
edad = 42
peso = 101.54
vivo = True
riquezas = None
amigas = ["Ada", "Ruby", "Miranda"]

print(nombre)
print(edad)
print(peso)
print(vivo)
print(riquezas)
print(amigas)
```
Emaitza:
```console
Ada
42
101.54
true
null
["Ada", "Ruby", "Miranda"]
```
6       Datuak irakurtzen
========================

Programa batek egin nahi badu, askotan behar izango du erabiltzaileak datu bat sartzen duela. Adibidez, programa bat izan nahi badugu eta gure izenak zenbat letra dituen jakitea edo gure jaiotza eguna hainbat egun falta duela jakitea, lehenengo egoera hori programa-k datu bat eskatu beharko litzateke.

Momentu honetan ikusten ari garen programa oinarrizkoak, erabiltzen dituzten pantaila horiek erabilzen dute exekutatzeko. Horiek konsolak dira, zalantzarik gabe.

Erabiltzaileak datu bat eskatzeko eta hainbat aldagaian gordetzeko, "input" funtzioa erabiltzen da:
```Python
nombre = input("Dime tu nombre: ")
print("Hola ", nombre)
```
Pantailan hurrengoa ikusiko zenuke:
```console
Dime tu nombre:
```
Input funtzioak Pantailan "Zein da zure izena?" hizkia agertzen du. Gainera, erabiltzaileak idatzi arte programa gelditzen da. Erabiltzaileak Rosa idatzi baldin bada, honela agertuko da pantailan:
```console
Dime tu nombre: Rosa
Hola Rosa
```
6.1.1    0.3 Ariketa

Idatzi programa bat erabiltzaileari izen bat eskatzeko eta hau aldagai batean gordetzeko. Ondoren, agurra erakutsi behar da konsolean.
```Python
nombre = input("Introduce tu nombre: ")
print("Hola, qué tal estás ", nombre)

# Alternativa:
# print("Hola, qué tal estás %s" % nombre)
```
Emaitza:
```console
Introduce tu nombre: Juan
Hola, qué tal estás Juan
```
6.2 Datuekin arduratzen saiatu
--------------------------

Input funtzioa erabiltzen dutenean, erabiltzaileak idazten duen guztia, testua bezain izango da, zenbakia idatzi ezik.

(I apologize if the translation is not perfect.)
```Python
valor = input("Dame un número: ")
doble = valor + valor
print(doble)
```
Erabiltzaileak zenbaki bat sartzen badu, adibidez 4, hau emaitza izango da:
```console
Dame un número: 4
44
```
4 + 4 batu eta 8 erakutsi baduzu, 4 eta 4 batu egin du asetzeko. Egia esan, input bidez irakurritako 4a testua da: "4".

Honek saihesteko, beste funtzio bat erabili behar dugu datu hori zenbaki errealean bihurtzeko: int()
```Python
valor = input("Dame un número: ")
doble = int(valor) + int(valor)
print(doble)
```
Edozein programazioa egiteko balio dezakezu hau da:
```Python
valor = input("Dame un número: ")
valor = int(valor)
doble = valor + valor
print(doble)
```
Edozein gauzarako erabil dezakezu, hala nola input-ean aplikatzea ere.
```Python
valor = int(input("Dame un número: "))
doble = valor + valor
print(doble)
```
Ora bai, batuketa zenbakizkoa izango da:
```console
Dame un número: 4
8
```
6.2.1    0.4 Ariketa:

Idatzi programa bat erabiltzari bati zenbaki bat eskatzeko eta 10 batu ondoren emaitza konsolan erakutsi behar du. Gogoratu sarrera balioa entzutetsu bihurtzeko int egin behar dela.
```Python
valor = input("Introduce un número: ")
resultado = int(valor) + 10

print("La suma es:", resultado)
```
Emaitza:
```console
Introduce un número: 32
La suma es: 42
```
6.3 Beste aldaketak
-----------------------

Badakit programazio hizkuntzetan aldagaien motak adierazi beharrik ez ditugula baina, adierazi dizkiguten motak (testua, zenbakia...) programa exekutatu arte kontuan hartzen dira.

Adibidez, zenbaki bat kontaindu duen aldagai bat daukagu eta hau testuan lotu nahi duguenean, akats bat jasoko genuke:
```Python
valor = 66
texto = "Mi edad es " + valor
```
Errorea hau da:
```console
TypeError: cannot concatenate 'str' and 'int' objects
```
Horregatik, testu batera indartzeko mota behartu behar dugu str() erabiliz:
```Python
valor = 66
texto = "Mi edad es " + str(valor)
```
Hori dela eta, kasu askotan balio bat mota jakin bati bihurtu beharko dugu. Bihurtzeko funtzio hauek dira:

* str(): balioa testura bihurtzen du. str(5) "5" itzuliko luke.
* int(): balioa zenbaki osora bihurtzen du. int("5") 5 itzuliko luke.
* float(): balioa zenbakizko hamartarrerako bihurtzen du. float("5.5") 5.5 itzuliko luke.
* bool(): balioa booleanora bihurtzen du. bool("False") False itzuliko luke.

Kontuz!

Inkompatible balio bat bihurtatu nahi baduzu, programak hut egitea posible da.

7    Operadoreak
==================

Programek zenbakiak kalkulatu, datuak prozesatu, balioen arabera erabakiak hartu behar dituzte. Horretarako, operadoreak behar ditugu.

7.1 Operadore aritmetikoak
---------------------------

Zenbatzeak, kenketak eta kalkulu basikoak balioekin eta aldagaietan dauzkagun balioekin egin ditzakegun operadore guztiak dira, adibidez, zenbatzea:
```Python
chicles = 4
chicles = chicles + 2
```
Programak kalkulatzen du 4 txikitxoen gainetik 6 izan zara. Programazioan erabiliko diren eragiketak hauek dira:

-  batuketa: +

-  kenketa: -

-  biderketa: *

-  zatiketa: /

Adibidez, egun batek zenbat segundu dituen kalkulatzeko:
```console
minutos = 60
segundos = 60
horas = 24
```
segundosTotales = segundos * minutos * horas

Puedes hacer cálculos bien complicados. Si quieres que parezcan más simples de leer, puedes utilizar paréntesis como en matemáticas:
```Python
ada = 14
bug = 10
neko = 2
media = (ada + bug + neko) / 3
```
7.1.1    Ariketa 0.5

Idatzi programa bat erabiltzaile bati zenbaki bat eskatzeko eta 5 ebatzi ondoren. Ondoren, emaitza pantailatik erakutsi behar da.
```Python
valor = input("Introduce un número: ")
resultado = int(valor) - 5

print("La resta es:", resultado)
```
Emaitza:
```console
Introduce un número: 30
La resta es: 25
```
7.1.2    Moduloa eta esponentziala

Programazioan oso garrantzitsua den operazio bat dago, matematikako klaseetan gutxi jardun ohi dena: hori da moduloa. Honek zatiketak ematen ditu, baina zatiketa emaitza ordez, hutsunea itzultzen du:
```Python
valor = 8
resultado = valor % 3
```
Emaitza 2 izanen da.

Exponentiala zehazki zenbaki bat bere burua zenbaki hainbat aldiz bideratuz lortzen da. Pythonen ** operadorearekin egin daiteke hainbat aldiz bideratzea.
```Python
valor = 2
resultado = valor ** 3 # equivale a: 2 * 2 * 2
```
```
-5, -248, -1.87, ...
```
Emaitza 8 izan da.

### 7.1.3    Signo aldatzea

Ondo dakizunez, zenbakiak 0 baino txikiagoak izan daitezke, negatiboak izendatuak, - aurrean agertzita:

Zenbakien signoa aldatu nahi badugu, - aurrean jarri dezakegu:
```Python
temperatura = -11
cuenta = 200

temperatura = -temperatura   11
cuenta = -cuenta    # -200
```
7.1.4  Abreviaturak
Zenbaitetan, aldagai batekin egin eta emaitza bere buruan gorde beharko duzu:

```Python
contador = 0
contador = contador + 2
```
Horrelako egoera hauetan, erabil dezakezu oinarrizko operadore batean, zeina egiten du eta bera instant batera esleitu. Haukoa izango litzateke aurreko kodearen bertsio sinplea:
```console
contador = 0
contador += 2
```
Operadore guztiekin hau egin dezakezu:

Lanbide

Ere bai da

Labur

(Note: This translation may not precisely convey the technical meaning of the original text.)
```Python
a = a + 1

a += 1

a = a - 1

a -= 1

a = a * 1

a *= 1

a = a / 1

a /= 1

a = a % 1

a %= 1
```
7.1.5    Ariketa 0.6

Idatzi programa bat erabiltzaile bati zenbaki bat eskatzeko eta handituko duena. Ondoren, emaitza konsolan erakutsi behar du. Ondoren balioa murriztu eta emaitza konsolan erakutsi.

Beharrezkoak diren eragiketak erabiliz!
```Python
valor = input("Introduce un número: ")
valor += 1

print("El incremento es", valor)

valor -= 1

print("El decremento es", valor)
```
Emaitza:
```console
Introduce un número: 6
El incremento es 7
El decremento es 6
```
7.2 Konparaketa operadoreak
------------------------------

Dira eragileak dira, balioa beste batekin alderatzeko aukera ematen digutenak. Orokorrean, zenbakiak erabiliz, eta eragin hauek emaitza True edo False izaten dute.

Adibidez, balio bat bestearekin berdina den ikusi nahi badugu, eragilea erabiltzen dugu: ==
```Python
valor = 5
resultado = valor == 5
```
Emaitza True izango da.

Konparazioen operadoreak hauek dira:

•       Berdina: ==

•       Desberdina: !=

•       Handiagoa: >

•       Txikiagoa: <

•       Handiago edo berdina: >=

•       Txikiago edo berdina: <=

Testua erabil dezakezu ere operadore honekin, berdintasuna egiaztatzeko:
```Python
nombre = "Ada"
resultado = nombre == "Bug"
```
Emaitza False izan daiteke.

Testua alfabetikoki handiago edo txikiago den konparatu ahal izaten digu ere:
```Python
nombre = "Ada"
resultado = "Ada" < "Bug"
```