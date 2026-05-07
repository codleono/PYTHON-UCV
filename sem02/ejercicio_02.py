"""
Un empleado recibe un aumento del 15% sobre su sueldo fijo.
calcular el monto del aumento y el sueldo final.
    ENTRADA: sueldo_fijo
    PROCESO: sueldo_fijo * 0.15
    SALIDA:aumento y sueldo final

"""
#desarrollo

sueldo_fijo = float(input("Ingrese su sueldo fijo: "))
aumento = (sueldo_fijo * 0.15)
sueldo_final = sueldo_fijo + aumento

print(f"El aumento es: S/.{aumento} y el sueldo final es: S/.{sueldo_final}")