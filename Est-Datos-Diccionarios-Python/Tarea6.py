# Ejercicio 1
# Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas 
# claves sean desde el número 1 hasta el número indicado. Los valores de cada clave serán las propias 
# claves elevadas al cubo.#

numero_positivo = int(input("Dijita un numero positivo: "))
diccionario = {}
for i in range(1, numero_positivo + 1):
    diccionario[i] = i ** 3
    print(diccionario)

#Ejercicio 2
# Escribe un programa que pregunte al usuario su nombre, edad y teléfono y lo guarde en un diccionario. 
# Después, debe mostrar por pantalla el mensaje ‘{nombre} tiene {edad} años y su número de 
# teléfono es {teléfono}.

programa = {}

programa ["nombre"] = str(input("Dijita tu nombre: "))
programa ["edad"] = int(input("Dijita tu edad: "))
programa ["telefono"] = int(input("Dijita tu numero de telefono: "))

print("El {} tiene {} aaños y su numero de telefono es {}".format(programa["nombre"], programa["edad"], programa["telefono"]))

# Ejercicio 3
# Escribe un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar
# el artículo y su precio por unidad. El artículo será la clave y el valor el precio, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra 
# y el coste total, con el siguiente formato : 
#                Artículo 1 Precio 
#                Artículo 2 Precio 
#                Artículo 3 Precio 
#                    . . . . . . 
#                Total Precio Total #

lista_Compras = []
articulo = input("Indique un artículo: ")

while articulo != "":
    precio = float(input("Indique el precio: "))
    lista_Compras.append((articulo, precio))
    articulo = input("Indica el artículo: ")

print("\nLista de compras:")
print("|" + " " * 7 + "Artículo" + " " * 7 + "|   Precio   |")
print("-" * 50)

total = 0
for articulo, valor in lista_Compras:
    total += valor
    print(f"| {articulo:<20} |   {valor:.2f}   |")

print("-" * 50)
print(f"| {'Total':<20} |   {total:.2f}   |")

#Ejercicio 4
# Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
# cantidad números positivos y negativos introducidos.#

numero = int(input("Introduce un numero entero por favor: "))
numeros_positivos = 0
total = 0

while numero != 0:
    if numero > 0:
        numeros_positivos += 1
    total += 1

    numero = int(input("Introduce un numero entero: "))
    diccionario = {"positivos": numeros_positivos, "negativos": total - numeros_positivos}
    print(diccionario)

#Ejercicio 5
# Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
# cantidad números pares e impares introducidos.#

numeros_pares = 0
numeros_ingresados = 0

while True:
    numero_ingresar = int(input("Introduce un número entero (0 para terminar): "))
    if numero_ingresar == 0:
        break
    elif numero_ingresar % 2 == 0:
        numeros_pares += 1
    numeros_ingresados += 1

nums = {"numeros pares": numeros_pares, "numeros impares": numeros_ingresados - numeros_pares}
print(nums)

# Ejercicio 6
# Crea un programa que permita al usuario introducir los nombres de los alumnos de una clase y las notas que
# han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario
# cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.#
#El programa va a pedir el nombre de un estudiante e irá pidiendo sus notas (del 1 al 10) hasta que introduzcamos
#un 0. Al final, cuando el nombre que introduzcamos sea un string vacío, el programa nos mostrará la
#lista de alumnos y la nota media obtenida por cada uno de ellos.
#PISTA: Vas a necesitar la función sum().

students = {}  # Creamos un diccionario vacío para almacenar la información de los estudiantes
name = input("Nombre del estudiante: ")  # Solicitamos el nombre del estudiante

while name != "":  # Continuamos hasta que se ingrese un nombre vacío
    students[name] = []  # Inicializamos una lista vacía para las notas del estudiante
    grade = int(input(f"Introduce las notas (de 1 a 10) de {name}, una a una: "))  # Solicitamos las notas

    while grade != 0:  # Continuamos hasta que se ingrese una nota de 0
        students[name].append(grade)  # Agregamos la nota a la lista del estudiante
        grade = int(input())  # Solicitamos la siguiente nota

    name = input("Nombre del estudiante: ")  # Solicitamos el nombre del siguiente estudiante

# Calculamos y mostramos la nota media para cada estudiante
print("\nResultados:")
for student in students:
    nota_media = sum(students[student]) / len(students[student])
    print(f"{student}: {nota_media:.2f}")

# Ejercicio 7
# Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
# sean desde el número 1 hasta el número indicado. Los valores de cada clave serán tantos símbolos "*" como
# indique la clave. #

numero = int(input("Dijita un numero entero positivo: "))
diccionario1 = {}
for i in range(1, numero + 1):
    diccionario1[i] = "+" * i
print(diccionario1)

# Ejercicio 8
# Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
# de valor la longitud de dicha palabra.#

numero_palabras = int(input("Cuantas palabras vas a dijitar: "))
palabras = {}

for _ in range(numero_palabras):
    palabra = input("palabra: ")
    palabras[palabra] = len(palabra)
print(palabras)

# Ejercicio 9
# Crea un programa que pida el número de palabras a introducir. Crear un diccionario de clave la palabra y
# de valor el número de vocales de la palabra. #

numero_palabras_introducir = int(input("¿Cuántas palabras vas a introducir? "))
palabras_dijitadas = {}

for _ in range(numero_palabras_introducir):
    palabra_ingrese = input("Palabra: ")
    palabra_ingrese = palabra_ingrese.lower()
    count = 0

    for c in palabra_ingrese:
        if c in "aeiou":
            count += 1

    print(f"Conteo de vocales en '{palabra_ingrese}': {count}")
    palabras_dijitadas[palabra_ingrese] = count

print("Palabras y sus conteos de vocales:")
for word, count in palabras_dijitadas.items():
    print(f"{word}: {count}")

#Ejercicio 10
# Dada una matriz, crea un diccionario que guarde el número de filas, el de columnas y cada fila en una entrada
# de un diccionario.#

matrix_biodimmensional = [[1, 2, 3, 4], [0, 2, 4, 6], [4, 3, 2, 1]]
dicc_inicializado = {"rows": len(matrix_biodimmensional), "columns": len(matrix_biodimmensional[0])}

for i in range(len(matrix_biodimmensional)):
    dicc_inicializado["row" + str(i)] = matrix_biodimmensional[i]

print(dicc_inicializado)
