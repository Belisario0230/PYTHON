# Ejercicio 1
# Dado un número entero introducido por teclado, guarda sus divisores en un conjunto y muéstralo.

numero = int(input("Dijite un numero entero positivo: "))
if numero >= 0:
    divisores = set()
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.add(i)
    print(divisores)
else:
    print("No has dijitado un numero entero positivo. Vuelve a intentarlo.")


# Ejercicio 2
# Crea un programa que dado un conjunto, nos devuelva su mínimo. Debes hacerlo sin recurrir a la función min().

mi_set = {10, 20, 30, 40, -50, 60, 70, 9, -400} 
minimo = 999

for e in mi_set:
    if e < minimo:
        minimo = e

print("El mínimo de {} es {}".format(mi_set, minimo))

# Ejercicio 3
# Dada una frase introducida por teclado, guarda en un conjunto todas las palabras que empiecen 
# por la letra indicada por el usuario.

frase_introducir = input("Frase: ")
letra_introducir = input("Letra: ")

frase_introducir = frase_introducir.lower()
letra_introducir = letra_introducir.lower()

oracion_introducir = frase_introducir.split(" ")
guardar_palabras = set()

for cualquier_letra in oracion_introducir:
    if cualquier_letra.startswith(letra_introducir):
        guardar_palabras.add(cualquier_letra)

print(guardar_palabras)

# Ejercicio 4
# Dado un conjunto, crea un programa que nos devuelva el caracter con mayor valor ASCII. 
# Debes hacerlo sin recurrir a la función max().

mi_conjunto = {0, 3, "A", 1, "ñ", "@", 8, "*", "ƒ"}
max = -9999

for e in mi_conjunto:
    if ord(str(e)) > max:
        max = ord(str(e))

print("El caracter con mayor valor ASCII es", chr(max))

#Ejercicio 5
#Dado un conjunto, crea un programa que nos devuelva el caracter con menor valor ASCII. 
# Debes hacerlo sin recurrir a la función min().

mi_conjunto = {0, 3, "A", 1, "!", "@", 8, "*", "ƒ"}
min = 9999

for e in mi_conjunto:
    if ord(str(e)) < min:
        min = ord(str(e))

print("El caracter con menor valor ASCII es", chr(min))

#Ejercicio 6
#Dada una frase introducida por teclado, guarda en un conjunto todas las palabras que contengan 
# la letra indicada por el usuario.

frase = input("Frase: ")
letra = input("Letra: ")

frase = frase.lower()
letra = letra.lower()

words = frase.split(" ")
contains_letter = set()

for cualquier_letra in words:
    if letra in cualquier_letra:
        contains_letter.add(cualquier_letra)

print(contains_letter)

#Ejercicio 7
#Dada una frase introducida por teclado, guarda en un conjunto la primera letra de cada palabra 
# sin hacer uso del método .split().

frase = input("Frase: ")
primera_letra = set()

for cualquier_letra in frase.title():
    if cualquier_letra.isupper():
        primera_letra.add(cualquier_letra.lower())

print(primera_letra)

#Ejercicio 8
#Dada una frase introducida por teclado, guarda en un conjunto todas las palabras 
# con longitud par. #1

introduce_frase = input("Frase: ")
introduce_frase = introduce_frase.lower()

palabras = introduce_frase.split(" ")
guardar_palabras = set()

for cualquier_letra in palabras:
    if len(cualquier_letra) % 2 == 0:
        guardar_palabras.add(cualquier_letra)

print(guardar_palabras)

#Ejercicio 9
#Dada una frase introducida por teclado, guarda en un conjunto todas las palabras que 
# acaben por la letra indicada por el usuario.

s = input("Frase: ")
letter = input("Letra: ")

s = s.lower()
letter = letter.lower()

words = s.split(" ")
ends_with = set()

for w in words:
    if w.endswith(letter):
        ends_with.add(w)

print(ends_with)

#Ejercicio 10
#Dada una frase introducida por teclado, guarda en un conjunto todas las palabras palíndromas.#2

frase_introduce_usuario = input("Frase: ")
frase_introduce_usuario = frase_introduce_usuario.lower()

palabras = frase_introduce_usuario.split(" ")
palindroms = set()

for w in palabras:
    isPalindrom = True
    l = []
    for c in w:
        l.append(c)


# Empieza la aventura!
# ¡Por fin ha llegado el día! La tripulación de Pyratilla zarpa con rumbo a lo desconcocido en busca de tesoros y con la intención de navegar por el mundo entero.

# A decir verdad, ninguno de los miembros de los Pyrates lo tiene difícil, pues según el mapa que encontró Pyerce leyendo libros de cartografía, su mundo está compuesto por un total de 7 islas:

# Isla Alegre, la isla en la que todos nacieron y se criaron

# Isla Golosa
# Isla Espesura
# Isla Arrecife
# Isla Lejana
# Isla Torva
# Isla Verde
# Ayuda a Pyratilla a hacer un conjunto de las islas de su mundo, llamado islands.

islas = {"Isla Alegre", "Isla Golosa", "Isla Espesura", "Isla Arrecife", "Isla Lejana", "Isla Torva", "Isla Verde"}

visitadas_islas = {"Isla Alegre"}

no_visitadas_islas = islas - visitadas_islas
print(no_visitadas_islas)