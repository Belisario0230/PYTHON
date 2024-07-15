# Ejercicio 1 Crea un programa que lea una secuencia de caracteres, guarde cada caracter en una posición 
# de una lista y finalmente muestre la secuencia invertida.#

string = input("Ingrese un string: ")
lista = []

for c in string:
    lista.append(c)
lista.reverse()
print(lista)

# Ejercicio 2 Crea un programa que lea dos strings de la misma longitud, los guarde intercalados
# en una lista. Por último,mostrar el contenido de la lista.Por  ejemplo,  si  introducimos hola 
# caracola y adios marieta,  debería  mostrarse haodleao  #

string1 = input("Ingrese strind 1: ")
string2 = input("Ingrese string 2: ")
lista1 = []
if len(string1) == len(string2):
    for i in range(len(string1)):
        lista1.append(string1[i])
        lista1.append(string2[i])
    for item in lista1:
        print(item, end = "")
else:
    print("Los strings no tienen la misma longitud")

# Ejercicio 3 Crea un programa que lea un string y guarde en una lista todas las consonantes. #
string10 = input("Ingrese una palabra: ")
lista_vacia = []
for palabra in string10.lower():
    if palabra == "a" or palabra == "e" or palabra == "i" or palabra == "o" or palabra == "u":
        continue
    lista_vacia.append(palabra)
    print(lista_vacia) 

#Ejercicio 4 Crea un programa que lea una palabra, la guarde en una lista y compruebe si se trata 
# de un palíndromo.#

palabra = input("Ingrese una palabra: ")
lista20= []
is_palindromo = True

for c in palabra:
    lista20.append(c)

n = len(lista20)
for i in range(int(n/2)):
    if lista20[i] != lista20[n-(i + 1)]:
        is_palindromo = False
print("Es {} palindromo? {}".format(palabra,'Si' if is_palindromo else 'No'))

# Ejercicio 5 Crea un programa que lea una matriz 3 x 3 y devuelva el máximo de cada fila.#
A = []
for i in range(3):
    A.append([])
    for j in range(3):
        A[i].append(float(input("Dijita el caracter: ({}, {})".format(i,j))))

for i in range(3):
    A[i].sort(reverse = True)
    print("El maximo de la fila {} es {}".format(i, A[i][0]))

# Ejercicio 6 Crea un programa que lea un entero, n, de teclado y construya una matriz de tamaño n×n. 
# Cada posición debe contener su orden en la matriz (desde 0 hasta n2 −1. Por ejemplo, si n es 3, 
# deberá crearse la matriz [0, 1, 2] [3, 4, 5] [6, 7, 8] #

numero = int(input("Ingrese un numero entero: "))
matrix = []
for i in range(numero):
    matrix.append([])
    for j in range(numero):
        matrix[i].append(numero * 1 + j)
for i in range(numero):
    print(matrix[i])

# Ejercicio 7 Crea una matriz de n×m y asigna los valores manualmente. El programa debe indicar si la
#  suma de cada columna es el mismo valor.#

numero = int(input("Ingrese un número entero: "))
matrix = int(input("Ingrese un número entero: "))
A = []

for i in range(numero):
    A.append([])
    for j in range(matrix):
        A[i].append(int(input("Elemento ({} {}): ".format(i, j))))

sumas = []
for j in range(matrix):
    suma = 0
    for i in range(numero):
        suma += A[i][j]
    sumas.append(suma)

suma1 = True
for i in range(matrix - 1):
    if sumas[i] != sumas[i + 1]:
        suma1 = False

print("¿La suma de las columnas es igual? {}".format("Sí" if suma1 else "No"))

#Ejercicio 8 Crear un programa determina si la matriz introducida manualmente (tanto sus dimensiones
# como los elementos) se trata de la matriz identidad. Recuerda que la matriz identidad debe 
# ser una matriz cuadrada.#

n = int(input("Numero de Filas"))
m = int(input("Unmero de Columnas"))

A = []
for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(int(input("Elemento ({} {})".format(i,j))))
identidad = True
if n == m:
    for i in range(n):
        for j in range(n):
            if i == j and A [i][j] != 1:
                identidad = False
            if i != j and A [i][j] != 0:
                identidad = False
else:
    identidad = False
    print("La matriz no es cuadrada. No puede ser la matriz identidad")
    print("¿La matriz dijitada es la matriz identidad? {}".format("Sí" if identidad else "No"))


#E jercicio 9
# Dada una matriz formada con listas, realiza un programa que calcule la matriz transpuesta.Solución

A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
T=[]
for i in range(len(A[0])):
    T.append([])
    for j in range(len(A)):
            T[i].append(A[j][i])
for i in range(len(T)):
    for j in range(len(T[0])):
        print(T[i][j], end=" ")
    print("")

#Ejercicio 10 Crea un programa que pida al usuario la dimensión y cree la matriz identidad 
# de orden correspondiente con numpy#

import numpy as np

n = int(input("Ingrese la dimensión de la matriz: "))
I = np.zeros((n, n))

for i in range(n):
    I[i, i] = 1

print(I)
