#Ejercicio numero 3

import random

n = int(input("Ingrese cuantos numeros aleatorios desea obtener: "))

aleatorios = [random.randint(0,1000) for _ in range(n)]
print(f"Los numeros aleatorios son: {aleatorios}")