#Ejercicio numero 8

numero = []

rango = int(input("Ingrese la cantidad de numeros que quiera ingresar: "))

for i in range (rango):
    lista=int(input("Ingrese un numero: "))
    numero.append(lista)

numeros.reverse()

print(f"La lista invertida es: {numero}")
