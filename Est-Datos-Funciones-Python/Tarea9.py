#Ejercicio 1
#Crea una función que busque todos los divisores del número entero positivo dado por parámetro 
# y devuelva una lista con todos los divisores de dicho número.

def divisores(numero):
    """
    Calcula los divisores de un número entero positivo.
    
    Args:
        numero: Número entero positivo
    
    Returns:
        divisores: Lista de divisores de numero
    """
    if type(numero) == int and numero > 0:
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return divisores
    else:
        print("El parámetro introducido debe ser un número entero positivo")

#Ejemplo de Uso
numero = 100
divisores_de_numero = divisores(numero)
print(f"Los divisores de {numero} son: {divisores_de_numero}")

#Ejercicio 2
#Crea una función que dados dos números reales por parámetro, devuelve el mayor.

def numero_Mayor(a, b):
    """
    Devuelve el mayor número de 2 números reales dados.
    
    Args:
        a: Número real
        b: Número real
    
    Returns:
        Número real
    """
    if a >= b:
        return a
    return b

# Ejemplo de uso
numero1 = 5.5
numero2 = 3.8
mayor_numero = numero_Mayor(numero1, numero2)
print(f"El mayor número entre {numero1} y {numero2} es: {mayor_numero}")

#Ejercicio 3
#Crea una función que dado un número devuelva su valor absoluto. Recuerda,
#|x| = { x si x >= 0 −x si x < 0

def absolute_value(x):
    """
    Devuelve el valor absoluto de un número real.
    
    Args:
        x: Número real
    
    Returns:
        Número real
    """
    if x >= 0:
        return x
    return -x

# Ejemplo de uso
numero = -8.9
valor_absoluto = absolute_value(numero)
print(f"El valor absoluto de {numero} es: {valor_absoluto}")

#Ejercicio 4
#Crea una función que devuelva True si el caracter introducido por parámetro se trata de una vocal 
# y False en caso contrario.

def es_una_vocal(es_una_letra):
    """
    Devuelve si el caracter dado es una vocal.
    
    Args:
        c: Caracter
    
    Returns:
        Booleano
    """
    if len(es_una_letra) == 1:
        if es_una_letra.lower() in ["a", "e", "i", "o", "u"]:
            return True
        return False
    else:
        print("El valor introducido debe ser un solo caracter")

# Ejemplo de uso
es_una_letra = 't'
es_una_vocal = es_una_vocal(es_una_letra)
print(f"¿El carácter '{es_una_letra}' es una vocal? {es_una_vocal}")

#Ejercicio 5
#Crea una función que devuelva el MCD (máximo común divisor) de 2 números proporcionados por 
# parámetro.
#PISTA: Aprovecha la función que calcula el mayor entre dos números dados. También 
# necesitarás una función que calcula el menor entre dos números dados.

def bigger(a, b):
    """
    Devuelve el mayor número de 2 números reales dados.
    
    Args:
        a: Número real
        b: Número real
    
    Returns:
        Número real
    """
    if a >= b:
        return a
    return b

def lower(a, b):
    """
    Devuelve el menor número de 2 números reales dados.
    
    Args:
        a: Número real
        b: Número real
    
    Returns:
        Número real
    """
    if a <= b:
        return a
    return b

def mcd(a, b):
    """
    Devuelve el MCD de dos números enteros.
    
    Args:
        a: Número entero
        b: Número entero
    
    Returns:
        max: Número entero
    """
    r = 0
    max = bigger(a, b)
    min = lower(a, b)
    while min > 0:
        r = min
        min = max % min
        max = r
    return max

# Ejemplo de uso
numero1 = 48
numero2 = 18
mcd_resultado = mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es: {mcd_resultado}")

#Ejercicio 6
#Crea una función que devuelva el MCM (mínimo común múltiplo) de 2 números proporcionados 
# por parámetro.
#PISTA: Aprovecha la función que calcula el MCD de dos números del ejercicio anterior 
# y la función que calcula el valor absoluto de un número.

# Definición de las funciones necesarias
def absolute_value(x):
    if x >= 0:
        return x
    return -x

def mcd(a, b):
    r = 0
    max = bigger(a, b)
    min = lower(a, b)
    while min > 0:
        r = min
        min = max % min
        max = r
    return max

def bigger(a, b):
    if a >= b:
        return a
    return b

def lower(a, b):
    if a <= b:
        return a
    return b

# Definición de la función mcm
def mcm(a, b):
    return absolute_value(a * b) // mcd(a, b)

# Ejemplo de uso
numero1 = 12
numero2 = 15
mcm_resultado = mcm(numero1, numero2)
print(f"El MCM de {numero1} y {numero2} es: {mcm_resultado}")

#Ejercicio 7
#Crea una función que dada una palabra devuelva si es palíndroma.

def is_palindrome(word):
    """
    Devuelve si la palabra word es palíndroma.
    
    Args:
        word: Palabra
    
    Returns:
        isPalindrome: Booleano
    """
    word = word.lower()
    l = []
    isPalindrome = True
    for c in word:
        l.append(c)
    n = len(l)
    for i in range(int(n / 2)):
        if l[i] != l[n - (i + 1)]:
            isPalindrome = False
    return isPalindrome

# Ejemplo de uso
palabra = "Radar"
es_palindromo = is_palindrome(palabra)
print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo}")

#Ejercicio 8
#Crea una función que dado un color en hexadecimal devuelva una lista de 3 posiciones, 
# cada una de ellas correspondiente al valor R, G o B en este orden. Los valores de RGB 
# varían entre 0 y 255.

def hex_to_decimal(hex_num):
    """
    Dado un número hexadecimal en formato string lo transforma a número decimal.
    
    Args:
        hex_num: String
    
    Returns:
        dec: Número entero
    """
    hex_to_dec = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }
    dec = 0
    for i in range(len(hex_num)):
        dec += hex_to_dec[hex_num[i]] * 16 ** (len(hex_num) - (i + 1))
    return dec

def hex_color_to_rgb(color_hex):
    """
    Dado un color en forma hexadecimal lo devuelve en forma RGB.
    
    Args:
        color_hex: String de 6 caracteres
    
    Returns:
        rgb: Lista de tamaño 3
    """
    color_hex = color_hex.upper()
    if len(color_hex) == 6:
        r = color_hex[:2]
        r = hex_to_decimal(r)
        g = color_hex[2:4]
        g = hex_to_decimal(g)
        b = color_hex[4:]
        b = hex_to_decimal(b)
        return [r, g, b]
    else:
        print("Un color en forma hexadecimal consta de 6 caracteres")

# Ejemplo de uso
color_hex = "1A2B3C"
rgb = hex_color_to_rgb(color_hex)
print(f"El color hexadecimal {color_hex} en formato RGB es: {rgb}")


#Ejercicio 9
#Crea una función que dada una lista de palabras por parámetro, devuelva un diccionario 
# que contenga cuántas son de longitud par y cuántas de longitud impar.

def even_odd_words(list_of_words):
    """
    Dada una lista de palabras, devuelve cuántas tienen longitud par e impar.
    
    Args:
        list_of_words: Lista de palabras
    
    Returns:
        info: Diccionario
    """
    info = {"even": 0, "odd": 0}
    for word in list_of_words:
        if len(word) % 2 == 0:
            info["even"] += 1
        else:
            info["odd"] += 1
    return info

# Ejemplo de uso
lista_de_palabras = ["hola", "mundo", "python", "es", "genial", "para", "programar"]
resultado = even_odd_words(lista_de_palabras)
print(f"Palabras con longitud par: {resultado['even']}, Palabras con longitud impar: {resultado['odd']}")


#Ejercicio 10
#Crea una función que dado un string por parámetro cuente cuántas veces sale cada caracter en
#  dicho string y devuelva toda esa información en un diccionario.

def count_characters(s):
    """
    Dado un string, devuelve un diccionario con el número de apariciones
    de cada caracter del string.
    
    Args:
        s: String
    
    Returns:
        info: Diccionario
    """
    s = s.lower()
    info = {}
    for c in s:
        if c == " ":
            if "blank" not in info.keys():
                info["blank"] = s.count(c)
        elif c not in info.keys():
            info[c] = s.count(c)
    return info
# Ejemplo de uso
texto = "Hola Mundo"
resultado = count_characters(texto)
print(f"Conteo de caracteres en '{texto}': {resultado}")
