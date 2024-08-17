#Ejercicio 1
#Dibuja 100 puntos aleatorios (entre 0 y 100 para ambas coordenadas) con colores 
# y tamaños aleatorios y una transparencia de 0.5.
#Tendrás que crear 4 arrays aleatorios de 100 posiciones: uno para las coordenadas
#  x, otro para y, otro para el color de cada punto y un último para el tamaño 
# de cada punto. Para que los puntos no se vean muy pequeños, multiplica el 
# array de tamaños por 10.
#Configura el tamaño de la figure a 10 x 10. Para ello, investiga el método .
# figure() de plt.
#Por último, selecciona los colores combinando el array aleatorio y el mapa de 
# color llamado hsv. Recuerda mostrar la colorbar.
import numpy as np
import matplotlib.pyplot as plt

# Crear 4 arrays aleatorios de 100 posiciones
x_coords = np.random.randint(0, 101, 100)
y_coords = np.random.randint(0, 101, 100)
colors = np.random.rand(100, 3)  # RGB values
sizes = np.random.randint(1, 11, 100) * 10

# Configurar el tamaño de la figura
plt.figure(figsize=(10, 10))

# Crear el scatter plot con los puntos aleatorios
plt.scatter(x_coords, y_coords, c=colors, s=sizes, alpha=0.5, cmap='hsv')

# Mostrar la colorbar
plt.colorbar()

# Etiquetas y título
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('100 Puntos Aleatorios')

# Mostrar el gráfico
plt.show()

#Ejercicio 2
#En el plano complejo, representa los números complejos 1 + i, 2i, −1 − i, −3,
#  −2 − i, −2i y 1 − i.
#Recuerda que el plano complejo es como un plano cartesiano, salvo que 
# el eje horizontal se denomina eje real y, el eje vertical, eje imaginario.
#Representa los puntos de color rojo y tamaño 120 y los ejes vertical 
# y horizontal de color negro y transparencia 0.5. Para representar los 
# puntos, puedes considerar una lista que contenga las partes reales y 
# otra lista que contenga las partes imaginarias de los números complejos.
#  Para representar los ejes, debes dibujar una recta horizontal y = 0 y 
# otra vertical x = 0. Investiga para ello el método .linspace() de numpy. 
# Para que las dimensiones del argumento x e y sean las mismas, puede que 
# tengas que usar el método .zeros de numpy para obtener un array de ceros 
# del tamaño deseado.
#Pon como título “Plano complejo” e investiga los métodos .xlim e .ylim de
#  plt para establecer el rango de x en el intervalo [-3.2, 3.2] y el rango 
# de y en el intervalo [-2.2, 2.2].
import numpy as np
import matplotlib.pyplot as plt

# Números complejos
complejos = [1 + 1j, 2j, -1 - 1j, -3, -2 - 1j, -2j, 1 - 1j]

# Partes reales e imaginarias
parte_real = np.real(complejos)
parte_imaginaria = np.imag(complejos)

# Crear la figura
plt.figure(figsize=(10, 10))

# Representar los puntos
plt.scatter(parte_real, parte_imaginaria, color='red', s=120, label='Números complejos')

# Representar los ejes
plt.axhline(y=0, color='black', alpha=0.5)
plt.axvline(x=0, color='black', alpha=0.5)

# Configurar límites de los ejes
plt.xlim(-3.2, 3.2)
plt.ylim(-2.2, 2.2)

# Etiquetas y título
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.title('Plano Complejo')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()

#Ejercicio 3
#Crea una función que dado un color en forma RGB lo transforme en su 
# forma hexadecimal.
def rgb_to_hex(rgb):
    """
    Convierte un color en formato RGB a su representación hexadecimal.

    Args:
        rgb (tuple): Tupla con los valores de las componentes roja, verde y azul (0-255).

    Returns:
        str: Representación hexadecimal del color.
    """
    r, g, b = rgb
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color

# Ejemplo de uso
color_rgb = (255, 128, 0)  # Ejemplo: naranja
color_hex = rgb_to_hex(color_rgb)
print("Color RGB:", color_rgb)
print("Color hexadecimal:", color_hex)


#Ejercicio 4
#Dibuja la función sin(x) x de color #f06741, la función 2 
# sin(x) x de color #a4f041 y la función − sin(x) x de color #8d41f0 
# donde x ∈ [−5π, 5π] en el mismo plot.
#Crea el array x de tamaño 100 con el método .linspace() de numpy.
#Haz que el tamaño de la figure sea 8 x 6.
import numpy as np
import matplotlib.pyplot as plt

# Crear el array x con 100 puntos en el intervalo [-5π, 5π]
x = np.linspace(-5 * np.pi, 5 * np.pi, 100)

# Evaluar las funciones en los puntos x
f1 = np.sin(x)
f2 = 2 * np.sin(x)
f3 = -np.sin(x)

# Configurar el tamaño de la figura
plt.figure(figsize=(8, 6))

# Graficar las funciones con los colores especificados
plt.plot(x, f1, label='$f_1(x) = \sin(x)$', color='#f06741')
plt.plot(x, f2, label='$f_2(x) = 2\sin(x)$', color='#a4f041')
plt.plot(x, f3, label='$f_3(x) = -\sin(x)$', color='#8d41f0')

# Etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funciones Trigonométricas')
plt.legend()

# Mostrar el gráfico
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Crear el array x con 100 puntos en el intervalo [-5π, 5π]
x = np.linspace(-5 * np.pi, 5 * np.pi, 100)

# Evaluar las funciones en los puntos x
f1 = np.sin(x)
f2 = 2 * np.sin(x)
f3 = -np.sin(x)

# Configurar el tamaño de la figura global
plt.figure(figsize=(10, 5))

# Subplot 1: f1(x) = sin(x)
plt.subplot(131)
plt.plot(x, f1, label='$f_1(x) = \sin(x)$', color='#f06741')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función 1')
plt.legend()

# Subplot 2: f2(x) = 2sin(x)
plt.subplot(132)
plt.plot(x, f2, label='$f_2(x) = 2\sin(x)$', color='#a4f041')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función 2')
plt.legend()

# Subplot 3: f3(x) = -sin(x)
plt.subplot(133)
plt.plot(x, f3, label='$f_3(x) = -\sin(x)$', color='#8d41f0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función 3')
plt.legend()

# Ajustar los subplots
plt.tight_layout()

# Mostrar la figura
plt.show()

#Ejercicio 6
#Dibuja un diagrama de sectores con los siguientes datos y los siguientes 
# . Añádele un título, etiquetas, sombra, una separación de 0.2 al sector 
#  pequeño, haz que empiece en el ángulo 45 y muestra los porcentajes con un 
# solo decimal.
#options = ["Suspenso", "Aprobado", "Notable", "Excelente"] count = [20, 10, 45, 
# 25] colors = ["#ff2667", "#ff7226", "#26a8ff", "#67ff26"]

import matplotlib.pyplot as plt

# Datos
options = ["Suspenso", "Aprobado", "Notable", "Excelente"]
count = [20, 10, 45, 25]
colors = ["#ff2667", "#ff7226", "#26a8ff", "#67ff26"]

# Configurar el tamaño de la figura
plt.figure(figsize=(8, 6))

# Crear el gráfico de sectores con espacio entre las etiquetas
plt.pie(count, labels=options, colors=colors, shadow=True, startangle=45, autopct='%.1f%%', explode=[0.2, 0, 0, 0])

# Título
plt.title('Distribución de Calificaciones', pad=20)  # Añadimos espacio al título

# Mostrar el gráfico
plt.show()

#Ejercicio 7
#Dibuja el siguiente grafo con los nodos de color #ad80fa, las aristas de color
#  #b1ddf5, el nombre de los nodos de color blanco y en negrita.
#import networkx as nx G = nx.Graph() G.add_nodes_from("abcde") 
# G.add_weighted_edges_from([("a", "b", 1), ("a", "c", 2), 
# ("a", "d", 2), ("a", "e", 5), ("b", "e", 4), ("c", "d", 3), ("d", "e", 1)])
import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo
G = nx.Graph()
G.add_nodes_from("abcde")
G.add_weighted_edges_from([("a", "b", 1), ("a", "c", 2), 
                           ("a", "d", 2), ("a", "e", 5), 
                           ("b", "e", 4), ("c", "d", 3), 
                           ("d", "e", 1)])

# Colores y estilos
node_color = '#ad80fa'
edge_color = '#b1ddf5'
font_color = 'white'
font_weight = 'bold'

# Dibujar el grafo
pos = nx.spring_layout(G)  # disposición para los nodos
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color=node_color, 
        edge_color=edge_color, font_color=font_color, font_weight=font_weight,
        node_size=700, font_size=15)
plt.show()

#Ejercicio 8
#Considera el grafo del ejercicio anterior. El tamaño de los nodos debe ser 350
#  por el grado del nodo. El tamaño de la figure global debe ser de 8 x 6.
import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo
G = nx.Graph()
G.add_nodes_from("abcde")
G.add_weighted_edges_from([("a", "b", 1), ("a", "c", 2), 
                           ("a", "d", 2), ("a", "e", 5), 
                           ("b", "e", 4), ("c", "d", 3), 
                           ("d", "e", 1)])

# Calcular el tamaño de los nodos en función del grado
node_sizes = [350 * G.degree(n) for n in G.nodes()]

# Colores y estilos
node_color = '#ad80fa'
edge_color = '#b1ddf5'
font_color = 'white'
font_weight = 'bold'

# Dibujar el grafo
pos = nx.spring_layout(G)  # disposición para los nodos
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color=node_color, 
        edge_color=edge_color, font_color=font_color, font_weight=font_weight,
        node_size=node_sizes, font_size=15)
plt.show()

#Ejercicio 9
#Considera el grafo del ejercicio anterior. El grosor de las aristas 
# debe ir acorde al peso de cada arista.
import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo
G = nx.Graph()
G.add_nodes_from("abcde")
G.add_weighted_edges_from([("a", "b", 1), ("a", "c", 2), 
                           ("a", "d", 2), ("a", "e", 5), 
                           ("b", "e", 4), ("c", "d", 3), 
                           ("d", "e", 1)])

# Calcular el tamaño de los nodos en función del grado
node_sizes = [350 * G.degree(n) for n in G.nodes()]

# Calcular el grosor de las aristas en función del peso
edge_widths = [G[u][v]['weight'] for u, v in G.edges()]

# Colores y estilos
node_color = '#ad80fa'
edge_color = '#b1ddf5'
font_color = 'white'
font_weight = 'bold'

# Dibujar el grafo
pos = nx.spring_layout(G)  # disposición para los nodos
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color=node_color, 
        edge_color=edge_color, font_color=font_color, font_weight=font_weight,
        node_size=node_sizes, width=edge_widths, font_size=15)
plt.show()

#Ejercicio 10
#Investiga el método .text() de plt para añadir texto a los plots.
#Añade las siguientes 3 palabras “LA”, “AVENTURA”, “SIGUE”.
#La palabra “LA” debe estar en la posición (0.2, 0.8), con tamaño 50 y 
# rotación 25, con alineación vertical y horizontal en el centro, y en 
# una caja de estilo redondo, con color de borde y relleno #242fff y 
# transparencia 0.7.
#La palabra “AVENTURA” debe estar en la posición (0.5, 0.55), con 
# tamaño 50 y rotación -15, con alineación vertical y horizontal en 
# el centro, y en una caja de estilo redondo, con color de borde y 
# relleno #8a24ff y transparencia 0.7.
#La palabra “SIGUE” debe estar en la posición (0.8, 0.3), con tamaño 
# 50 y rotación 10, con alineación vertical y horizontal en el centro,
#  y en una caja de estilo redondo, con color de borde y relleno #24fff4 
# y transparencia 0.7.
#El tamaño de la figure global debe ser 10 x 8.
import matplotlib.pyplot as plt

# Crear la figura
plt.figure(figsize=(10, 8))

# Añadir la palabra "LA"
plt.text(0.2, 0.8, "LA", fontsize=50, rotation=25,
         verticalalignment='center', horizontalalignment='center',
         bbox=dict(facecolor='#242fff', alpha=0.7, boxstyle='round', edgecolor='#242fff'))

# Añadir la palabra "AVENTURA"
plt.text(0.5, 0.55, "AVENTURA", fontsize=50, rotation=-15,
         verticalalignment='center', horizontalalignment='center',
         bbox=dict(facecolor='#8a24ff', alpha=0.7, boxstyle='round', edgecolor='#8a24ff'))

# Añadir la palabra "SIGUE"
plt.text(0.8, 0.3, "SIGUE", fontsize=50, rotation=10,
         verticalalignment='center', horizontalalignment='center',
         bbox=dict(facecolor='#24fff4', alpha=0.7, boxstyle='round', edgecolor='#24fff4'))

# Mostrar la figura
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axis('off')  # Ocultar los ejes
plt.show()
