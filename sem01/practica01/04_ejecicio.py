"""
Enunciado: Convertir una cantidad en soles a dólares. Tipo de cambio: 1 dólar = 3.8 soles
    entrada: cantidad_soles
    proceso: cant_dolares = cantidad_soles / 3.8  
    salida: cant_dolares
"""

# entrada
cantidad_soles = float(input("Ingrese la cantidad en soles: "))

# proceso
cant_dolares = cantidad_soles / 3.8

# salida
print(f"Equivale a: $ {cant_dolares:.2f}")

