# Ejercicio 1: Multiplicar un número por su anterior y siguiente
plus_before_after = lambda n: (n - 1) * n * (n + 1)
print(plus_before_after(10))  # Reemplaza 5 con el número que desees

# Ejercicio 2: Verificar si el primer número es mayor que el segundo
first_is_bigger = lambda x, y: x > y
print(first_is_bigger(7, 5))

# Ejercicio 3: Filtrar palabras con más vocales que consonantes
def more_vowels(w):
    """Devuelve si hay más vocales que consonantes en una palabra
    Args:
        w: Palabra en formato string
    Returns:
        Booleano
    """
    consonants = 0
    vowels = 0
    for char in w.lower():
        if char in ["a", "e", "i", "o", "u"]:
            vowels += 1
        else:
            consonants += 1
    return vowels > consonants

words = ["castaña", "lea", "asa", "boli", "mando", "aminoacido"]
filtered_words = list(filter(more_vowels, words))

print("Palabras con más vocales que consonantes:", filtered_words)

# Ejercicio 4: Filtrar números con más de 5 divisores
def total_divisors(n):
    """Calcula el número de divisores de un número entero positivo
    Args:
        n: Número entero positivo
    Returns:
        divisors: Lista de divisores de n
    """
    if isinstance(n, int) and n > 0:
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return len(divisors)

nums = [49, 1024, 666, 147, 2101, 12]
filtered_nums = list(filter(lambda n: total_divisors(n) > 5, nums))

print("Números con más de 5 divisores:", filtered_nums)

# Ejercicio 5: Encontrar la palabra más larga en una lista
from functools import reduce

def longer_word(w1, w2):
    """Devuelve la palabra de mayor longitud
    Args:
        w1: Palabra en formato string
        w2: Palabra en formato string
    Returns:
        Palabra en formato string
    """
    if len(w1) >= len(w2):
        return w1
    return w2

words = ["castaña", "termodinamico", "asa", "boli", "mando", "aminoacido"]
longest_word = reduce(longer_word, words)

print("La palabra más larga es:", longest_word)

# Ejercicio 6: Calcular el promedio de una lista de números
def average(nums):
    """Calcula el promedio de una lista de números
    Args:
        nums: Lista de números
    Returns:
        Promedio de los números
    """
    if nums:
        return sum(nums) / len(nums)
    return None

numbers = [10, 20, 30, 40, 50]
average_result = average(numbers)

print("El promedio es:", average_result)

# Ejercicio 7: Encontrar el máximo común divisor (MCD) de dos números
def gcd(a, b):
    """Calcula el máximo común divisor (MCD) de dos números
    Args:
        a: Primer número entero positivo
        b: Segundo número entero positivo
    Returns:
        MCD de a y b
    """
    while b:
        a, b = b, a % b
    return a

num1, num2 = 48, 60
gcd_result = gcd(num1, num2)

print("El MCD entre", num1, "y", num2, "es:", gcd_result)

# Ejercicio 8: Calcular el factorial de un número
def factorial(n):
    """Calcula el factorial de un número entero no negativo
    Args:
        n: Número entero no negativo
    Returns:
        Factorial de n
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

factorial_num = 5
factorial_result = factorial(factorial_num)

print("El factorial de", factorial_num, "es:", factorial_result)

# Ejercicio 9: Encontrar el número primo más grande en un rango dado
def is_prime(num):
    """Verifica si un número es primo
    Args:
        num: Número entero positivo
    Returns:
        Booleano que indica si el número es primo
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_in_range(start, end):
    """Encuentra el número primo más grande en un rango dado
    Args:
        start: Límite inferior del rango
        end: Límite superior del rango
    Returns:
        Número primo más grande en el rango
    """
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return max(primes)

range_start, range_end = 100, 200
largest_prime = largest_prime_in_range(range_start, range_end)

print("El número primo más grande entre", range_start, "y", range_end, "es:", largest_prime)

# Ejercicio 10: Encontrar el número triangular más grande en un rango dado
def is_triangular(num):
    """Verifica si un número es triangular
    Args:
        num: Número entero positivo
    Returns:
        Booleano que indica si el número es triangular
    """
    total = 0
    i = 1
    while total < num:
        total += i
        i += 1
    return total == num

def largest_triangular_in_range(start, end):
    """Encuentra el número triangular más grande en un rango dado
    Args:
        start: Límite inferior del rango
        end: Límite superior del rango
    Returns:
        Número triangular más grande en el rango
    """
    triangulars = [num for num in range(start, end + 1) if is_triangular(num)]
    return max(triangulars)

range_start, range_end = 100, 200
largest_triangular = largest_triangular_in_range(range_start, range_end)

print("El número triangular más grande entre", range_start, "y", range_end, "es:", largest_triangular)
