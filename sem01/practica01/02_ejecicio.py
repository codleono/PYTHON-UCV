"""
Enunciado: Un empleado recibe un aumento del 15% sobre su sueldo fijo. Calcular el monto del aumento.
    entrada: sueldo fijo
    proceso: sueldo fijo + 0.15
    salida: aumento, sueldo final
"""

#entrada
sueldo_fijo = float(input("Ingrese su sueldo actual: "))

#proceso
aumento = sueldo_fijo * 0.15
sueldo_final = sueldo_fijo + aumento

# salida
print(f"Tu aumento es: S/. {aumento:.2f}")
print(f"Tu sueldo final es: S/. {sueldo_final:.2f}")