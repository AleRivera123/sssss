#Ejercicio numero 14

numero = []

rango = int(input("Ingrese la cantidad de numeros que quiera ingresar: "))

for i in range (rango):
    lista=int(input("Ingrese un numero: "))
    numero.append(lista)


print("El factorial de los numeros es: ")
print(sum(numero)/len(numero))