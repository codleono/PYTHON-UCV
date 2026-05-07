"""
ingresa una medida KM y convertirla en:
metros, centimetros, milimetros
considerando que 
1 km es = 1000 m
1 m = 100 cm
1 cm = 10mm
salida: m, cm, mm
entrada: km
proceso: m = km * 1000
        cm = m * 100
        mm = cm * 10
"""
km = float(input("Ingrese el valor en KM: "))

#proceso
m = km * 1000
cm = m * 100
mm = cm * 10

print(f"el valor en metros es: {m} m.")
print(f"el valor en Centrimetro es: {cm} cm.")
print(f"el valor en Milimetros es: {mm} mm.")