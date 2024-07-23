# Ejercicio 8: Calcular el factorial de un número
def numero_factorial(numero):
    """Calcula el factorial de un número entero no negativo
    Args:
        n: Número entero no negativo
    Returns:
        Factorial de n
    """
    if numero == 0:
        return 1
    return numero * numero_factorial(numero - 1)

factorial_num = 5
factorial_result = numero_factorial(factorial_num)

print("El factorial de", factorial_num, "es:", factorial_result)




