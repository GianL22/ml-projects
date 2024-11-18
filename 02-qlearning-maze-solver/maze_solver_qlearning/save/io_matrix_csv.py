import csv
import numpy as np
import pathlib
def save_matrix_to_csv(matrix, path):
    # Abrir el archivo CSV en modo escritura
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Escribir rows con la matrix
        for row in matrix:
            writer.writerow(row)

def read_matrix_csv(path, dtype=int):
    # Leer el archivo CSV
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Leer filas y convertir a lista de listas
        matrix = [list(map(dtype, row)) for row in reader]

    # Convertir a numpy array
    matrix = np.array(matrix)

    return matrix