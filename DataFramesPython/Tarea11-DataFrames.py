#Ejercicio 1
#Crea un dataframe con 15 filas y 2 columnas. La primera columna se llamará x, 
# la segunda y. Cada entrada será un número real a tu elección. Guarda el 
# dataframe en una variable llamada points.

import pandas as pd
dataFrame = {
    "x": [0, 0.30, -0.6, -0.85, 1, 1.35, -1.55, -1.75, 2, 2.35, -2.53, -2.85, 3, 3.45, -3.59],
    "y": [0, 0.25, 0.5, -0.75, -1, 1.25, 1.5, -1.75, -2, 2.25, 2.5, -2.75, -3, 3.25, 3.5]
}
points = pd.DataFrame(data=dataFrame)
print(points)

#Ejercicio 2
#Del dataset points, muestra las filas cuyo valor en la columna x sea positivo.
points[points["x"]>0]
print(points[points["x"]>0])

#Ejercicio 3
#Del dataset points, muestra las filas cuyo valor en la columna y sea negativo. 
# Usa el método .query().
points[points["y"]<0]
print(points[points["y"]<0])

#Ejercicio 4
#Del dataset points, muestra las observaciones cuyos puntos (x, y) pertenezcan 
# al primer cuadrante. Usa el método .query().
primer_cuadrante = points.query("x >= 0 and y >= 0")

print(primer_cuadrante)

#Ejercicio 5
#Del dataset points, muestra las observaciones de la forma: “El punto ({x}, {y}) 
# {no/sí} pertenece al primer cuadrante”.
import pandas as pd

for i, row in points.iterrows():
    x, y = row["x"], row["y"]
    pertenece_primer_cuadrante = "sí" if x > 0 and y > 0 else "no"
    print(f"El punto ({x:.2f}, {y:.2f}) {pertenece_primer_cuadrante} pertenece al primer cuadrante")
    print("")

#Ejercicio 6
#Crea un dataframe con 10 filas y 4 columnas. La primera columna se llamará word; 
# la segunda, length; la tercera, vowels; y la última, consonants. 
# La columna words contendrá las siguientes 10 palabras: “euro”, “diez” “algas”, 
# “broma”, “cicuta”, “fatiga”, “nachos”, “jadeos”, “hazañas”, “boutique”. Las 
# columnas length, vowels y consonants contendrán, respectivamente, la longitud,
#  el total de vocales y el total de consonantes. Guarda el dataframe en la 
# variable words.
import pandas as pd

# Crear una lista con las palabras
words_list = ["euro", "diez", "algas", "broma", "cicuta", "fatiga", "nachos", "jadeos", "hazañas", "boutique"]

# Crear un diccionario con las columnas y sus valores
data = {
    "word": words_list,
    "length": [len(word) for word in words_list],
    "vowels": [sum(1 for char in word if char.lower() in "aeiou") for word in words_list],
    "consonants": [sum(1 for char in word if char.lower() not in "aeiou") for word in words_list]
}

# Crear el DataFrame
words = pd.DataFrame(data)

# Mostrar el DataFrame
print(words)

#Ejercicio 7
#Muestra las 10 observaciones de words con el formato “La palabra {word} tiene
#  {length} letras, de las cuales {vowels} son vocales y {consonants} 
# consonantes”.
#1
for row in words.itertuples():
    print("La palabra {} tiene {} letras, de las cuales {} son vocales y {} consonantes".format(row.word, row.length, row.vowels, row.consonants))

#Ejercicio 8
#Muestra aquellas observaciones de words que tienen el mismo número de 
#vocales y consonantes. Usa el método .query().
mismo_numero_vocales_consonantes = words.query("vowels == consonants")
print(mismo_numero_vocales_consonantes)

#Ejercicio 9
#Investiga el método .sort_values() para ordenar las observaciones según 
# la longitud de las palabras en orden descendente.
# Supongamos que ya tienes el DataFrame 'words' con las palabras y sus atributos
print(words.sort_values(by="length", ascending=False))

#Ejercicio 10
#Convierte la columna vowels a lista y, con sorted() ordénala de mayor a menor. 
# Investiga para ello el método .tolist().
# Supongamos que ya tienes el DataFrame 'words' con las palabras y sus atributos
print(sorted(words["vowels"].tolist(), reverse=True))
