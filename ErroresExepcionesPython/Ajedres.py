import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def square_color(number, letter):
    """
    Devuelve el color de la casilla correspondiente en un tablero de ajedrez.

    Args:
        number: Número entero (1-8)
        letter: Letra (a-h)

    Returns:
        color: String ("blanco" o "negro")
    """
    # Verificar que el tipo de dato de los parámetros sea el adecuado
    if not isinstance(number, int):
        return "El número debe ser un entero."
    if not isinstance(letter, str):
        return "La letra debe ser un string."

    # Verificar que el número esté en el rango de valores permitidos
    if number < 1 or number > 8:
        return "El número debe estar entre 1 y 8."

    # Verificar que la letra sea una sola letra y esté en el conjunto permitido
    if len(letter) != 1:
        return "La letra debe ser un solo caracter."
    if letter not in "abcdefgh":
        return "La letra debe estar entre 'a' y 'h'."

    # Determinar el color de la casilla
    letter_index = ord(letter) - ord('a') + 1
    if (number + letter_index) % 2 == 0:
        return "blanco"
    else:
        return "negro"

# Crear el tablero de ajedrez
def create_chessboard():
    board = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            if square_color(i + 1, chr(j + ord('a'))) == "negro":
                board[i, j] = 1

    plt.figure(figsize=(8, 8))
    sns.heatmap(board, cmap="binary", cbar=False, linewidths=0.5, linecolor='black')
    plt.xticks(np.arange(8) + 0.5, list('abcdefgh'))
    plt.yticks(np.arange(8) + 0.5, np.arange(1, 9))
    plt.gca().invert_yaxis()
    plt.show()

# Ejemplo de uso
create_chessboard()
