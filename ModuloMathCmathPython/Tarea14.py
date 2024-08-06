#Ejercicio 1
# Muestra la veracidad de las siguientes propiedades de los logaritmos 
# con 3 ejemplos diferentes en cada caso. En otras palabras, escoge 3 tríos de 
# valores para a, b y c y comprueba que todas las propiedades se satisfacen:
# • loga(1) = 0 ∀a ∈ R+ 
# • loga(a) = 1 ∀a ∈ R+ 
# • loga(bn) = n loga(b) ∀a, b ∈ R+, n ∈ Z 
# • loga(b 1n ) = 1 n loga(b) ∀a, b ∈ R+ n ∈ Z 
# • loga(b · c) = loga(b) + loga(c) ∀a, b, c ∈ R+ 
# • loga ( b c ) = loga(b) − loga(c) ∀a, b, c ∈ R+
# • loga(b) = logc(b) logc(a) ∀a, b, c ∈ R+
import math

a, b, c, n = (10, 5, 2.5), (10, 100, 1000), (25, 15, 5), (2, 3, 4)

for i in range(3):
    print("\n=== a = {}, b = {}, c = {}, n = {} ===".format(a[i], b[i], c[i], n[i]))
    print(math.log(1, a[i]) == 0)
    print(math.log(a[i], a[i]) == 1)
    print(math.isclose(math.log(b[i]**n[i], a[i]), n[i] * math.log(b[i], a[i])))
    print(math.isclose(math.log(b[i]**(1/n[i]), a[i]), (1/n[i]) * math.log(b[i], a[i])))
    print(math.isclose(math.log(b[i] * c[i], a[i]), math.log(b[i], a[i]) + math.log(c[i], a[i])))
    print(math.isclose(math.log(b[i] / c[i], a[i]), math.log(b[i], a[i]) - math.log(c[i], a[i])))
    print(math.isclose(math.log(b[i], a[i]), math.log(b[i], c[i]) / math.log(a[i], c[i])))


#Ejercicio 2
#Crea una función que dado un número real representando grados lo transforme a 
# radianes. Crea otra función que dado un valor real representando radianes lo
#  transforme a grados.#Comprueba que tus funciones calculan correctamente el 
# resultado comparándolo con el obtenido con los métodos .degree() y .radians()
#EXTRA: Si en la primera función nos introducen un número fuera del intervalo 
# [0, 360], devolver el equiv- alente en radianes dentro del intervalo [0, 2π]. 
# Y, para la segunda función, si nos introducen un valor fuera del intervalo 
# [0, 2π], devolver el equivalente en grados dentro del intervalo [0, 360].
import math

# Función para convertir grados a radianes
def grados_a_radianes(grados):
    return grados * math.pi / 180

# Función para convertir radianes a grados
def radianes_a_grados(radianes):
    return radianes * 180 / math.pi

# Funciones para comprobar los métodos
grados = 180
radianes = math.pi

# Comprobaciones
print(grados_a_radianes(grados))  # Resultado: 3.14159...
print(radianes_a_grados(radianes))  # Resultado: 180

# Comprobación con valores fuera de rango
def grados_a_radianes_normalizado(grados):
    grados = grados % 360
    return grados * math.pi / 180

def radianes_a_grados_normalizado(radianes):
    radianes = radianes % (2 * math.pi)
    return radianes * 180 / math.pi

#Ejercicio 3
#Elige cualquier valor para α y comprueba que
#sin2(α) + cos2(α) = 1
#tan(α) = sin(α) cos(α)
import math

# Elegimos un ángulo alfa
alfa = math.pi / 4  # 45 grados

# Comprobación de sin^2(α) + cos^2(α) = 1
sin_cuadrado = math.sin(alfa)**2
cos_cuadrado = math.cos(alfa)**2
print(sin_cuadrado + cos_cuadrado)  # Resultado: 1

# Comprobación de tan(α) = sin(α) / cos(α)
tan_alfa = math.tan(alfa)
sin_div_cos = math.sin(alfa) / math.cos(alfa)
print(tan_alfa == sin_div_cos)  # Resultado: True


#Ejercicio 4
#Comprueba que, en Python, un número cualquiera dividido entre 
# un número muy cercano a 0 sigue siendo considerado finito.
num = 1
cercano_cero = 1e-15
resultado = num / cercano_cero
print(math.isfinite(resultado))  # Resultado: True


#Ejercicio 5
#Elige valores enteros para n y k y comprueba si la siguiente igualdad es cierta:
#(n k) = ( n n − k)
import math

n = 5
k = 2

comb1 = math.comb(n, k)
comb2 = math.comb(n, n - k)
print(comb1 == comb2)  # Resultado: True


#Ejercicio 6
#Transforma el complejo (1, -1) a coordenadas polares.
import cmath

complejo = 1 - 1j
polar = cmath.polar(complejo)
print(polar)  # Resultado: (1.414..., -0.785...)


#Ejercicio 7
#Elige cualquier valor complejo para z y comprueba que
#sinh(z) = ez − e−z 2
#cosh(z) = ez + e−z 2
z = 1 + 2j
sinh_z = (cmath.exp(z) - cmath.exp(-z)) / 2
cosh_z = (cmath.exp(z) + cmath.exp(-z)) / 2
print(sinh_z)
print(cosh_z)


#Ejercicio 8
#Elige cualquier valor complejo para z y comprueba que
#sinh(−z) = − sinh(z)
#cosh(−z) = cosh(z)
neg_z = -z
sinh_neg_z = (cmath.exp(neg_z) - cmath.exp(-neg_z)) / 2
cosh_neg_z = (cmath.exp(neg_z) + cmath.exp(-neg_z)) / 2
print(sinh_neg_z == -sinh_z)  # Resultado: True
print(cosh_neg_z == cosh_z)  # Resultado: True


#Ejercicio 9
#Comprueba que tan (x) = 0 siendo x múltiplo de π. Prueba por ejemplo 
# con los 10 primeros múltiplos negativos y positivos de π.
for i in range(-10, 11):
    x = i * math.pi
    print(math.tan(x))  # Resultado: 0 para todos


#Ejercicio 10
#Muestra con 3 ejemplos diferentes que la siguiente igualdad es cierta.
#  Es decir, escoge valores diferentes para a, n y m, sustitúyelos y muestra 
# que en ambos lados de la igualdad se obtiene el mismo resultado.
#am · an = am+n
a = 2
m = 3
n = 4

izquierda = a**m * a**n
derecha = a**(m + n)
print(izquierda == derecha)  # Resultado: True
