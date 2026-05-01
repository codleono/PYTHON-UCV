"""
Solicita una nota de 0 a 20 y clasifica:
        ·	0 a 10 → “Desaprobado”
        ·	11 a 14 → “Aprobado”
        ·	15 a 17 → “Notable”
        ·	18 a 20 → “Excelente”

"""

nota = int(input("Ingrese la Nota: "))

if nota >= 0 and nota <= 10:
    print("Desaprobado")
elif nota >= 11 and nota <= 14:
    print("Aprobado")
elif nota >= 15 and nota <= 17:
    print("Notable")
elif nota >= 18 and nota <= 20:
    print("Excelente")
else:
    print("Nota no valida")