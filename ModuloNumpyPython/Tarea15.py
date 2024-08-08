#Ejercicio 1
print("----------------------------------------------------------------------")
print("Ejercicio 1")
print("")
#Crea un array unidimensional de 9 elementos y transfórmalo en un array 3D.
# Muestra la dimensión y la shape antes y después del reshape.
"""
Explicación:
import numpy as np: Importa la biblioteca NumPy, que es esencial para trabajar con arrays en Python.
abc = np.array(["a", "b", "c", ...]): Crea un array unidimensional con 9 elementos.
abc.ndim: Devuelve la dimensión del array (1D antes del reshape).
abc.shape: Devuelve la forma del array (una tupla que representa la cantidad de elementos en cada dimensión).
abc.reshape(1, 3, 3): Cambia la forma del array a 3D (1x3x3).
print(...): Muestra la información de dimensiones y formas antes y después del reshape.
"""
import numpy as np

# Crear un array unidimensional de 9 elementos
abc = np.array(["a", "b", "c", "d", "e", "f", "g", "h", "i"])

# Mostrar la dimensión y la forma del array antes del reshape
print("Dimensión (antes):", abc.ndim)
print("Shape (antes):", abc.shape)

# Transformar el array unidimensional en un array 3D
abc = abc.reshape(1, 3, 3)

# Mostrar la dimensión y la forma del array después del reshape
print("Dimensión (después):", abc.ndim)
print("Shape (después):", abc.shape)


#Ejercicio 2
print("----------------------------------------------------------------------")
print("Ejercicio 2")
print("")
#Dados los arrays 2D [[-6, -5], [-4, -3], [-2, -1]] y [[1, 2], [3, 4], [5, 6]], 
# concaténalos de modo que obtengas el array [[1, 2, -6, -5], [3, 4, -4, -3] 
# [5, 6, -2, -1]].
"""
Explicación:

Se crean dos arrays 2D a y b.
np.concatenate((b, a), axis=1): Combina los arrays a y b horizontalmente (a lo largo del eje 1).
El resultado es un array combinado con elementos de b seguidos por los de a en cada fila.
"""
import numpy as np

a = np.array([[-6, -5], [-4, -3], [-2, -1]])
b = np.array([[1, 2], [3, 4], [5, 6]])

# Concatenar los arrays a y b a lo largo del eje 1
c = np.concatenate((b, a), axis=1)

print("Resultado de la concatenación:\n", c)


#Ejercicio 3
print("----------------------------------------------------------------------")
print("Ejercicio 3")
print("")
#Dado el array 2D [[1, 2, 3], [-1, 0, 1], [4, 5, 6], [-4, 0, 4], [3, 2, 1],
#  [-3, 0, 3]], di- vídelo en 3 arrays 2D.
"""
Explicación:

Crea un array 2D a con 6 filas y 3 columnas.
np.array_split(a, 3): Divide el array a en 3 sub-arrays.
Imprime cada sub-array por separado.
"""

import numpy as np

a = np.array([[1, 2, 3], [-1, 0, 1], [4, 5, 6], [-4, 0, 4], [3, 2, 1], [-3, 0, 3]])

# Dividir el array en 3 partes
a1, a2, a3 = np.array_split(a, 3)

print("array a1:\n", a1)
print("\narray a2:\n", a2)
print("\narray a3:\n", a3)


#Ejercicio 4
print("----------------------------------------------------------------------")
print("Ejercicio 4")
print("")
#Dado el array 2D [["ala", "delfín", "arroz"], ["cena", "kayak", "picnic"], 
# ["hoja", "gato", "elle"]], busca las palabras que sean palíndromos.
#PISTA: Necesitarás una función universal.
"""
Explicación:

Crea un array words con palabras.
is_palindrome(word): Define una función que verifica si una palabra es un palíndromo.
np.frompyfunc(...): Convierte la función en una función universal que puede aplicarse a arrays.
np.where(...): Encuentra las posiciones de las palabras que son palíndromos en el array.
Imprime las palabras que son palíndromos.
"""

import numpy as np

words = np.array([["ala", "delfín", "arroz"], ["cena", "kayak", "picnic"], ["hoja", "gato", "elle"]])

def is_palindrome(word):
    """Devuelve si la palabra es palíndroma."""
    word = word.lower()
    isPalindrome = True
    
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            isPalindrome = False
    
    return isPalindrome

# Crear una función universal para identificar palíndromos
np_is_palindrome = np.frompyfunc(is_palindrome, 1, 1)

# Encontrar índices de palíndromos
idx = np.where(np_is_palindrome(words) == True)

print("Las palabras palíndromas son: ")
for i in range(len(idx[0])):
    print(words[idx[0][i], idx[1][i]])


#Ejercicio 5
print("----------------------------------------------------------------------")
print("Ejercicio 5")
print("")
#Dado el array 1D ["cena", "frío", "kayak", "remo", "sol"]], ¿qué índice deberá 
# ocupar el elemento “python” para que se mantenga el orden alfabético?
"""
Explicación:

Se crea un array words ordenado alfabéticamente.
np.searchsorted(words, "python"): Determina la posición en la que "python" debería insertarse para mantener el orden.
Se imprime el índice calculado.
"""
import numpy as np

words = np.array(["cena", "frío", "kayak", "remo", "sol"])

# Encontrar el índice donde "python" debería insertarse para mantener el orden
index = np.searchsorted(words, "python")
print("El índice donde debería insertarse 'python' es:", index)


#Ejercicio 6
print("----------------------------------------------------------------------")
print("Ejercicio 6")
print("")
#Crea un minijuego que piense un número aleatorio entre 1 y 10 y, hasta que no 
# lo aciertes, te pida un número del 1 al 10. Cuando aciertes, tendrá que 
# devolver el número de intentos y la frase: “¡¡¡ENHORABUENA!!! Has acertado 
# el número que había pensado: el {}”. En caso de que falles, el juego deberá 
# mostrar la frase “¡Has fallado! ¡Prueba otra vez!”
"""
Explicación:

random.randint(1, 10): Genera un número aleatorio entre 1 y 4.
El bucle while continúa hasta que el usuario adivine el número.
count lleva la cuenta de los intentos, y se felicita al usuario al acertar.
"""

from numpy import random

print("Voy a pensar un número del 1 al 4. A ver si lo adivinas: ")

n = random.randint(1, 4)
num = int(input())
count = 1

# Bucle hasta que el usuario acierte el número
while num != n:
    print("¡Has fallado! ¡Prueba otra vez!")
    num = int(input())
    count += 1

print("¡¡¡ENHORABUENA!!! Has acertado el número que había pensado: el {}".format(n))
print("Te ha costado {} intentos".format(count))

#Ejercicio 7
print("----------------------------------------------------------------------")
print("Ejercicio 7")
print("")
#Crea un minijuego que piense un array 1D aleatorio de 5 elementos. 
# Los elementos serán números enteros entre 1 y 20. Para cada intento,
#  primero tendrá que pedir 5 números enteros del 1 al 20. El juego nos
#  tendrá que decir cuántos números del array hemos acertado y cuántos
#  números del array están bien colocados. El
#juego no termina hasta que no se hayan acertado todos los números 
# pensados en la posición correspondiente. Al acabar, se tendrá que 
# mostrar la frase: “¡¡¡ENHORABUENA!!! Has acertado el array que había pensado: {}”
"""
Explicación:

random.randint(9, size=3): Genera un array aleatorio de 5 elementos entre 0 y 9.
Se crea un bucle que sigue hasta que se acierten todas las posiciones correctamente.
Se pide al usuario que introduzca números y se comparan con los del array generado.
Se da retroalimentación sobre cuántos valores y posiciones son correctos.

"""
from numpy import random

nums = random.randint(9, size=3)
print(nums)

value = 0
position = 0

# Bucle hasta que se acierten todos los números en la posición correcta
while position != 3:
    sol = []
    value = 0
    position = 0

    for i in range(3):
        num = int(input("Introduce el elemento en la posición {} ".format(i)))
        sol.append(num)
        if num in nums:
            value += 1
        if num == nums[i]:
            position += 1

    print("Tu respuesta ha sido", sol)
    print("Has acertado {} valores".format(value))
    print("Has acertado {} posiciones".format(position))

print("¡¡¡ENHORABUENA!!! Has acertado el array que había pensado:", nums)


#Ejercicio 8
print("----------------------------------------------------------------------")
print("Ejercicio 8")
print("")
#A partir de la lista [-3, -2, -1, 0, 1, 2, 3], genera dos arrays aleatorios 
# 2D de size = (3, 4) y súmalos.
"""
Explicación:

Se crea una lista x con números enteros.
random.choice(x, size=(3, 4)): Genera dos arrays 2D de tamaño 3x4 con valores aleatorios tomados de x.
Imprime los arrays y su suma.

"""

from numpy import random

x = [-3, -2, -1, 0, 1, 2, 3]

# Generar dos arrays aleatorios 2D y sumarlos
a = random.choice(x, size=(3, 4))
b = random.choice(x, size=(3, 4))

print("a =\n", a)
print("b =\n", b)
print("a + b =\n", a + b)


#Ejercicio 9
print("----------------------------------------------------------------------")
print("Ejercicio 9")
print("")
#Crea una función universal que dado un array de strings devuelva el número 
# total de vocales de cada string.
"""
Explicación:

total_vowels(w): Cuenta cuántas vocales hay en una palabra dada.
np.frompyfunc(...): Convierte la función en una función universal que puede aplicarse a arrays.

"""
import numpy as np

def total_vowels(w):
    """Devuelve el total de vocales de una palabra."""
    vowels = 0
    for c in w:
        if c in ["a", "e", "i", "o", "u"]:
            vowels += 1
    return vowels

# Crear una función universal para contar vocales en un array de strings
np_total_vowels = np.frompyfunc(total_vowels, 1, 1)

# Crear un array de ejemplo
words = np.array(["hola", "mundo", "python", "numpy"])

# Aplicar la función universal al array
vowel_counts = np_total_vowels(words)

# Imprimir los resultados
print(vowel_counts)


#Ejercicio 10 
print("----------------------------------------------------------------------")
print("Ejercicio 10")
print("")
# Crea una función universal que dados un array 1D de valores string y conjunto de strings, compruebe para 
# cada elemento del array 1D, si está presente o no en el conjunto.
"""
Explicación:

is_in_set(element, s): Define una función que verifica si un elemento está presente en un conjunto s. Devuelve True si el elemento está en el conjunto, de lo contrario devuelve False.
np.frompyfunc(is_in_set, 2, 1): Convierte is_in_set en una función universal (np_is_in_set) que puede aplicarse a arrays de NumPy. Aquí, 2 indica que la función toma dos argumentos (el elemento y el conjunto) y 1 indica que la función devuelve un valor.
Uso típico:

Puedes aplicar np_is_in_set a un array 1D de strings y a un conjunto para verificar si cada elemento del array está presente en el conjunto.

"""

import numpy as np

def is_in_set(element, s):
    """Devuelve si un elemento pertenece al conjunto s."""
    if element in s:
        return True
    return False

# Crear una función universal que verifica la pertenencia de elementos en un conjunto
np_is_in_set = np.frompyfunc(is_in_set, 2, 1)

#Ejemplo de Uso#
words = np.array(["apple", "banana", "cherry", "date"])
fruit_set = {"apple", "date", "fig"}

# Aplicar la función universal al array y al conjunto
result = np_is_in_set(words, fruit_set)

print(result)  # Muestra un array con valores True o False
"""
Explicación del ejemplo:

Se crea un array words con nombres de frutas.
Se define un conjunto fruit_set que contiene algunas frutas.
np_is_in_set(words, fruit_set): Aplica la función universal para verificar si cada elemento de words está en fruit_set.
El resultado es un array que contiene True o False según si cada fruta del array está en el conjunto.
Este ejercicio es útil para realizar búsquedas y comprobaciones rápidas en grandes volúmenes de datos.
"""