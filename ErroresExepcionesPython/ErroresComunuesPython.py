"""
ArithmeticError

result = 1 / 0
#Explicación: Este código intenta dividir por cero, lo que no está permitido en matemáticas.

AssertionError

assert 1 == 2, "1 no es igual a 2"
#Explicación: La declaración assert falla porque la condición es falsa.

AttributeError

class MyClass:    pass
obj = MyClass() obj.some_attribute
#Explicación: Se intenta acceder a un atributo que no existe en el objeto.

EOFError
input("Presiona Enter sin escribir nada: ")
#Explicación: La función input() llega al final del archivo sin recibir datos.

FloatingPointError

import math math.exp(1000)
#Explicación: La operación en coma flotante falla debido a un valor demasiado grande.

ImportError

import non_existent_module
#Explicación: Se intenta importar un módulo que no existe.

IndentationError
def my_function():
print("Hola")
#Explicación: La indentación no es correcta.

IndexError
my_list = [1, 2, 3] 
my_list[5]
#Explicación: Se intenta acceder a un índice que está fuera del rango de la lista.

KeyError
my_dict = {"a": 1} 
my_dict["b"]
#Explicación: Se intenta acceder a una clave que no existe en el diccionario.

KeyboardInterrupt
try:    
    while True:        
        pass
except KeyboardInterrupt:    
    print("Interrupción del teclado")
#Explicación: El usuario interrumpe la ejecución del programa con Ctrl+C.

LookupError
my_dict = {"a": 1} 
my_dict["b"]
#Explicación: Este es un error general que incluye IndexError y KeyError.

MemoryError
a = ' ' * 10**10
#Explicación: Se intenta asignar más memoria de la disponible.

NameError
print(non_existent_variable)
#Explicación: Se intenta usar una variable que no ha sido definida.

NotImplementedError
class MyClass:    
    def my_method(self):        
        raise NotImplementedError("Este método debe ser sobreescrito") 
obj = MyClass() 
obj.my_method()
#Explicación: Se llama a un método que debe ser implementado por una subclase.

OverflowError
import math math.exp(1000)
#Explicación: El resultado de una operación aritmética es demasiado grande para ser representado.

RuntimeError
raise RuntimeError("Este es un error de tiempo de ejecución")
#Explicación: Un error general que no encaja en ninguna otra categoría.

TabError
def my_function():    
      print("Hola")
#Explicación: La indentación consiste en tabulaciones y espacios en blanco inconsistentes.

TypeError
"2" + 2
#Explicación: Se intenta sumar una cadena y un entero, lo cual no es permitido.

ValueError
int("hola")
#Explicación: Se intenta convertir una cadena que no representa un número a un entero.

ZeroDivisionError
result = 1 / 0 Explicación Se intenta dividir por cero
#Explicacion: Se intenta dividir por cero
"""