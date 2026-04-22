"""
Enunciado: Ingresar 3 notas de un alumno y calcular su promedio.
    entrada: n1, n2 , n3
    proceso:  (n1, n2 , n3)/3
    salida: nota_final
"""
# entrada
n1 = float(input("Ingrese la Nota 01: "))
n2 = float(input("Ingrese la Nota 02: "))
n3 = float(input("Ingrese la Nota 03: "))

# proceso
promedio = (n1 + n2 + n3)/3
# salida
print(f"El promedio de las notas es: {promedio:.2f}")