"""
Solicita tres números enteros y muestra cuál es el mayor. Si son iguales, mostrar un mensaje apropiado.
"""

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))

if num_1 == num_2 == num_3:
    print("Los tres números ingresados son iguales....!!!")
elif num_1 >= num_2 and num_1 >= num_3:
    print(f"El numero mayor es: {num_1}")
elif num_2 >= num_1 and num_2 >= num_3:
    print(f"El numero mayor es: {num_2}")
else:
    print(f"El numero mayor es: {num_3}") 