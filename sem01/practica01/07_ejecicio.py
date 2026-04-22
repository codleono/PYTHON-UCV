"""
Enunciado: Ingresar la capacidad de un disco duro en gigabytes (GB) y convertirla a:
    •	Megabytes (MB)
    •	Kilobytes (KB)
    •	Bytes (B)
Usar:
    •	1 GB = 1024 MB
    •	1 MB = 1024 KB
    •	1 KB = 1024 B
"""

# entrada
gb = float(input("Ingrese la capacidad del disco duro en GB: "))

# proceso
mb = gb * 1024
kb = mb * 1024
bytes = kb * 1024

# salida
print(f"En Megabytes equivalen a: {mb:.2f} MB")
print(f"En Kilobytes equivalen a: {kb:.2f} KB")
print(f"En Bytes equivalen a: {bytes:.2f} BAYTES")
