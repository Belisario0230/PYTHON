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

#FILAS#
#Dado un dataframe, podemos seleccionar una fila en particular de diversas formas:

#Con el método .loc[] (por nombre o etiqueta)
#Con el método .iloc[] (por posición)

