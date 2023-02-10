#Ejercicio numero 9

from random import randint

def llenar_matriz(n):
    matriz = []

    for i in range(n):
        fila = []

        for c in range(n):
            fila.append(randint(1, 100))

        matriz.append(fila)

    return matriz

final = llenar_matriz(5)

print(final)