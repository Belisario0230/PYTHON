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