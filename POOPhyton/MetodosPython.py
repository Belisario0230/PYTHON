
#Métodos de instancia:
#Estos métodos están asociados a un objeto específico y pueden acceder a 
# sus atributos.
#Se definen dentro de la clase y toman self como su primer parámetro.
#Ejemplo: Utiliza el parametro SELF #

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

persona1 = Persona(nombre="Juan")
print("Metodo de Instancia")
persona1.saludar()  # Imprime "Hola, soy Juan."

#Métodos de clase:
#Son compartidos por todos los objetos de la clase y no acceden a atributos 
# específicos de un objeto.
#Se definen usando el decorador @classmethod.
#Ejemplo: utiliza el parametro CLS #
class Circulo:
    pi = 3.14

    @classmethod
    def calcular_area(cls, radio):
        return cls.pi * radio**2

area = Circulo.calcular_area(radio=5)
print("Metodo de Clase")
print(f"Área del círculo: {area}")  # Imprime "Área del círculo: 78.5"

#Métodos estáticos:
#No dependen de instancias y no acceden a atributos de la clase ni del objeto.
#Se definen usando el decorador @staticmethod.
#Ejemplo: #
class Utilidades:
    @staticmethod
    def sumar(a, b):
        return a + b

resultado = Utilidades.sumar(a=10, b=20)
print("Metodo de Estatico")
print(f"Resultado de la suma: {resultado}")  # Imprime "Resultado de la suma: 30"

