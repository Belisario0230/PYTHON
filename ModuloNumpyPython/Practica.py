#Claro! Te explicaré cómo leer los arrays en cada uno de los niveles que mencionaste:
"""
Unidimensional (1D):
Para leer un array unidimensional, simplemente accede a sus elementos mediante índices. Por ejemplo:
Python

unidimensional = [1, 2, 3, 4]
print(unidimensional[0])  # Imprime el primer elemento (1)
Código generado por IA. Revisar y usar cuidadosamente. Más información sobre preguntas frecuentes.
Bidimensional (2D):
Para leer un array bidimensional, utiliza dos índices: uno para la fila y otro para la columna. Por ejemplo:
Python

import numpy as np
bidimensional = np.array([[1, 2, 3], [4, 5, 6]])
print(bidimensional[1, 2])  # Imprime el elemento en la segunda fila y tercera columna (6)
Código generado por IA. Revisar y usar cuidadosamente. Más información sobre preguntas frecuentes.
Tridimensional (3D):
Para leer un array tridimensional, necesitas tres índices: uno para la matriz, otro para la fila y otro para la columna. Por ejemplo:
Python

tridimensional = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tridimensional[1, 0, 1])  # Imprime el elemento en la segunda matriz, primera fila y segunda columna (6)
Código generado por IA. Revisar y usar cuidadosamente. Más información sobre preguntas frecuentes.
Cuatridimensional (4D):
Similar al 3D, pero con un índice adicional. Por ejemplo:
Python

cuatridimensional = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print(cuatridimensional[1, 1, 0, 1])  # Imprime el elemento en la segunda matriz, segunda fila, primera columna y segunda columna (14)
"""

import numpy as np

# Listar todos los métodos y atributos de NumPy
metodos_numpy = dir(np)

# Enumerar e imprimir los métodos y atributos
for indice, metodo in enumerate(metodos_numpy):
    print(f"{indice}: {metodo}")

# Buscar el método 'random' en la lista de métodos
metodo_choice = [metodo for metodo in metodos_numpy if 'shuffle' in metodo]

print("\nMétodos relacionados con shuffle':")
for metodo in metodo_choice:
    print(metodo)

