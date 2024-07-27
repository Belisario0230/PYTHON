import pandas as pd

print("dataframe 1 forma de hacer")
data = {"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]}
df1 = pd.DataFrame(data = data)
print(df1)
print("")
print("")

print("dataframe 2 forma de hacer apartir de una lista de listas")
df2 = pd.DataFrame(data = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],
                   columns = ["x", "y"])
print(df2)
print("")
print("")

print("dataframe 3 forma de hacer modificando nombre de las filas")
df3 = pd.DataFrame(data = data, index = ["obs1", "obs2", "obs3", "obs4", "obs5"])
print(df3)
print("")
print("")

print("dataframe 4 forma de hacer apartir de una lista de diccionarios")
data = [{"x": 1, "y": 2},
        {"x": 2, "y": 4},
        {"x": 3, "y": 6},
        {"x": 4, "y": 8},
        {"x": 5, "y": 10}]
df4 = pd.DataFrame(data = data)
print(df4)
print("")
print("")

print("#dataframe 5 hacuendo uso de la funcion zip#")
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

data = list(zip(x, y))
print(data)
print("")
print("")
df5 = pd.DataFrame(data, columns = ["x", "y"])
print(df5)

# Para crear dataframe con el metodo from_dict()#
d = {"a": [1, 2, 3],
     "b": [4, 5, 6],
     "b1": [7, 8, 9]}

df = pd.DataFrame.from_dict(d)
print(df)

# Para crear dataframe con el metodo orient #
d = {"fila1": [1, 4, 7],
     "fila2": [2, 5, 8],
     "fila3": [3, 6, 9]}

df = pd.DataFrame.from_dict(d, orient = "index", columns = ["A", "B", "C"])
print(df)

#metodo shape#
df.shape

nrows = df.shape[0]
ncols = df.shape[1]
print("El número de filas de df es", nrows)
print("El número de columnas de df es", ncols)

#metodo size#
df.size

df.shape[0] * df.shape[1] == df.size

#metodo ndim #
df.ndim

#SUBDATAFRAMES#
#COLUMNAS#

# Dado un dataframe, podemos seleccionar una columna en particular de diversas formas:

# Indicando el nombre de la columna entre claudators, []
# Con el método .columns[]
# Con el método .loc[] (por nombre o etiqueta)
# Con el método .iloc[] (por posición)

fdata = {"Name": ["Alicia", "Bill", "Carlos", "Diana"],
        "Age": [22, 28, 19, 34],
        "Pet": [True, False, False, True],
        "Height": [157, 190, 175, 164],
        "Birthday": ["Mayo", "Junio", "Agosto", "Diciembre"]}
df = pd.DataFrame(data = fdata, index = ["obs1", "obs2", "obs3", "obs4"])

# Seleccionamos la columna Birthday por nombre
print(df["Birthday"])

# Seleccionamos la columna Birthday con el método .columns[]
print(df[df.columns[4]])

# Seleccionamos la columna Birthday con el método .loc[]
print(df.loc[:, "Birthday"])

 #Seleccionamos la columna Birthday con el método .iloc[]
print(df.iloc[:, 4])

# Seleccionamos las columnas Name y Age por nombre
print(df[["Name", "Age"]])

# Seleccionamos las columnas Name y Age con el método .columns[]
print(df[df.columns[[0, 1]]])

print(df[df.columns[0:2]])

# Seleccionamos las columnas Name y Age con el método .loc[]
print(df.loc[:, ["Name", "Age"]])

print(df.loc[:, "Name":"Age"])

# Seleccionamos las columnas Name y Age con el método .iloc[]
print(df.iloc[:, [0, 1]])

print(df.iloc[:, 0:2])


#ejercicio#
def is_palindrome(word): 
  """
  Devuelve si la palabra word es palíndroma.
  Args:
    word: Palabra en formato string
  Returns:
    isPalindrome: Booleano
  """
  word = word.lower()
  l = []
  isPalindrome = True
  for c in word: 
    l.append(c) 
  n = len(l)
  for i in range(int(n / 2)):
    if l[i] != l[n - (i + 1)]: 
      isPalindrome = False
  return isPalindrome

words = ["sol", "ala", "cama", "duro", "bueno", "kayak", "marea", "rotor", "misterio", "acurruca"]
data = {"word": words,
        "length": map(len, words),
        "start": map(lambda w: w[0], words),
        "end": map(lambda w: w[-1], words),
        "isPalindrome": map(is_palindrome, words)}

import pandas as pd
words = pd.DataFrame(data)
words = words.set_index("word")
words.index.names = [None]

words.head()

for col in list(words):
  print("=== {} ===".format(col.upper()))
  print(words[col], end = "\n\n\n")

words2 = words.iloc[:, 1:]
words2.head()


#FILAS#
#Dado un dataframe, podemos seleccionar una fila en particular de diversas formas:

#Con el método .loc[] (por nombre o etiqueta)
#Con el método .iloc[] (por posición)

# Seleccionamos la edad de la segunda observación con el método .loc[]
print("Solo imprime las filas indicadas")
print(df.loc["obs1", "Age"])

# Seleccionamos la edad de la segunda observación con el método .iloc[]
print(df.iloc[1, 1])

# Seleccionamos la segunda y tercera fila y las columnas nombre y cumpleaños
# Con el método .loc[]
print(df.loc["obs2":"obs3", ["Name", "Birthday"]])

# Con el método .iloc[]
print(df.iloc[1:3, [0, 4]])

#FILAS Y COLUMNAS COMBINADAS DATAFRAMES#
#Para seleccionar un elemento en concreto, hay que indicar la fila y la columna y lo podemos hacer de dos formas:

#Con el método .loc[] (por nombre o etiqueta)
#Con el método .iloc[] (por índice)

# Seleccionamos la edad de la segunda observación con el método .loc[]
print(df.loc["obs2", "Age"])

# Seleccionamos la edad de la segunda observación con el método .iloc[]
print(df.iloc[1, 1])

# Seleccionamos la segunda y tercera fila y las columnas nombre y cumpleaños
# Con el método .loc[]
print("Imprime las filas obs2 y obs3 y las columnas name y birthday")
print(df.loc["obs2":"obs3", ["Name", "Birthday"]])

# Con el método .iloc[]
print(df.iloc[1:3, [0, 4]])

import pandas as pd

# Datos iniciales
dfruta = {"fruit": ["sandía", "melón", "manzana", "cerezas", "plátano", "pera", "melocotón", "fresas"],
          "count": [1, 1, 6, 10, 3, 6, 4, 10]}

print("METODOS DE DATAFRAMES")

# Creación del DataFrame
dfrutas = pd.DataFrame(dfruta)
print("DataFrame inicial:")
print(dfrutas)

# METODO HEAD MUESTRA LOS PRIMEROS ELEMENTOS
print("\nMétodo head (primeros 4 elementos):")
print(dfrutas.head(4))

# METODO TAIL MUESTRA LOS ULTIMOS ELEMENTOS
print("\nMétodo tail (últimos 3 elementos):")
print(dfrutas.tail(3))

# METODO COPY aquí sería una referencia, es decir, cambia al DataFrame original
fruits = dfrutas
fruits.iloc[6, 0] = "naranja"
print("\nDataFrame después de cambiar 'melocotón' a 'naranja':")
print(fruits)

# METODO COPY MUESTRA UNA COPIA LITERAL DF
fruits_copy = dfrutas.copy()
print("\nCopia del DataFrame original:")
print(fruits_copy)

# METODO RENOMBRE LAS COLUMNAS DF (AQUÍ SOLO CREA UNA VARIABLE PERO NO CAMBIA NADA)
df_renamed = dfrutas.rename(columns={"fruit": "fruta", "count": "cantidad"})
print("\nDataFrame con columnas renombradas (sin inplace):")
print(df_renamed)

# Cambiamos el nombre de las columnas al DataFrame original
dfrutas.rename(columns={"fruit": "fruta", "count": "cantidad"}, inplace=True)
print("\nDataFrame con columnas renombradas (con inplace):")
print(dfrutas)

# Cambiamos el nombre de las FILAS al DataFrame original PERO AQUÍ SOLO SE CREA PERO NO CAMBIA NADA
df_renamed_rows = dfrutas.rename(index={0: "obs1", 1: "obs2", 7: "obs8"})
print("\nDataFrame con filas renombradas (sin inplace):")
print(df_renamed_rows)

# Cambiamos el nombre de las filas al DataFrame original
dfrutas.rename(index={0: "obs1", 1: "obs2", 7: "obs8"}, inplace=True)
print("\nDataFrame con filas renombradas (con inplace):")
print(dfrutas)

# METODO COLUMNS MUESTRA LAS COLUMNAS
print("\nColumnas del DataFrame:")
print(dfrutas.columns)

# Cambiamos el nombre de las columnas directamente
dfrutas.columns = ["FRUTA", "CANTIDAD"]
print("\nDataFrame con columnas renombradas directamente:")
print(dfrutas)

# METODO INSERT INSERTA UNA POSICION CUALQUIERA DATAFRAME
dfrutas.insert(loc=2, column="PRECIO", value=[2.50, 2.00, 0.35, 0.10, 0.35, 0.20, 0.15, 0.05])
print("\nDataFrame después de insertar la columna 'PRECIO':")
print(dfrutas)

# METODO .POP ELIMINA COLUMNA INDICADA POR PARAMETRO
# Añadimos una columna 'COLOR' para demostrar el método .pop
dfrutas["COLOR"] = ["rojo", "verde", "rojo", "rojo", "amarillo", "verde", "naranja", "rojo"]
column_popped = dfrutas.pop("COLOR")
print("\nDataFrame después de eliminar la columna 'COLOR':")
print(dfrutas)
print("\nColumna 'COLOR' eliminada:")
print(column_popped)

# Volvemos a añadir la columna recientemente eliminada al final del DataFrame
dfrutas["COLOR"] = column_popped
print("\nDataFrame después de volver a añadir la columna 'COLOR':")
print(dfrutas)

# METODO RANK DESDE LA PRIMERA HASTA LA ULTIMA DE UNA COLUMNA ORDENA ASCENDENTE
dfrutas["RANKING_FRUTA"] = dfrutas["FRUTA"].rank()
print("\nDataFrame con ranking ascendente de 'FRUTA':")
print(dfrutas)

# ESTE METODO RANK ORDENA DESCENDENTE
dfrutas["RANKING_PRECIO"] = dfrutas["PRECIO"].rank(ascending=False)
print("\nDataFrame con ranking descendente de 'PRECIO':")
print(dfrutas)

# El método .nunique() devuelve el conteo de cuántos valores únicos hay en cada columna
print("\nNúmero de valores únicos en cada columna:")
print(dfrutas.nunique())

# Dada una columna de un DataFrame, el método .unique() devuelve un array con los valores únicos de dicha columna
print("\nValores únicos en la columna 'COLOR':")
print(dfrutas["COLOR"].unique())
print("\nValores únicos en la columna 'PRECIO':")
print(dfrutas["PRECIO"].unique())

# El método .duplicated() nos ayuda a analizar los valores duplicados
bool_duplicated = dfrutas["CANTIDAD"].duplicated(keep=False)
print("\nFilas con valores duplicados en 'CANTIDAD':")
print(dfrutas[bool_duplicated])

# El método .drop_duplicates() elimina los duplicados del DataFrame
df_without_duplicates = dfrutas.drop_duplicates(subset="CANTIDAD", keep="first")
print("\nDataFrame después de eliminar duplicados en 'CANTIDAD':")
print(df_without_duplicates)

# El método .nsmallest() nos devuelve las n filas con menor valor de la columna que indiquemos por parámetro
print("\nLas 3 observaciones con menor precio:")
print(dfrutas.nsmallest(3, "PRECIO"))

# El método .nlargest() nos devuelve las n filas con mayor valor de la columna que indiquemos por parámetro
print("\nLas 5 observaciones con mayor cantidad:")
print(dfrutas.nlargest(5, "CANTIDAD"))

# El método .dtypes nos indica de qué tipo es cada columna del DataFrame
print("\nTipos de datos de cada columna:")
print(dfrutas.dtypes)

#Bucles y Dataframes inicio#
d = {"name": ["Juan Gabriel", "María", "Ricardo"],
     "surname": ["Gomila", "Santos", "Alberich"],
     "gender": ["m", "f", "m"]}

df = pd.DataFrame(d)
df

#Usamos .iterrows() para obtener el índice de cada fila junto al contenido de 
# cada una:
for i, j in df.iterrows():
  print("Índice de la fila: {},\n\nContenido de la fila:\n{}".format(i, j), end = "\n\n\n")

#Usamos .itertuples() para obtener una tupla con toda la información 
# de cada fila:#
for i in df.itertuples():
  print("Contenido de la fila:\n{}".format(i), end = "\n\n")

#Para iterar sobre las columnas de un dataframe,creamos una lista de las 
# columnas del dataframe y luego iterarmos sobre esa lista para obtener la información de esas columnas
#usamos el métood .iteritems()#
columns = list(df)
print(columns)

for c in columns:
  print("Columna {}:\n{}".format(c, df[c]), end = "\n\n")

#Usamos .iteritems() para obtener el nombre de cada columna junto al contenido 
# de cada una:#
for i, j in df.items():
  print("Nombre de la columna: {},\n\nContenido de la columna:\n{}".format(i, j), end = "\n\n\n")

#CARGA DE ARCHIVOS APARIR ARCHIVO CSV local# 
# direccion url pagina kaggle : https://www.kaggle.com/datasets?fileType=csv #
import pandas as pd
simpsons_df = pd.read_csv("CargaArchivosPython\ArchivosCSV\characterssimpsons.csv")
simpsons_df.head()
print(simpsons_df.head)

simpsons_df.tail()
print(simpsons_df.tail)

#DATAFRAMES APARIR URL#
letters_freq_df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/letter_frequency.csv")
letters_freq_df.columns = ["Letra", "Frecuencia", "Porcentaje"]
print(letters_freq_df)

#CRGA DE ARCHIVOS APARTIR DE GOOGLE COLAB#
#from google.colab import drive
#drive.mount('/content/drive')

#simpsons_df = pd.read_csv("/content/drive/MyDrive/python-basico/datasets/characters-simpsons.csv")
#simpsons_df.head()

#CARGA ARCHIVOS MEDIANTE UN JSON EN GOOGLE COLAB#
#import pandas as pd
#quiz_index = pd.read_json("/content/drive/MyDrive/python-basico/datasets/json_index_example.json",
#                          orient = "index")
#quiz_index.head()

#CARGAR ARCHIVO JSON FORMA LOCAL SU COMPUTADOR#
print("CARGAR ARCHIVO JSON FORMA LOCAL SU COMPUTADOR")
import pandas as pd
quiz_index = pd.read_json("CargaArchivosPython\ArchivosJSON\json_index_example.json",
                          orient = "index")
quiz_index.head()
print(quiz_index.head)
quiz_index = df.shape
print(df.shape) 

#El parámetro orient
#En el caso de archivos json, podría darse que no tuvieran la misma configuración
#  que nuestro ejemplo, json_index_example.json cuya orientación se corresponde con index.

#El parámetro orient del método .read_json() admite otras opciones como columns 
# o values.

#Veamos ambos casos con los ficheros json_columns_example.json y
# json_values_example.json, respectivamente.

print("Orientación con index")
# Orientación con index
import pandas as pd
quiz_index = pd.read_json("CargaArchivosPython\ArchivosJSON\json_index_example.json",
                          orient = "index")
quiz_index.head()
print(quiz_index)

print("Orientación con columns")
# Orientación con columns
quiz_columns = pd.read_json("CargaArchivosPython\ArchivosJSON\json_columns_example.json",
                    orient = "columns")
quiz_columns.head()
print(quiz_columns)

print("Orientación con Values")
# Orientación con values
quiz_values = pd.read_json("CargaArchivosPython\ArchivosJSON\json_values_example.json",
                           orient = "values")
quiz_values.head()
print(quiz_values)

#Descarga de un JSON desde una URL#
import pandas as pd
from_url = pd.read_json("https://api.exchangerate-api.com/v4/latest/USD")
from_url.head()
print(from_url.head())

#DATOS FALTANTES METODOS(ISNOTNULL - NOTNULL#

# Nos devuelve True allí donde hay un dato faltante
simpsons_df.isnull().head()
print(simpsons_df.isnull())

# Nos devuelve False allí donde hay un dato faltante
simpsons_df.notnull().head()
print(simpsons_df.notnull())

#Existen muchas técnicas para tratar con valores faltantes: se sustituyen por 
# la media, por la mediana, se elimina la observación, se interpolan... 
# nosotros no entraremos en detalle en ese aspecto. Simplemente veremos los 
# métodos de Python que podemos utilizar para tratar con valores faltantes:

#.fillna()
#.replace()
#.interpolate()
#.dropna()

#El método .fillna() sustituye los valores faltantes por el valor que 
#indiquemos por parámetro

# Necesitamos la librería numpy para crear un dataframe con valores NaN
print("Aqui creamos el DataFrame")
import numpy as np
data = {"Primer lanzamiento": [100, 86, np.nan, 75, 97],
        "Segundo lanzamiento": [80, np.nan, 63, 81, 88],
        "Tercer lanzamiento": [93, 89, 92, 97, np.nan]
        }

points_df = pd.DataFrame(data, index = ["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4", "Jugador 5"])
print(points_df)

# Sustituimos todos los NaN por 0 puntos
print("Aqui Sustituimos todos los NaN por 0 punto utilizamos metodo FILLNA ")
points_df.fillna(0)
print(points_df.fillna(0))

#Para sustituir valores faltantes con el método .replace() lo hacemos del 
#siguiente modo: primero pasamos por parámetro el valor que queremos sustituir ejemplo los NaN por nan se reemplaza o asi se indica 
#y luego, el valor por el cual queremos sustituirlo en eset caso es 100000000 como ejemplo.

print("Aqui Sustituimos utlizando metodo REPLACE ")
points_df = pd.DataFrame(data, index = ["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4", "Jugador 5"])
points_df.replace(np.nan, 1000000)
print(points_df.replace(np.nan,1000000))

#Si usamos el método .interpolate(), sustituiremos los valores NaN por valores 
#interpolados. Este método consta de muchos parámetros para elegir el 
#método (que por defecto es linear) por el cual llevar a cabo la interpolación se puede refereir a uno de lso casos a promediar
print("Aqui Sustituimos utilizando metodo INTERPOLATE ")
points_df = pd.DataFrame(data, index = ["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4", "Jugador 5"])
points_df.interpolate()
print(points_df.interpolate())

#ejemplo del metodo INTERPOLATE #
import pandas as pd
import numpy as np

# Crear un DataFrame con valores NaN
data = {'A': [1, np.nan, 3, np.nan, 5],
        'B': [np.nan, 2, np.nan, 4, 5]}
df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

# Interpolar los valores NaN utilizando el método 'linear'
df_interpolated = df.interpolate(method='linear')

print("\nDataFrame con valores interpolados:")
print(df_interpolated)

# El método .dropna() elimina las filas que contienen valores faltantes.
print("Aqui ELIMINAMOS. utilizamos metodo DROPNA")
points_df = pd.DataFrame(data, index = ["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4", "Jugador 5"])
points_df.dropna()
print(points_df.dropna())
print("")
print("")

#FILTRANDO DATAFRAMES#
#Mostramos las observaciones con porcentaje mayor a 5
print("FILTRANDO DATAFRAMES")
letters_freq_df[letters_freq_df["Porcentaje"] > 5]
print(letters_freq_df[letters_freq_df["Porcentaje"] > 5])

# Mostramos las observaciones con frecuencia menor o igual a la de la letra S
print("Mostramos las observaciones con frecuencia menor o igual a la de la letra S")
freq_S = letters_freq_df.loc[18, "Frecuencia"]
letters_freq_df[letters_freq_df["Frecuencia"] <= freq_S]
print(letters_freq_df[letters_freq_df["Frecuencia"] <= freq_S])

#El método .query() nos puede ser útil para este cometido, pero funciona 
#únicamente cuando los valores de la columna no contienen espacios en blanco.
# Mostramos aquellas observaciones cuyo porcentaje es mayor a 5
print("Metodo Query solo funciona sin espacios en blanco 'Porcentaje > 5'")
letters_freq_df.query('Porcentaje > 5')
print(letters_freq_df.query('Porcentaje > 5'))

# Mostramos aquellas observaciones cuyo porcentaje es mayor a 5 y menor o igual a 8
print("Porcentaje > 5 and Porcentaje <= 8")
letters_freq_df.query("Porcentaje > 5 and Porcentaje <= 8")
print(letters_freq_df.query("Porcentaje > 5 and Porcentaje <= 8"))
print("")

#SERIES EN PANDAS( SON UNA ESPECIA DE COLUMNAS DE UN DF#
#Serie. Una Serie de pandas es como una columna de un dataframe.
#Podemos construir Series de pandas a partir de una lista unidimensional
print("Mis series en PANDAS")
a = [1, 2, 3, 4, 5]
my_series = pd.Series(a)
print(my_series)

#para acceder a un valor especifico#
print("para acceder a un valor especifico")
print(my_series[3])

#Cuando creamos una Serie, podemos modificar sus etiquetas con el 
# parámetro index:#
print("Cuando creamos una Serie, podemos modificar sus etiquetas con el parámetro index")
my_series = pd.Series(a, index = ["a", "b", "c", "d", "e"])
print(my_series)

#Ahora, para acceder a una entrada en particular, lo haremos con las nuevas
#  etiquetas:
print("Ahora, para acceder a una entrada en particular, lo haremos con las nuevas etiquetas:")
print(my_series["c"])

#También podemos crear Series a partir de diccionarios. 
#n este caso, las claves se corresponderán con las etiquetas de las 
#series, y los valores del diccionario con los valores que toman las entradas de la Serie.
print("CRear series apartir de DICCIONARIOS")
videos = {"day1": 5, "day2": 9, "day3": 7, "day4": 6, "day5": 8}
my_series = pd.Series(videos)
print(my_series)

#Para convertir una Serie en un DataFrame en Pandas, puedes utilizar 
# el método to_frame(). Aquí tienes un ejemplo:#
import pandas as pd

# Crear una Serie de ejemplo
notas = pd.Series([5.7, 8.5, 9.1, 5.5, 8.2, 9.0],
                  index=["Juan", "Jenifer", "David", "Pablo", "Armando", "Magdalena"])
print("Convertir una serie a DataFrame")
# Convertir la Serie en un DataFrame
df = notas.to_frame(name="Notas")

print(df)

#Para convertir una Serie en una lista, puedes usar el método tolist():#
print("Convertir una serie a una lista")
notas_lista = notas.tolist()
print(notas_lista)
print("")
#MULTIINDICES EN PANDAS PARA ANALISIS DE DATOS EJEMPLO DATAFRAME#
print("#MULTIINDICES EN PANDAS PARA ANALISIS DE DATOS EJEMPLO DATAFRAME#")
import pandas as pd
df = pd.read_csv("CargaArchivosPython\WordsByCharacteres\WordsByCharacter-220320-150428.csv")
df.head()
print("metodo HEAD me muestra la cabecera los PRIMEROS 5 del DF")
print(df.head())
print("metodo TAIL me muestra los ULTIMOS 5 del DF")
print(df.tail())
#MUESTRA NOMBRES DE LAS COLUMNAS DEL INDEX #
print("MUESTRA NOMBRES DE LAS COLUMNAS DEL INDEX")
print(df.index.names)
#DEVUELVE UN ARRAY QUE REPRESENTA LOS VALORES DEL INDice del multiindex#
print("#DEVUELVE UN ARRAY QUE REPRESENTA LOS VALORES DEL INDice del multiindex#")
print(df.index.values)
df.index.values

#En esta línea de código, estás creando un MultiIndex en un DataFrame de Pandas. 
# Permíteme explicarte paso a paso:
#Primero, tienes un DataFrame llamado df.
#Luego, utilizas el método .set_index(['Film', 'Chapter', 'Race', 'Character']) 
# para establecer un índice compuesto por las columnas 'Film', 'Chapter', 'Race' 
# y 'Character'.
#Después, aplicas .sort_index() para ordenar el DataFrame según los valores 
# de este nuevo MultiIndex.

multiindex = df.set_index(['Film', 'Chapter', 'Race', 'Character']).sort_index()
#aqui imprime los primeros 5 cabecera#
print(multiindex.head())
#aqui se imprime los ultimos 5 la cola#
print(multiindex.tail())
#aqui se obtiene una lista con los nombres 
# de los niveles en ese MultiIndex#
print(multiindex.index.names)
# DEVUELVE UN ARRAY QUE REPRESENTA LOS VALORES DEL INDice del multiindex #
multiindex.index.values
print(multiindex.index.values)

# Esta línea sirve para reiniciar los índices múltiples de Búsqueda
#multiindex.reset_index()

#La línea de código multiindex.loc[('The Fellowship Of The Ring',
#  '01: Prologue'), :] selecciona todas las filas en el DataFrame con un 
# índice jerárquico (MultiIndex) donde el nivel 'Film' coincide con 
# 'The Fellowship Of The Ring' y el nivel 'Chapter' coincide con '01:
#  Prologue'1. En otras palabras, estás filtrando las filas relacionadas 
# con el primer capítulo de “La Comunidad del Anillo”. Si necesitas más 
# ayuda o tienes más preguntas, no dudes en preguntar#
multiindex.loc[('The Fellowship Of The Ring', '01: Prologue'), :]
print(multiindex.loc[('The Fellowship Of The Ring', '01: Prologue'), :])

#Tienes un DataFrame llamado multiindex con un MultiIndex (índice jerárquico) 
# creado previamente1.
#La parte ('The Fellowship Of The Ring', slice(None), 'Elf') se refiere a la 
# selección de filas en el DataFrame. Aquí está desglosado:
#'The Fellowship Of The Ring': Selecciona todas las filas donde el nivel 
# 'Film' coincide con “The Fellowship Of The Ring”.
#slice(None): Esto representa todas las posibles opciones para el nivel 
# 'Chapter'. En otras palabras, selecciona todas las filas en ese nivel.
#'Elf': Selecciona todas las filas donde el nivel 'Race' coincide con “Elf”.
#Finalmente, .head(3) muestra las primeras tres filas resultantes de esta 
# selección. #En resumen, estás filtrando las filas relacionadas con la película 
# “The Fellowship Of The Ring” y el grupo de personajes “Elf”. 
# Si necesitas más ayuda o tienes más preguntas, no dudes en preguntar.#

multiindex.loc[('The Fellowship Of The Ring', slice(None), 'Elf'), : ].head(3)
print(multiindex.loc[('The Fellowship Of The Ring', slice(None), 'Elf'), : ].head(3))

#La línea de código multiindex.loc[('The Two Towers', slice(None), slice(None),
#  ['Gandalf', 'Saruman']), :] selecciona todas las filas en el DataFrame con un 
# índice jerárquico (MultiIndex) donde:
#El nivel 'Film' coincide con 'The Two Towers'.
#Los niveles restantes no tienen restricciones específicas 
# (se utiliza slice(None) para indicar que no se filtran).
#Además, se filtran las filas donde el nivel 'Character' 
# coincide con 'Gandalf' o 'Saruman'#
multiindex.loc[('The Two Towers', slice(None), slice(None), ['Gandalf', 'Saruman']), :]
print(multiindex.loc[('The Two Towers', slice(None), slice(None), ['Gandalf', 'Saruman']), :])

# Calcular la suma de las palabras habladas por Isildur
total_palabras_isildur = multiindex.xs('Isildur', level='Character').sum()
print(f"Isildur habla un total de {total_palabras_isildur} palabras en todas las películas.")
# Otra forma de validar cauntas palabras habla Isuldur#
print(multiindex.xs('Isildur', level = 'Character').sum())

#Tienes un DataFrame llamado df.
#Utilizas .pivot_table() para crear una tabla dinámica con las siguientes 
# configuraciones: #index=['Race', 'Character']: Estableces los niveles del 
# índice en función de las columnas 'Race' y 'Character'.
#columns='Film': Las columnas de la tabla dinámica se basarán en los 
# valores únicos de la columna 'Film'.
#aggfunc='sum': Agregas los valores sumando los datos para cada combinación 
# de índice y columna.
#margins=True: Agregas filas y columnas adicionales para mostrar totales 
# generales.
#margins_name='All The Movies': Nombras la fila/columna de totales 
# generales como “All The Movies”.
#fill_value=0: Rellenas los valores faltantes con ceros.
#.sort_index(): Ordenas la tabla dinámica según los niveles del índice.#
pivoted = df.pivot_table(index = ['Race', 'Character'],
                         columns = 'Film',
                         aggfunc = 'sum',
                         margins = True,
                         margins_name = 'All The Movies',
                         fill_value = 0).sort_index()

#Ordena el DataFrame pivoted según los valores de la columna 'Words' 
# correspondientes a todas las películas (columna 'All The Movies') 
# en orden descendente.
#Reorganiza las columnas del DataFrame pivoted según el orden especificado 
# en la lista order#
print("")
print("Ordena el DataFrame pivoted segun los valores de las clumnas words")
order = [('Words', 'The Fellowship Of The Ring'),
         ('Words', 'The Two Towers'),
         ('Words', 'The Return Of The King'),
         ('Words', 'All The Movies')]
print("")
print("Ordena el DATAFRAME por valor de mayor a menor ascending")
pivoted = pivoted.sort_values(by = ('Words', 'All The Movies'), ascending = False)

pivoted = pivoted.reindex(order, axis = 1)

print(pivoted)

print(pivoted.loc['Hobbit'])

#Este DataFrame muestra las palabras habladas por cada personaje en las películas
#  “The Fellowship Of The Ring”, “The Two Towers” y “The Return Of The King”, 
# así como el total de todas las películas#