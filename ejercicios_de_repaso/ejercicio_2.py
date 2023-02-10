#Ejercicio numero 2

import math

radio = float(input("Ingrese el radio del circulo: "))

area = math.pi*radio*radio

decimales= round(area, 4)
print(f"El area del circulo es: {decimales}")