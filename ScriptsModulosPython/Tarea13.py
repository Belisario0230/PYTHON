#Ejercicio 1
#Crea un script llamado vectors.py. Ábrelo y crea una clase llamada 
# Vector2D. El constructor debe guardar las coordenadas x e y del vector.
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Ejercicio 2
#Crea los siguientes métodos:
#• La propiedad .module que devuelva el módulo del vector. Recuerda que el 
# módulo de un vector 2D se calcula como √x2 + y2. Para calcular raíces 
# cuadradas, dispones del método math.sqrt(). • El método de instancia 
# .scalar_prod() que multiplique el vector por el número real dado por parámetro, que por defecto vale 1.
#Configura el método .__str__ para que se nos muestre por pantalla el vector 
# de la forma (x, y).
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def module(self):
        return math.sqrt(self.x**2 + self.y**2)

    def scalar_prod(self, a=1):
        self.x *= a
        self.y *= a

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

#Ejercicio 3
#Crea los siguientes métodos:
#• El método de clase .sum() que dados dos vectores los sume y devuelva un
#  objeto de la clase Vector2D. • El método de clase .subtract() que dadoas 
# dos vectores los reste y devuelva un objeto de la clase Vector2D.
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def module(self):
        return math.sqrt(self.x**2 + self.y**2)

    def scalar_prod(self, a=1):
        self.x *= a
        self.y *= a

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    @classmethod
    def sum(cls, u, v):
        return cls(u.x + v.x, u.y + v.y)

    @classmethod
    def subtract(cls, u, v):
        return cls(u.x - v.x, u.y - v.y)

#Ejercicio 4
#Crea los siguientes métodos:
#• El método estático .dot_product() que dados dos vectores calcule 
# su producto escalar. Recuerda que el producto escalar de 2 vectores 
# 2D u y v se calcula como u · v = uxvx + uy vy• El método de clase 
# .distance() que dados dos vectores calcule la distancia entre ellos. Recuerda 
# que la distancia entre 2 vectores 2D u y v se 
# calcula como √(ux − vx)2 + (uy − vy )2
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def module(self):
        return math.sqrt(self.x**2 + self.y**2)

    def scalar_prod(self, a=1):
        self.x *= a
        self.y *= a

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    @classmethod
    def sum(cls, u, v):
        return cls(u.x + v.x, u.y + v.y)

    @classmethod
    def subtract(cls, u, v):
        return cls(u.x - v.x, u.y - v.y)

    @staticmethod
    def dot_product(u, v):
        return u.x * v.x + u.y * v.y

    @classmethod
    def distance(cls, u, v):
        return cls.subtract(u, v).module

#Ejercicio 5
#Ahora crea la clase Vector3D que herede de la clase Vector2D. Empieza 
# con el constructor para que además de las coordenadas x e y, también 
# tome la coordenada z. Recuerda que puedes utilizar el método .super()
#  para acceder a métodos de la clase padre.
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

#Ejercicio 6
#Crea en la clase Vector3D los métodos siguientes:
#• el método .__str__() para que muestre el vector por pantalla de 
# la forma (x, y, z). • la propiedad .module. Al tener vectores 3D, el 
# módulo se calcula como √x2 + y2 + z2 • el método de instancia .scalar_prod() 
# • los métodos de clase .sum() y .subtract() para que devuelvan objetos 
# de la clase Vector3D. • el método estático .dot_product(), pues ahora el 
# producto escalar se calcula como u · v = uxvx + uy vy + uz vz• el método 
# de clase .distance(), pues ahora la distancia se calcula como √ (ux − vx)2 
# + (uy − vy )2 + (uz − vz )2
#Recuerda que dispones del método .super() para evitar repeticiones 
# innecesarias de código.
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    @property
    def module(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def scalar_prod(self, a=1):
        super().scalar_prod(a)
        self.z *= a

    @classmethod
    def sum(cls, u, v):
        return cls(u.x + v.x, u.y + v.y, u.z + v.z)

    @classmethod
    def subtract(cls, u, v):
        return cls(u.x - v.x, u.y - v.y, u.z - v.z)

    @staticmethod
    def dot_product(u, v):
        return super(Vector3D, Vector3D).dot_product(u, v) + u.z * v.z

    @classmethod
    def distance(cls, u, v):
        return cls.subtract(u, v).module


#Ejercicio 7
#Crea en la clase Vector3D los métodos siguientes:
#• el método de clase .zero() que devuelva un objeto Vector3D con
#  todas sus componentes 0. • el método de clase .horizontal() que
#  devuelva un objeto Vector3D con todas sus componentes 0 salvo la primera
#  que valdrá 1. • el método de clase .vertical() que devuelva un objeto
#  Vector3D con todas sus componentes 0 salvo la segunda que valdrá 1. • 
# el método de clase .forward() que devuelva un objeto Vector3D con todas 
# sus componentes 0 salvo la tercera y última que valdrá 1.
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    @property
    def module(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def scalar_prod(self, a=1):
        super().scalar_prod(a)
        self.z *= a

    @classmethod
    def sum(cls, u, v):
        return cls(u.x + v.x, u.y + v.y, u.z + v.z)

    @classmethod
    def subtract(cls, u, v):
        return cls(u.x - v.x, u.y - v.y, u.z - v.z)

    @staticmethod
    def dot_product(u, v):
        return super(Vector3D, Vector3D).dot_product(u, v) + u.z * v.z

    @classmethod
    def distance(cls, u, v):
        return cls.subtract(u, v).module

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)

    @classmethod
    def horizontal(cls):
        return cls(1, 0, 0)

    @classmethod
    def vertical(cls):
        return cls(0, 1, 0)

    @classmethod
    def forward(cls):
        return cls(0, 0, 1)


#Ejercicio 8
#Crea en la clase Vector2D el método de instancia .extend_to_3D() que 
# devuelva un objeto de la clase Vector3D siendo la componente z el valor 
# indicado por parámetro, que por defecto valdrá 0.
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def module(self):
        return math.sqrt(self.x**2 + self.y**2)

    def scalar_prod(self, a=1):
        self.x *= a
        self.y *= a

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    @classmethod
    def sum(cls, u, v):
        return cls(u.x + v.x, u.y + v.y)

    @classmethod
    def subtract(cls, u, v):
        return cls(u.x - v.x, u.y - v.y)

    @staticmethod
    def dot_product(u, v):
        return u.x * v.x + u.y * v.y

    @classmethod
    def distance(cls, u, v):
        return cls.subtract(u, v).module

    def extend_to_3D(self, z=0):
        return Vector3D(self.x, self.y, z)


