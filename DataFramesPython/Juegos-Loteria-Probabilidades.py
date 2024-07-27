import itertools
import random

# Generar todas las combinaciones posibles de 5 números del 1 al 43
combinaciones = list(itertools.combinations(range(1, 44), 5))

# Número ganador (puedes cambiar esto según el sorteo real)
numero_ganador = [3, 7, 15, 22, 40]

# Generar un número aleatorio del 1 al 16
numero_aleatorio_otro_rango = random.randint(1, 16)

# Verificar si alguna combinación coincide con el número ganador
for combinacion in combinaciones:
    if list(combinacion) == numero_ganador:
        print("¡Has acertado! La combinación ganadora es:", combinacion)
        print("Numero aleatorio de 16 numeros:", numero_aleatorio_otro_rango)
        break
else:
    print("No has acertado. Sigue intentándolo.")



import random

# Generar 4 números aleatorios del 1 al 10000
numeros_aleatorios = random.sample(range(1, 10000), 1)

# Signos del zodiaco
signos_zodiaco = [
    "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo",
    "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"
]

# Generar un número aleatorio para seleccionar un signo
indice_signo = random.randint(0, 11)
signo_aleatorio = signos_zodiaco[indice_signo]

# Imprimir los resultados
print("Números aleatorios del 1 al 10000:", numeros_aleatorios)
print("Signo aleatorio del zodiaco:", signo_aleatorio)
