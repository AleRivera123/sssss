#Ejercicio numero 10


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);


num = int(input("Ingrese el numero que desea sacar factorial: "))
print("Factorial of", num, "is", factorial(num))