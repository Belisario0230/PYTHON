import matplotlib.pyplot as plt
import numpy as np

# Grafico No 1 Nube de Puntos #
height = [174.3, 153.5, 162.1, 157.9, 174.8, 169.2, 172.0, 160.4, 152.8, 163.3] 
weight = [ 65.7,  59.2,  57.3,  61.5,  77.3,  90.7,  85.4,  63.1,  73.2, 105.5]

plt.title("Alturas vs. pesos")
plt.xlabel("Alturas (cm)")
plt.ylabel("Pesos (kg)")
plt.scatter(x = height, y = weight, 
            c = "black", edgecolors = "red", alpha = 1,
            marker = "X", s = 200, linewidths = 2)
plt.show()

# Observación. Grafico No 2 Podríamos mostrar 2 conjuntos diferentes de datos 
# en un gráfico de nube de puntos: #
height_boys = [174.3, 153.5, 162.1, 157.9, 174.8, 169.2, 172.0, 160.4, 152.8, 163.3] 
weight_boys = [65.7, 59.2, 57.3, 61.5, 77.3, 90.7, 85.4, 63.1, 73.2, 105.5]

height_girls = [154.2, 156.1, 160.3, 157.9, 162.6, 153.9, 170.1, 165.2, 157.6, 163.5] 
weight_girls = [55.3, 54.2, 47.3, 62.4, 77.5, 60.3, 52.4, 58.1, 50.2, 80.1]

plt.title("Alturas vs. pesos")
plt.xlabel("Alturas (cm)")
plt.ylabel("Pesos (kg)")

plt.scatter(x = height_boys, y = weight_boys, c = "red", marker = "^", s = 100)
plt.scatter(x = height_girls, y = weight_girls, c = "blue", marker = "v", s = 100)

plt.show()

#Observación. Grafico No 3 Podemos dibujar cada punto de un tamaño, pasando
#  una lista al parámetro s:#
x = [1, 2, 3, 4, 5, 6, 7]
sizes = [100, 150, 200, 250, 300, 350, 400]

plt.scatter(x = x, y = x, s = sizes, c = "m", alpha = 0.5)
plt.title("Diferentes tamaños")
plt.show()

#Observación. Grafico No 4 Podemos pintar un punto de cada color, pasando como
#  parámetro c una lista de colores:#
x = [1, 2, 3, 4, 5, 6, 7]
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
sizes = [100, 150, 200, 250, 300, 350, 400]

plt.scatter(x = x, y = x, c = colors, s = sizes)
plt.title("Arcoiris")
plt.show()

#Grafico No 5 También podríamos haber usado un mapa de color para colorear los puntos.

#Para ello, en vez de una lista de colores, necesitaremos indicar en el parámetro 
#cmap el mapa de color a usar y, en el parámetro c indicar una lista o array 
#1D de valores entre 0 y 100 para indicar así el color de cada punto para el 
#colormap determinado.#

colors = np.array([0, 10, 20, 30, 40, 50, 60])

plt.scatter(x = x, y = x, c = colors, cmap = "plasma", s = 200)
plt.title("Mapa de color plasma")
plt.show()

#Observación. Grafico No 6 Podemos adjuntar al gráfico el mapa de color usado 
# con el método .colorbar()
colors = np.array([0, 10, 20, 30, 40, 50, 60])

plt.scatter(x = x, y = x, c = colors, cmap = "plasma", s = 200)
plt.title("Mapa de color plasma")
plt.colorbar()
plt.show()

#Ejercicio No 6,1 Grfico #
colors = np.array([0, 10, 20, 30, 40, 50, 60])

plt.scatter(x = x, y = x, c = colors, cmap = "plasma_r", s = 200)
plt.title("Mapa de color plasma")
plt.colorbar()
plt.show()

#Para hacer un gráfico 7 line plot, usamos el método .plot() del módulo plt.#
plt.title("Alturas vs. pesos")
plt.xlabel("Alturas (cm)")
plt.ylabel("Pesos (kg)")
plt.plot(sorted(height), weight, 
            c = "blue", ls = "--", lw = 2,
            marker = "*", ms = 20, mfc = "m")
plt.show()

#Grafico No 8 Podríamos obtener el mismo resultado usando el parámetro fmt#
plt.title("Alturas vs. pesos")
plt.xlabel("Alturas (cm)")
plt.ylabel("Pesos (kg)")
plt.plot(sorted(height), weight, "*--b", lw = 2,
         markersize = 20, mfc = "m")
plt.show()

#**Observación.** Si no indicamos parámetro `x`, se consideran como primeras 
# coordenadas los números enteros 0, 1, 2, ..., $n-1$, siendo $n$ el número 
# total de observaciones:#

rainy_days = [20, 15, 19, 25, 13, 8, 3, 5, 10, 16, 20, 18]

plt.title("Días de lluvia por mes")
# (0 = Enero, 1 = Febrero, ..., 11 = Diciembre)
plt.xlabel("Mes")
plt.ylabel("Total días de lluvia")
plt.plot(rainy_days, c = "cyan", marker = "o")
plt.show()

#**Observación.** En un mismo plot podemos dibujar más de una línea:#
l1 = np.array([3, 5, 1, 9])
l2 = np.array([8, 2, 6, 4])

plt.plot(l1, c = "blue")
plt.plot(l2, c = "magenta")
plt.title("2 líneas en 1 plot")
plt.show()

#### Bar Plot

#Para hacer un gráfico de barras, usamos el método `.bar()` del módulo `plt`.

#Algunos de los parámetros de este método son:

#* `x`: float, array o lista que indica las categorías o coordenadas de las barras
#* `height`: float, array o lista que indica las alturas de las barras
#* `width`: para cambiar la anchura de las barras
#* `linewidth`: para cambiar el tamaño del borde de las barras
#* `bottom`: para cambiar el valor vertical mínimo de las barras
#* `align`: posición de la marca del eje horizontal con respecto a la base de las barras. Por defecto vale "center"
#* `color` para cambiar los colores de las barras. Si pasamos una lista, podemos asignar un color diferente a cada barra
#* `edgecolor`: para cambiar el color del borde de las barras#

#### Bar Plot

#Para hacer un gráfico de barras, usamos el método `.bar()` del módulo `plt`.
grades = ["Suspenso", "Aprobado", "Notable", "Excelente"]
count = [35, 55, 23, 7]

plt.bar(grades, count, color = ["#ff7f7d", "#ffc07d", "#817dff", "#7dff86"])
plt.xlabel("Notas")
plt.ylabel("Número alumnos")
plt.title("Notas de los alumnos de una clase")
plt.show()


#Aqui se modifica el width el anterior por defecto tenia 1 este tiene
#0.5 mas angosto#

plt.bar(grades, count, color = ["#ff7f7d", "#ffc07d", "#817dff", "#7dff86"], width = 0.5)
plt.xlabel("Notas")
plt.ylabel("Número alumnos")
plt.title("Notas de los alumnos de una clase")
plt.show()

#Si quisiésemos las barras en horizontal, habrá que usar el método `.barh()`.#
plt.barh(grades, count, color = ["#ff7f7d", "#ffc07d", "#817dff", "#7dff86"])
plt.xlabel("Notas")
plt.ylabel("Número alumnos")
plt.title("Notas de los alumnos de una clase")
plt.show()

#**¡Cuidado!** Si quisiéramos modificar la anchura de las barras horizontales, 
# habrá que modificar el parámetro `height`en vez del parámetro `width`#
plt.barh(grades, count, color = ["#ff7f7d", "#ffc07d", "#817dff", "#7dff86"], height = 0.5)
plt.xlabel("Notas")
plt.ylabel("Número alumnos")
plt.title("Notas de los alumnos de una clase")
plt.show()