# -*- coding: utf-8 -*-
"""Tema11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SVna2SuGYoft1u1OWcgIPLq6w5hIldpO

# Funciones `lambda`

## Funciones `lambda`

Son un tipo especial de funciones de `Python` que tienen la sintaxis siguiente
"""

lambda parámetros: expresión

"""- Son útiles para ejecutar funciones en una sola línea
- Pueden tomar cualquier número de argumentos
- Tienen una limitación: solamente pueden contener una expresión

Veamos algunos ejemplos

---

#### Ejemplo 1

Función que dado un número, le suma 10 puntos más:
"""

plus10 = lambda x: x + 10
plus10(5)

"""---

#### Ejemplo 2

Función que calcula el producto de dos números:
"""

prod = lambda x, y: x * y

prod(5, 10)

"""---

#### Ejemplo 3

Función que dados 3 números, calcula el discriminante de la ecuación de segundo grado.

Recordemos que dada una ecuación de segundo grado de la forma $$ax^2 + bx + c = 0$$

el discriminante es $$\triangle =  b^2-4ac$$

y dependiendo de su signo, nos indica cuantas soluciones reales va a tener la ecuación:

- Si $\triangle > 0$, entonces hay dos soluciones diferentes
- Si $\triangle = 0$, entonces hay dos soluciones que son iguales
- Si $\triangle < 0$, entonces no hay solución
"""

discriminante = lambda a, b, c: b ** 2 - 4 * a * c
discriminante(1, 2, 1) # Se corresponde a la ecuación x^2 + 2x + 1 = 0, cuya única solución es x = -1

"""---

## La función `filter()`

- Aplica una función a todos los elementos de un objeto iterable
- Devuelve un objeto generador, de ahí que usemos la función `list()` para convertirlo a lista
- Como output, devuelve los elementos para los cuales el aplicar la función ha devuelto `True`

Con la ayuda de las funciones `lambda`, apliquemos `filter()` para quedarnos con los números múltiplos de 7 de la siguiente lista llamada `nums`
"""

nums = [49, 57, 62, 147, 2101, 22]
list(filter(lambda x: (x % 7 == 0), nums))

"""La función proporcionada a `filter()` no tiene por qué ser `lambda`, sino que puede ser una ya existente, o bien una creada por nosotros mismos.

Con las siguientes líneas de código vamos a obtener todas las palabras cuya tercera letra sea `s` haciendo uso de `filter()` y la función creada `third_letter_is_s()`:
"""

def third_letter_is_s(word):
  return word[2] == "s"

words = ["castaña", "astronomía", "masa", "bolígrafo", "mando", "tostada"]
list(filter(third_letter_is_s, words))

"""## La función `reduce()`

- Aplica continuamente una misma función a los elementos de un objeto iterable

    1. Aplica la función a los primeros dos elementos
    2. Aplica la función al resultado del paso anterior y el tercer elemento
    3. Aplica la función al resultado del paso anterior y el cuarto elemento
    4. Sigue así hasta que solo queda un elemento
- Devuelve el valor resultante

Con la ayuda de las funciones `lambda`, apliquemos `reduce()` para calcular el producto de todos los elementos de una lista
"""

from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
reduce(lambda x, y: x * y, nums)

"""De nuevo, la función proporcionada a `reduce()` no tiene por qué ser `lambda`, sino que puede ser una ya existente o bien, una creada por nosotros mismos.

Con las siguientes líneas de código, vamos a obtener el máximo de una lista dada, haciendo uso de `reduce()` y la función creada `bigger_than()`:
"""

def bigger_than(a, b):
  if a > b:
    return a
  return b

bigger_than(14, 7)

nums = [-10, 5, 7, -3, 16, -30, 2, 33]
reduce(bigger_than, nums)

"""## La función `map()`

- Aplica una misma función a todos los elementos de un objeto iterable
- Devuelve un objeto generador, de ahí que usemos la función `list()` para convertirlo a lista
- Como output, devuelve el resultado de aplicar la función a cada elemento

Con la ayuda de las funciones `lambda`, apliquemos `map()` para calcular las longitudes de las siguientes palabras
"""

words = ["zapato", "amigo", "yoyo", "barco", "xilófono", "césped"]
list(map(lambda w: len(w), words))

"""Sin embargo, para este caso en concreto no haría falta usar funciones `lambda`, pues podríamos hacer directamente"""

list(map(len, words))

"""## La función `sorted()`

- Ordena los elementos del objeto iterable que indiquemos de acuerdo a la función que pasemos por parámetro
- Como output, devuelve una permutación del objeto iterable ordenado según la función indicada

Con la ayuda de las funciones `lambda`, apliquemos `sorted()` para ordenar la lista `words` en función de las longitudes de las palabras en orden descendente.
"""

words = ["zapato", "amigo", "yoyo", "barco", "xilófono", "césped"]
sorted(words, key = lambda x: len(x), reverse = True)

"""De nuevo, podríamos en este caso evitar el uso de las funciones `lambda` haciendo uso del siguiente código:"""

sorted(words, key = len, reverse = True)

"""**Observación.** Si quisiésemos ordenar en orden ascendente, simplemente tendríamos que indicar `reverse = False`, que al ser el valor por defecto, bastaría con omitir dicho parámetro.

**Observación.** Si el tipo de objeto a ser ordenado es un string y no indicamos parámetro `key`, entonces se ordenan por defecto: orden alfabético ascendente.
"""

sorted(words, key = len)

sorted(words)
