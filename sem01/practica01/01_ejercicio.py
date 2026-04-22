"""
Leer la medida de una pared en metros y convertirla a centímetros.
        salida: centimetros
        entrada: metros
        proceso: centimetros = (metros * 100)
"""

#entrada
metros = float(input("ingresa la medida de la pared en Metros: "))

#proceso
centimetros = (metros * 100)

#salida
print(f"La medida de la pared en centimetros es: {centimetros}")
