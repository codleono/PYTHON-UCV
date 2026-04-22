"""
Enunciado: Ingresar el radio de un círculo y calcular su área.
Fórmula: Area = pi * r²
Considerar: pi = 3.1416

"""

# entrada
radio = float(input("Ingrese el radio del círculo: "))

# proceso
PI = 3.1416
area = PI * radio**2

# salida
print(f"Area del circulo: {area:.2f}")