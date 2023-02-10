#Ejercicio numero 4

numero=int(input("Ingrese el numero que desea evaluar: "))

if numero % 2==0:
    print(f"{numero} s par.")
elif numero % 2==1:
    print(f"{numero} es impar.")
else:
    print(f"el calculo es errado y {numero} no es un numero valido.")