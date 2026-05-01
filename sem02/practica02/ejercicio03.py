"""
Lee una nota de un alumno (0 a 20).

    · Si es mayor o igual a 11 → "Aprobado"
    · Si es menor a 11 → "Desaprobado"

"""
nota = float(input("Ingresa tu nota: "))

if nota >= 11:
    print("Estas aprobado")
elif nota < 11:
    print("Estas desaprobado")
else:
    print("nota no valida")