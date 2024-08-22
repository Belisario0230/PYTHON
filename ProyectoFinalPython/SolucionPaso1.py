import csv

class Pawns:
    def __init__(self):
        self.letters = []

    def addPawn(self, c):
        self.letters.append(c)

    def addPawns(self, c, n):
        for _ in range(n):
            self.addPawn(c)

    def createBag(self):
        with open('D:/Documents/CURSOS1/PYTHON/ProyectoFinalPython/bag_of_pawns-220320-111432.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la fila de encabezado
            for row in reader:
                self.addPawns(row[0], int(row[1]))

    def showPawns(self):
        pawn_counts = {}
        for pawn in self.letters:
            if pawn in pawn_counts:
                pawn_counts[pawn] += 1
            else:
                pawn_counts[pawn] = 1
        for pawn, count in pawn_counts.items():
            print(f"Ficha {pawn}: {count}")