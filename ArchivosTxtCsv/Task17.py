#Ejercicio 1
#Pídele al usuario el nombre, el apellido, la edad y su color favorito.
#Guarda la información en un diccionario de claves name, surname, age y color.
#Crea y escribe un txt con 4 frases, una en cada línea. La primera debe 
# indicar el nombre del usuario; la segunda, el apellido; la tercera, la edad; 
# y la última, el color favorito del usuario.
"""
name = input("Introduce tu nombre: ")
surname = input("Introduce tu apellido: ")
age = int(input("Introduce tu edad: "))
color = input("Introduce tu color favorito: ")

info = {
    "name": name,
    "surname": surname,
    "age": age,
    "color": color
}

with open("D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\EscribirFicheroTask17.txt", mode="w") as f:
    f.write(f"El usuario se llama {info['name']} {info['surname']}\n")
    f.write(f"La edad del usuario es {info['age']}\n")
    f.write(f"El color favorito del usuario es el {info['color'].lower()}")

#Ejercicio 2
#Lee el archivo txt creado en el ejercicio anterior para ver que se ha
#creado correctamente.
with open("D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\EscribirFicheroTask17.txt", mode="r") as f:
    for line in f:
        print(line.strip())  # Elimina los saltos de línea al final de cada línea


#Ejercicio 3
#Crea un archivo txt vacío y llámalo ej3.txt.
f = open("D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\EscribirFicheroTask17EjercicioVacio3.txt", mode="x")
f.close()


#Ejercicio 4
#Elimina el archivo creado en el ejercicio 3.
import os
os.remove("D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\EscribirFicheroTask17EjercicioVacio3.txt")

#Ejercicio 5
#Crea un archivo txt vacío y llámalo ej5.txt. Sobreescribelo con las 
# siguientes líneas:
#"x,y,Color,Shape \n" "1,1,#6fb7ff,< \n" "-1,1,#ffa66f,v \n" "-1,-1,#ffee6f,> 
# \n" "1,-1,#db6fff,^ \n"

#Creamos archivo TXT Vacio#
f = open("D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\EscribirFicheroTask17EjercicioVacio3.txt", mode="x")
f.close()


#Modificamos archivo TXt que se encontraba vacio#
f = open("D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\EscribirFicheroTask17EjercicioVacio3.txt", mode="w")
f.write("x,y,Color,Shape\n")
f.write("1,1,#6fb7ff,<\n")
f.write("-1,1,#ffa66f,v\n")
f.write("-1,-1,#ffee6f,>\n")
f.write("1,-1,#db6fff,^\n")
f.close()
"""
#Ejercicio 6
#Lee el archivo txt del ejercicio 5 como si fuera un archivo csv. Guarda
#  las filas del objeto reader en una lista llamada df. Al final tendrás
#  una lista con 5 listas de tamaño 4.

import csv

data = []
with open("D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\EscribirFicheroTask17EjercicioVacio3.txt", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
"""
#Ejercicio 7
#Utiliza el método .read_csv() de pandas para leer el contenido del txt 
# del ejercicio 5 y guardarlo en un dataframe llamado df.
import pandas as pd
df=pd.read_csv("D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\EscribirFicheroTask17EjercicioVacio3.txt")

#Ejercicio 8
#Utiliza el dataframe df para representar los puntos cuyas coordenadas x 
# están guardadas en la columna x y cuyas coordenadas y están guardadas en 
# la columna y. Para ello utiliza el método .scatterplot() de seaborn.
#Pon de título “Puntos”. No muestres etiqueta en el eje horizontal ni en el 
# eje vertical. Haz que el tamaño de la figure sea de 5 x 5 y que el tamaño 
# de los puntos sea de 500.
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))
sns.scatterplot(data=df, x="x", y="y", s=500)
plt.title("Puntos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()


#Ejercicio 9
#Modifica el gráfico anterior para que el color venga dado por la 
# variable Color de df y la forma de los puntos, por la variable Shape.
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))
sns.scatterplot(data=df, x="x", y="y", s=500, hue="Color", palette=df["Color"].tolist(), style="Color", markers=df["Shape"].tolist())
plt.title("Puntos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()

"""
#Ejercicio 10
#Guarda en un csv la información de la lista data del ejercicio 6. 
# Llama al archivo csv ej10.csv
import csv
with open("D:\Documents\CURSOS1\PYTHON\ArchivosTxtCsv\Ejercicio10.csv", "w") as f:
    writer=csv.writer(f)
    for row in data:
        writer.writerow(row)
