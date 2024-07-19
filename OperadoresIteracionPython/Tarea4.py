# Ejerciico No 1 Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, 
# muestra si el número introducido es par o impar.#


print("Por favor introduce un numero entero")
numero_entero = int(input("Introduce un numero entero ya sea par o impar y caundo quieras salir del bucle solo introduce el numero 0: "))
while numero_entero != 0:
        print("El numero {} es {}".format(numero_entero, "Par" if numero_entero % 2 == 0 else "Impar"))
        numero_entero = int(input())
else:
    print("Has salido del bucle")

# Ejercicio No 2 Haz que el usuario introduzca una palabra y una letra por teclado. Comprueba si 
# la palabra contiene la letra o no e indícaselo al usuario por pantalla.#

print("Introduce una palabra")
palabra_usuario = input()
print("Introduce una letra")
letra_usuario = input()

i = 0
found = False
while i < len(palabra_usuario):
      if palabra_usuario[i] == letra_usuario:
            found = True
            break
      i += 1
print("La palabra {} {} contiene la letra {}".format(palabra_usuario, "Si" if found else "No", letra_usuario))

# Ejercicio No 3 Haz que el usuario introduzca precios por teclado (si introduce 0, entonces 
# es que ha finalizado). Si el usuario pasa de 200€, entonces ya no debe poder introducir más precios 
# pues se ha pasado del presupuesto. Sea cual sea el resultado 
# (o bien el precio final o bien que no tiene más presupuesto), indícaselo por pantalla al usuario. #

print("Por favor dijita los precios y recuerda que cuando quieras salir del bucle puedes dijitar el numero 0: ")
precio_dijitado = float(input())
total_presupuesto = precio_dijitado

while precio_dijitado != 0:
      if total_presupuesto >= 200:
            break
      precio_dijitado = float(input())
      total_presupuesto += precio_dijitado

if total_presupuesto > 200:
      print("No tiene mas presupuesto; Por favor verifique: ")
else:
      print("El total del presupuesto es : {}".format(total_presupuesto))

# Ejerciico No 4 Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, 
# calcula cuántos números positivos y cuántos negativos ha introducido y muéstraselo al final.#

print("dijite un numero entero: ")
numero_dijitado2 = int(input())
numero_positivo = 0
total_numero_ingresados = 0
while numero_dijitado2 != 0:
      if numero_dijitado2 > 0:
            numero_positivo += 1
      total_numero_ingresados += 1
      numero_dijitado2 = int(input())
print("De los {} numeros dijitados, {} son positivos y {} y negativos".format(numero_dijitado2, numero_positivo, total_numero_ingresados - numero_positivo))
      

# Ejercicio No 5 Haz que el usuario introduzca números por teclado. Mientras el usuario no introduzca el 0,
# pídele otro número. Cuando el usuario introduzca el 0, muéstrale la media aritmética 
# de los números que ha introducido.#

print("Ingresa un numero entero")
numero_dijitado3 = int(input())
med_arimetica = 0
total = 0
while numero_dijitado3 != 0:
      total += 1
      med_arimetica = (med_arimetica * ( total - 1) + numero_dijitado3) / total
      numero_dijitado3 = int(input())
print("La media arimetica de los numeros que has introducido es", med_arimetica)

# Ejercicio No 6 Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo 
# del intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se 
# encuentren entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, 
# muestra por pantalla el resultado de la suma #

numero1 = int(input("Extermo izquierdo"))
numero2 = int(input("Extermo Derecho"))

for i in range(numero1, numero2 + 1):
    print(i)

# Ejerciico No 7 Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se encuentren
# entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, muestra por pantalla
# el resultado de la suma.#

numero1 = int(input("Extermo izquierdo"))
numero2 = int(input("Extermo Derecho"))

for i in range(numero1, numero2 + 3):
    print(i)

# Ejercicio No 8 Pídele al usuario cuántos números va a introducir. Con un bucle for, solicítale esa cantidad de números y
# calcula su producto.#

numero = int(input("Que numero vas a dijitar: "))
producto = 1

for i in range(numero):
      numero_dijitado = int(input())
      producto *= numero_dijitado
print("El producto de los numeros dijitados es",numero, numero_dijitado, producto)

# Ejercicio No 9 Haz que el usuario introduzca su edad y el año actual. Imprime todos los años que han pasado desde su año
# de nacimiento hasta el año actual (ambos incluidos) #

edad = int(input("Dijita tu Edad: "))
año_actual = int(input("Dijita el año actual: "))
for i in range(año_actual, año_actual - edad -1, -1):
    print(i)

# Ejercicio No 10 Haz que el usuario introduzca un número entero. Muestra un cuadrado y luego un triángulo rectángulo de
# lado y altura, respectivamente, el número entero introducido. Por ejemplo, si el usuario introduce como
# número 5, se deberá mostrar: #

numero = int(input("Dijita un Número entero: "))    
for i in range(numero):
    print("* "*(i+1)+" "*(20-(2*i+2)+1)+"* "*numero)
