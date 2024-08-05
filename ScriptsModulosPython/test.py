#Ejercicio 9
#En un notebook de Google Colab, importa el script, crea dos objetos de 
# la clase Vector2D y prueba que todos los métodos de la clase Vector2D
#  funcionan correctamente.
# Asegúrate de que las clases Vector2D y Vector3D estén en el mismo directorio o ajusta la ruta de importación

from Tarea13 import Vector2D, Vector3D

# Crear un vector 2D
u = Vector2D(3, 4)
print(u)
print("El módulo del vector u es ||u|| =", u.module)

# Realizar el producto escalar con un escalar
u.scalar_prod(2)
print("2u =", u)
u.scalar_prod(1/2)

# Crear otro vector 2D
v = Vector2D(-1, 2)
print(v)

# Sumar y restar vectores
print(u, "+", v, "=", Vector2D.sum(u, v))
print(u, "-", v, "=", Vector2D.subtract(u, v))

# Producto punto de dos vectores
print("u·v =", u, "·", v, "=", Vector2D.dot_product(u, v))

# Distancia entre dos vectores
print("d(u, v) =", Vector2D.distance(u, v))

# Extender un vector 2D a 3D
u3d = u.extend_to_3D(5)
print(u3d)

#Ejercicio 10
#Ahora crea dos objetos de la clase Vector3D y prueba que todos los 
# métodos de la clase Vector3D funcionan correctamente.
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    @property
    def module(self):
        return math.sqrt(self.x**2 + self.y**2)

    def scalar_prod(self, a=1):
        self.x *= a
        self.y *= a

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

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return super().__str__()[:-1] + f", {self.z})"

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

# Pruebas (Yo quiero hacer mis pruebas locales porque es lo que mas voy a usar)
u = Vector3D(1, 0, -1)
print(u)
print("El módulo del vector u es ||u|| =", u.module)
u.scalar_prod(-3)
print("-3u =", u)
u.scalar_prod(-1/3)
v = Vector3D(-3, 1, 2)
print(v)
print(u, "+", v, "=", Vector3D.sum(u, v))
print(u, "-", v, "=", Vector3D.subtract(u, v))
print("u·v =", u, "·", v, "=", Vector3D.dot_product(u, v))
print("d(u, v) =", Vector3D.distance(u, v))
print(Vector3D.zero())
print(Vector3D.horizontal())
print(Vector3D.vertical())
print(Vector3D.forward())



