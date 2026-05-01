"""
Pide la distancia en km y calcula el costo:
    ·   Si es hasta 5 km → S/ 10
    ·   De 6 a 15 km → S/ 20
    ·   Más de 15 km → S/ 30
"""

distancia = float(input("Ingrese la distancia en km: "))

if distancia <= 5:
    costo = 10
elif 6 <= distancia <= 15:
    costo = 20
else:
    costo = 30

print(f"Distancia recorrida: {distancia} km")
print(f"Costo: S/. {costo:.2f}")