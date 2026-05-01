"""
solicita edos numeros enteros e identificar cual es mayor
si don iguales, mostrar unmensaje

"""

n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))

if n1 > n2:
    print(f"EL numero mayor es: {n1:.2f}")
elif n2 > n1: 
    print(f"EL numero mayor es: {n2:.2f}") 
else:
    print("Ambos son iguales")

