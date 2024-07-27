# -*- coding: utf-8 -*-
"""solucionDataFrameEjercicioEjemplo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z7cBKujrMuKitqDzE8QjyPXPA_7joIqB

# Un sueño de los más extraño

Una vez levaron el ancla y pusieron rumbo a Isla Torva, solo quedaba esperar hasta avistar tierra. El viaje prometía ser tranquilo, de modo que tanto Pyerce como Pym insistieron a su capitán que siguiera descansando y les dejara a ellos encargarse de llegar a su destino, pues habiendo derrotado al Valrock, se había merecido el descanso tras haber luchado solo en tan ardua batalla contra el monstruo más magestuoso de todos los mares.

Pyratilla al principio se opuso, pues sentía que era su deber estar despierto y atento en caso de que apareciera otro enemigo, pero luego pensó que realmente no es que se lo mereciera sino que necesitaba dicho descanso. De este modo, dejó a sus tripulantes encargados de llegar a Isla Torva, pero en caso de necesidad, les ordenó que lo avisaran.

Y así fue como Pyratilla se encerró en su camarote, se metió bajo las sábanas y se quedó frito.

---

Pyratilla despertó, pero no lo hizo en su camarote. Lo último que recordaba era haberse metido en la cama con la intención de descansar mientras su tripulación se encargaba de llegar a su destino: Isla Torva. Por tanto, no conseguía entender como había llegado a la habitación blanca en la que se encontraba.

Miró a su alrededor y lo único que veía era su cama sobre la cuál estaba tendido y un escritorio de madera pegado a una de las 4 paredes. Observó que no había ni puertas ni ventanas. La luz provenía de una lámpara del techo.

Se frotó los ojos una y otra vez e incluso se pellizco varias veces la mano hasta dejársela roja para ver si estaba soñando. Parecía que no, pues siempre que abría los ojos volvía a ver la cama, el escritorio y la lámpara. Decidió levantarse y ver más de cerca ese bonito escritorio de madera.

Al levantarse de la cama logró ver que sobre el escritorio había 2 hojas de papel escritas. Se acercó rápidamente para leer las palabras negras que destacaban sobre el fondo blanco. En la primera hoja podía leerse "Vamos a jugar a un juego. Las reglas son sencillas: sigue las instrucciones que aparecerán en la otra hoja y conseguirás salir de aquí. En total hay 10 pruebas que debes superar numeradas del 1 al 10. Si las respondes todas correctamente, abrirás una salida. En caso contrario... no."

Sorprendido y un poco asustado observó la otra hoja. En ella solamente se leía: "Carga el csv llamado `characters-hp` en una variable llamada `hp_df`".

¡Ayuda a Pyratilla a cargar el csv (que previamente debes haber guardado en tu carpeta de Google Drive) en la variable `hp_df`!

PISTA: A la hora de cargar el dataset con el método que creas conveniente, vas a tener que configurar dos parámetros: el parámetro `sep` tiene que estar igualado a `";"`, y el parámetro `encoding` debe estar igualado a `"Windows-1252"`. De lo contrario, la carga del csv `characters-hp` te devolverá error.
"""

#from google.colab import drive
#drive.mount('/content/drive')

# Para obtener el encoding del csv (pues no se encontraba en utf-8)
import chardet
rawdata = open("CargaArchivosPython\ArchivosCSV\charactershp-220809-170900.csv", 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']
print(charenc)

import pandas as pd
hp_df = pd.read_csv("CargaArchivosPython\ArchivosCSV\charactershp-220809-170900.csv",
                    sep = ";", encoding = "Windows-1252")

"""Una vez cargado el dataset, las palabras mágicamente desapariecieron poco a poco para dar lugar a otras. Ahora, en la segunda hoja se podía leer lo siguiente:

Resuelve las 10 siguientes pruebas:

1. Calcula el total de observaciones del csv que has guardado en la variable `hp_df`
2. Da la instrucción para visualizar las 10 primeras observaciones del dataframe
3. Averigua el índice de la columna llamada `Id`. Después, guarda en la variable `hp_df` todas las filas y todas las columnas salvo la columna que lleva por nombre `Id`. En otras palabras, elimina la columna que lleva por nombre `Id` del dataframe original haciendo uso del método `.columns()`
4. Tras el cambio, ¿de cuántas variables consta el dataframe `hp_df`?
5. Di el valor de la variable `Species` para el personaje llamado `Dobby` sin usar el método `.query()`
6. Usa el método `.query()` para obtener únicamente las observaciones cuyo valor de la variable `Job` es `Student` y guarda este dataframe filtrado en la variable `hp_students`
7. Fíjate que los nombres de las filas del dataframe `hp_students` siguen siendo los originales. Renombra las filas para que vayan del 1 al número total de observaciones que haya en `hp_students`. PISTA: Para acceder a los índices del dataframe puedes llamar al atributo `index`. Se trata de que sustituyas el original por una lista que contega como entradas los números que van del 1 al número total de observaciones que tiene el dataframe `hp_students`
8. ¿Qué proporción de estudiantes hay? La proporción se calcula como el número de estudiantes entre el número total de observaciones.
9. ¿Cuál es el valor de `Hair colour` para la observación 30 de `hp_students`? Calcúlalo usando el método `.loc[]`
10. Obtén la cantidad de colores diferentes que hay para la variable `Eye colour` en el dataframe `hp_students`. Recuerda que `nan` no es un color. ¿Cuántos estudiantes no tienen un valor para la variable `Eye colour`?

¡Ayuda a Pyratilla a resolver correctamente las 10 pruebas para salir de la habitación blanca!
"""
### Prueba 1
print("Prueba 1")
#Calcula el total de observaciones del csv que has guardado en la variable `hp_df`


print("El total de observaciones en hp_df es", hp_df.shape[0])

### Prueba 2
print("Prueba 2")

#Da la instrucción para visualizar las 10 primeras observaciones del dataframe


print(hp_df.head(10))

### Prueba 3
print("Prueba 3")

#Averigua el índice de la columna llamada `Id`. Después, guarda en la variable 
# `hp_df` todas las filas y todas las columnas salvo la columna que lleva por 
# nombre `Id`. En otras palabras, elimina la columna que lleva por nombre `Id` 
# del dataframe original haciendo uso del método `.columns()`
for c in hp_df.columns:
  print(c)
print("Al ser la primera columna, su índice es el 0")

hp_df = hp_df[hp_df.columns[1:]]

### Prueba 4
print("Prueba 4")

#Tras el cambio, ¿de cuántas variables consta el dataframe `hp_df`?

print("Ahora, el dataframe hp_df consta de {} columnas".format(hp_df.shape[1]))

### Prueba 5
print("Prueba 5")
##Di el valor de la variable `Species` para el personaje llamado `Dobby` sin usar el método `.query()`
# Accedemos a la fila del personaje llamado Dobby
hp_df[hp_df["Name"] == "Dobby"]
hp_df.loc[hp_df["Name"] == "Dobby", "Species"]
print("Podemos observar que el valor para la variable Species de esta observación es House elf")

### Prueba 6
print("Prueba 6")
##Usa el método `.query()` para obtener únicamente las observaciones cuyo valor 
# de la variable `Job` es `Student` y guarda este dataframe filtrado en la 
# variable `hp_students`

hp_students = hp_df.query('Job == "Student"')
print(hp_students)

### Prueba 7
print("Prueba 7")

#Fíjate que los nombres de las filas del dataframe `hp_students` siguen 
# siendo los originales. Renombra las filas para que vayan del 1 al número 
# total de observaciones que haya en `hp_students`.

#PISTA: Para acceder a los índices del dataframe puedes llamar al atributo 
# `index`. Se trata de que sustituyas el valor original de dicho atributo por
#  una lista que contega como entradas los números que van del 1 al número total 
# de observaciones que tiene el dataframe `hp_students`

hp_students.index = list(range(1, hp_students.shape[0] + 1))

print(hp_students)

### Prueba 8
print("Prueba 8")

#¿Qué proporción de estudiantes hay? La proporción se calcula como el 
# número de estudiantes entre el número total de observaciones.

print(hp_students.shape[0] / hp_df.shape[0])

### Prueba 9
print("Prueba 9")

#¿Cuál es el valor de `Hair colour` para la observación 30 de 
# `hp_students`? Calcúlalo usando el método `.loc[]`

print(hp_students.loc[30, "Hair colour"])

### Prueba 10
print("Prueba 10")

#Obtén la cantidad de colores diferentes que hay para la variable 
# `Eye colour` en el dataframe `hp_students`. Recuerda que `nan` no es un 
# color. ¿Cuántos estudiantes no tienen un valor para la variable `Eye colour`?

print(len(hp_students["Eye colour"].dropna().unique()))
print(hp_students[hp_students["Eye colour"].isnull() == True].shape[0])

print(hp_students["Eye colour"].dropna().unique())
print(hp_students[hp_students["Eye colour"].isnull() == True])

## Desenlace

#Tras completar la última prueba, las palabras volvieron a esfumarse lentamente. Tras unos instantes, en la hoja aparecieron las últimas palabras:

#"ENHORABUENA! Parece ser que has superado con éxito todas las pruebas. Lo prometido es deuda: ahí tienes tu salida..."

#Pyratilla alzó la vista y vio que al lado del escritorio había aparecido una puerta de la misma madera que la mesa donde había estado resolviendo todas las pruebas. Nuestro querido capitán lentamente acercó la mano al pomo, lo giró con suavidad y...

#Agitado, Pyratilla se levantó sobresaltado de la cama. "Todo ha sido un sueño", pensó. No dejaba de darle vueltas a qué podría haber habido tras esa puerta de madera. Instantes después decidió que iba a pasar del tema, pues de fondo se oían los gritos de Pym dicendo "¡Tierra a la vista! ¡Tierra a la vista!"

#Salió de la cama de un salto, se colocó el sombrero y se preparó para una nueva aventura en Isla Torva. Todo lo anterior se quedó en solo un sueño, pero de lo más extraño.


