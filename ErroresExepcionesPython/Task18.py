#Ejercicio 1
# Dada la función divisors(), asegura con assert que el parámetro n se trata de un número 
# entero positivo. De lo contrario, muestra como mensaje que "n debe ser de tipo int y 
# debe ser mayor que 0"
# def divisors(n): """ Calcula los divisores de un número entero positivo. 
# Args: n: Número entero positivo Returns: divisors: Lista de 
# divisores de n """ divisors = [] for i in range(1, n + 1): if n % i == 0: divisors.append(i) 
# return divisors
def divisors(n):
    """
    Calcula los divisores de un número entero positivo.

    Args:
        n: Número entero positivo

    Returns:
        divisors: Lista de divisores de n
    """

def imprimir_divisores(n):
    assert type(n) == int and n > 0, "n debe ser de tipo int y debe ser mayor que 0 y usamos la declaracion assertionError"
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    print(divisors)

# Ejemplo de uso
#imprimir_divisores(-2)
#imprimir_divisores(y)
imprimir_divisores(2)

#Ejercicio 2
#Dada la función divisors(), muestra TypeError con el mensaje correspondiente si 
# el parámetro n no se trata de un número entero y muestra ValueError con el mensaje 
# correspondiente si n no se trata de un número positivo.
#def divisors(n): """ Calcula los divisores de un número entero positivo. Args:
#  n: Número entero positivo Returns: divisors: Lista de divisores de n """ divisors = [] for 
# i in range(1, n + 1): if n % i == 0: divisors.append(i) return divisors
def divisors(n):
    """
    Calcula los divisores de un número entero positivo.

    Args:
        n: Número entero positivo

    Returns:
        divisors: Lista de divisores de n
    """
    if type(n) != int:
        raise TypeError("n debe ser de tipo int y la decalracion para su validacion es ValueError")
    if n <= 0:
        raise ValueError("n debe ser positivo y la decalracion para su validacion es ValueError")
    
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    
    return divisors

# Ejemplo de uso
#n = 12
n = 12
#n = -12
print(f"Los divisores de {n} son: {divisors(n)}")

#Ejercicio 3
#Dada la función is_palindrome(), asegura con assert que el parámetro word se trata 
# de una variable de tipo string. De lo contrario, muestra como mensaje que "word debe 
# ser de tipo string".
#def is_palindrome(word): """ Devuelve si la palabra word es palíndroma. Args: word: 
# Palabra Returns: isPalindrome: Booleano """ word = word.lower() l = [] isPalindrome = 
# True for c in word: l.append(c) n = len(l) for i in range(int(n / 2)): if l[i] != l[n - 
# (i + 1)]: isPalindrome = False return isPalindrome
def is_palindrome(word):
    """
    Devuelve si la palabra word es palíndroma.

    Args:
        word: Palabra

    Returns:
        isPalindrome: Booleano
    """
    assert type(word) == str, "word debe ser una variable de tipo string"
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
palabra = "reconocer"
#palabra = 12346
print(f"¿La palabra '{palabra}' es palíndroma? {is_palindrome(palabra)}")

#Ejercicio 4
#Dada la función is_palindrome(), muestra TypeError con el mensaje correspondiente si word 
# no se trata de una variable de tipo string.
#def is_palindrome(word): """ Devuelve si la palabra word es palíndroma. Args: word:
#  Palabra Returns: isPalindrome: Booleano """ word = word.lower() l = [] isPalindrome = 
# True for c in word: l.append(c) n = len(l) for i in range(int(n / 2)): if l[i] != l[n - 
# (i + 1)]: isPalindrome = False return isPalindrome
def is_palindrome(word):
    """
    Devuelve si la palabra word es palíndroma.

    Args:
        word: Palabra

    Returns:
        isPalindrome: Booleano
    """
    if type(word) != str:
        raise TypeError("word debe ser una variable de tipo string y usa la declaracion TypeError")
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
palabra = "anilina"
#palabra = 1234
print(f"¿La palabra '{palabra}' es palíndroma? {is_palindrome(palabra)}")

#Ejercicio 5
#Dada la función is_palindrome(), muestra ValueError con el mensaje correspondiente 
# si word no se trata de una palabra. Es decir, si una vez ha pasado la comprobación 
# de ser una variable de tipo string, comprueba que no tiene espacios.
#def is_palindrome(word): """ Devuelve si la palabra word es palíndroma. Args:
#2word: Palabra Returns: isPalindrome: Booleano """ word = word.lower() l = [] isPalindrome 
# = True for c in word: l.append(c) n = len(l) for i in range(int(n / 2)): if l[i] !=
#  l[n - (i + 1)]: isPalindrome = False return isPalindrome
def is_palindrome(word):
    """
    Devuelve si la palabra word es palíndroma.

    Args:
        word: Palabra

    Returns:
        isPalindrome: Booleano
    """
    if type(word) != str:
        raise TypeError("word debe ser una variable de tipo string")
    if " " in word:
        raise ValueError("word debe ser una palabra y no debe contener espacios la declaracion es ValueError")
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
palabra = "sometemos"
#palabra "some   temos"
#palabra "some#$%"

print(f"¿La palabra '{palabra}' es palíndroma? {is_palindrome(palabra)}")

#Ejercicio 6
#Dada la función is_palindrome() del resultado del ejercicio anterior, modifícala de modo 
# que acepte no solo palabras sino también frases y devuelva si el string introducido es 
# palíndromo o no. Recuerda tener en cuenta la excepción TypeError junto al mensaje 
# correspondiente.
def is_palindrome(s):
    """
    Devuelve si la palabra s es palíndroma.

    Args:
        s: Palabra

    Returns:
        isPalindrome: Booleano
    """
    if type(s) != str:
        raise TypeError("s debe ser una variable de tipo string")
    s = s.lower()
    s = s.replace(" ", "")
    l = []
    isPalindrome = True
    for c in s:
        l.append(c)
    n = len(l)
    for i in range(int(n / 2)):
        if l[i] != l[n - (i + 1)]:
            isPalindrome = False
    return isPalindrome

# Ejemplo de uso
palabra = "radar"
#palabra = 1234
print(f"¿La frase '{palabra}' es palíndroma? {is_palindrome(palabra)}")


#Ejercicio 7
#Utiliza try / except para dado un objeto de Python guardado en la variable x, 
# aplicarle el método .index() y localizar el elemento "c". En el bloque try, guarda 
# el resultado en la variable result. En el bloque except, en la variable result, si 
# el objeto x es una lista, guarda el mensaje "La lista no tiene el elemento "c". En 
# caso contario, guarda el mensaje "El objeto {tipo del objeto que sea x} no tiene el 
# método .index()". Finalmente, imprime por pantalla el resultado.

#x = ["a", "b", "C"]
x = {"a", "b", "C"}#

try:
    result = x.index("c")
except:
    if type(x) == list:
        result = 'La lista no tiene el elemento \"c\"'
    else:
        result = "El objeto {} no tiene el método .index()".format(type(x).__name__)

print(result)

#Ejercicio 8
#Crea una función que calcule el área de un cuadrado. Como parámetro se 
# recibirá un número real, correspondiente a la longitud de la base. Lanza 
# las excepciones pertinentes siempre que el parámetro no se trate de un número 
# real o entero positivo.
def square_area(base):
    """
    Calcula el área de un cuadrado de lado base.

    Args:
        base: Variable numérica

    Returns:
        base ** 2: Variable numérica
    """
    if not isinstance(base, (int, float)):
        raise TypeError("El parámetro base debe ser de tipo int o float")
    if base < 0:
        raise ValueError("El parámetro base debe ser positivo")
    return base ** 2

# Ejemplo de uso
lado = 5
#lado = "ab"
print(f"El área de un cuadrado con lado {lado} es: {square_area(lado)}")


#Ejercicio 9
#Crea una función que solicite al usuario la edad. Lanza una excepción en caso de que no
#  se trate de una edad válida. Se considera edad no válida una edad negativa o mayor a 
# 150. En cada caso, lanza el mensaje correspondiente.
def user_age():
    """
    Pide al usuario su edad.

    Returns:
        age: Número entero
    """
    age = int(input("Introduce tu edad: "))
    if age < 0:
        raise ValueError("No existen las edades negativas")
    elif age > 118:
        raise ValueError("Una persona no puede tener más de 119 años")
    return age

# Ejemplo de uso
try:
    edad = user_age()
    print(f"Tu edad es: {edad}")
except ValueError as e:
    print(e)


#Ejercicio 10
# Crea una función que solicite al usuario una letra en mayúscula. Lanza una excepción en
#  caso de que el usuario no haya introducido nada, no haya introducido una letra, no haya
#  introducido una letra mayúscula o no haya introducido solamente un caracter.
def get_upper_letter():
    """
    Pide al usuario una letra mayúscula.

    Returns:
        letter: Letra mayúscula
    """
    letter = input("Introduce una letra mayúscula: ")
    if len(letter) > 1:
        raise ValueError("Has introducido más de un caracter")
    elif len(letter) == 0:
        raise ValueError("No has introducido nada")
    else:
        if not letter.isalpha():
            raise ValueError("No has introducido una letra")
        else:
            if not letter.isupper():
                raise ValueError("No has introducido una letra mayúscula")
    print("La letra que has introducido es", letter)

# Ejemplo de uso
try:
    get_upper_letter()
except ValueError as e:
    print(e)
