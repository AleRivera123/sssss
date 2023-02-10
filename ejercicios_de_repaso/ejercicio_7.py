#Ejercicio numero 7

numeros = []

rango = int(input("Ingrese la cantidad de numeros que quiera ingresar: "))

for i in range (rango):
    lista=int(input("Ingrese un numero: "))
    numero.append(lista)

mayor = numero[0]
for x in range (rango):
    if numero[x]>mayor:
        mayor = numero [x]

menor = numero[0]
for x in range (rango):
    if numero[x]<menor:
        menor=numero[x]
        posicion=x

print(f"El numero mayor de la lista es: {mayor}")
print(f"El numero menor de la lista es: {menor}")

