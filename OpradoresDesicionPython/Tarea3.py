# Ejercicio 1 Haz que un usuario introduzca un número real y evalúa si dicho número es positivo, 
# negativo o cero. Devuelve por pantalla el resultado en cada caso.#

num = int(input("Por favor introduzca un numero "))

if num > 0:
    print("El numero es positivo")
elif num == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")

    
# Ejercicio 2 Haz que un usuario introduzca su nombre y evalúa con operadores if y else si dicho 
# nombre tiene una longitud mayor a 10 caracteres o no. Devuelve por pantalla el resultado en cada caso.#

name = input("Introduce tu nombre porfavor: ")

if len(name) > 10:
    print("Su nombre tiene una longitud de mas de 10 caracteres")
else:
    print("Su nombre tiene una longitud menor a 10 caracteres")

#Ejercicio 3 Realiza el ejercicio anterior con el uso del operador ternario.#

name = input("Introduce tu nombre please ")
resultado = "Su nombre es mayor a 10 caracteres" if len(name) > 10 else "Su nombre tiene menos de 10 caracteres"
print(resultado)

# Ejercicio 4 Haz que un usuario introduzca dos números enteros positivos. Comprueba si el primer número introducido por el usuario es mayor o igual que el segundo número introducido por el usuario. Devuelve
# por pantalla el resultado en cada caso. PISTA: Asegúrate de hacer uso de la función int() donde pertoque.

num1 = int(input("Dijite el primer numero entero positivo: "))
num2 = int(input("Dijite el segundo numero entero positivo: "))

if num1 >= num2:
    print("El numero {} es mayor que el {} numero".format(num1, num2))
else:
    print("El numero {} es mayor que el  {} numero".format(num2, num1))

# Ejercicio 5 Haz que un usuario introduzca dos números enteros positivos. Suponiendo que el primer 
# número introducido por el usuario es mayor o igual al segundo número introducido por el usuario, 
# comprueba que la división del primer número entre el segundo número es exacta. En caso de la división ser 
# exacta, devuelve el cociente por pantalla e indica que la división en efecto es exacta. En caso de la división no ser exacta, 
# devuelve el cociente y el resto por pantalla e indica que la división entre los dos números no es exacta#

numx = int(input("Ingrese primer numero entero positvo: "))
numy = int(input("Ingrese segundo numero entero: "))

if numx % numy == 0:
    print("La division del numero {} entre el numero {} es exacta {}".format(numx, numy, numx // numy))
else:
    print("La division del numero {} entre el numero {} no es exacta y su cociente es {} y su resto es  {}".format(numx, numy, numx // numy, numx % numy))

# Fusiona lo hecho en los ejercicios 4 y 5 para que 1. Un usuario introduzca dos números enteros 
# por pantalla. 2. Comprobar si el primer número es mayor o igual al segundo número introducido por 
# el usuario. Devolver por pantalla en que caso nos encontramos. 3. Hacer la división entera pertinente 
# en cada caso. 4. Si la división es exacta, entonces devolver por pantalla el cociente e indicar que 
# la división es exacta. Si la división no es exacta, entonces devolver por pantalla el cociente y
# el resto e indicar que la división realizada no es exacta.#

numero1 = int(input("Ingrese el 1er numero entero"))
numero2 = int(input("Ingrese el 2do numero entero"))

if numero1 >= numero2:
    print("El primer numero es mayor o igual que el segundo numero introducido")
    print("Dividimos el numero {} entre el numero {}".format(numero1, numero2))
    if numero1 % numero2 == 0:
        print("La division es exacta y el cociente es {}".format(numero1 // numero2))
    else:
        print("La division no es exacta y el cociente es {} y el resto es {}".format(numero1//numero2, numero1%numero2))
else:
    print("El segundo numero es mayor o igual que el primer numero introducido")
    print("Dividimos el numero {} mayor entre el numero {}".format(numero2, numero1))
    if numero2 % numero1 == 0:
        print("La division es exacta y el cociente es {}".format(numero2 // numero1))
    else:
        print("La division no es exacta y el cociente es {} y el resto es {}".format(numero2//numero1,numero2%numero1))

# Ejercicio 7 Haz que un usuario introduzca dos números enteros positivos. 
# Comprueba si el mayor es múltiplo del menor. Devuelve por pantalla el resultado en cada caso.#

numero3 = int(input("Ingresa un numero entero"))
numero4 = int(input("Ingresa un numero entero"))

if numero3 >= numero4:
    if numero3 % numero4:
        print("El primer numero es multiplo del segundo numero")

    else:
        print("El primer numero no es multiplo del segundo")

else:
    if numero4 % numero3:
        print("El segundo numero es multiplo del primer numero")
    else:
        print("El segundo numero no es multiplo del primer numero")

# Ejercicio 8 Haz que un usuario introduzca una palabra y comprueba si dicha palabra empieza por mayúscula.
# Devuelve por pantalla el resultado en cada caso.#

string1 = input("Introduce una palabra sin espacios: ")
if string1.find(" ") == -1:
    print("El string no tiene espacios")
    if string1 [0].isupper():
        print("El string inicia por mayuscula")
    else:
        print("El string no inicia por mayuscula")
else:
    print("El string tiene espacios")

# Ejercicio 9 Haz un usuario introduza una letra y comprueba si se trata de una vocal. Si el usuario introduce un string de más de un carácter, infórmale de que no se puede procesar el dato, pues debe tener como máximo tamaño 
# 1. PISTA: Convierte la letra introducida a minúsculas para tener que realizar menos comprobaciones#

letter = input("Introduce una letra: ").lower()

if len(letter) == 1 and letter.isalpha():
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print("La letra es vocal")
    else:
        print("la letra es una consonante")
else:
    print("el string dijitado no es una letra")

# Ejercicio 10 #

import math

# Solicita los coeficientes de la ecuación al usuario
print("Dada la ecuación de segundo grado de la forma ax^2 + bx + c = 0")
print("Por favor, introduzca los coeficientes de la ecuación que desea resolver.")
a = float(input("Coeficiente a = "))
b = float(input("Coeficiente b = "))
c = float(input("Coeficiente c = "))

# Verifica que no se trate de una ecuación de primer grado
if a != 0:
    # Calcula el discriminante
    disc = b**2 - 4*a*c
    
    if disc > 0:
        # Dos soluciones reales y diferentes
        sol1 = (-b + math.sqrt(disc)) / (2*a)
        sol2 = (-b - math.sqrt(disc)) / (2*a)
        print("Hay dos soluciones: x = {} y x = {}".format(sol1, sol2))
    elif disc == 0:
        # Una solución real
        sol = -b / (2*a)
        print("Hay una solución que se repite: x = {}".format(sol))
    else:
        # Soluciones complejas
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)
        print("Hay dos soluciones complejas: x = {} + {}i y x = {} - {}i".format(real_part, imag_part, real_part, imag_part))
else:
    print("No se trata de una ecuación de segundo grado, ya que a = 0")
