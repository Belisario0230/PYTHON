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

#DATAFRAMES APARIR ARCHIVO CSV local# 
# direccion url pagina kaggle : https://www.kaggle.com/datasets?fileType=csv #
import pandas as pd
simpsons_df = pd.read_csv("DataFrames\characterssimpsons.csv")
simpsons_df.head()
print(simpsons_df.head)

simpsons_df.tail()
print(simpsons_df.tail)

#DATAFRAMES APARIR URL#
letters_freq_df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/letter_frequency.csv")
letters_freq_df.columns = ["Letra", "Frecuencia", "Porcentaje"]
print(letters_freq_df)

