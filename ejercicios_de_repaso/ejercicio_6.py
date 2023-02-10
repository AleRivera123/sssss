#Ejercicio numero 6

numero = []

rango = int(input("Ingrese la cantidad de numeros que quiera ingresar: "))

for i in range (rango):
    lista=int(input("Ingrese un numero: "))
    numero.append(lista)

listSum = sum(numero)
print(f"La suma de la lista es: {listSum}")