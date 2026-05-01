"""
Una empresa cobra la luz de la siguiente manera:
    ·        Si el consumo es menor a 100 kWh → 0.80 soles por kWh
    ·        Si el consumo es entre 100 y 200 kWh → 1.00 sol por kWh
    ·        Si el consumo es mayor a 200 kWh → 1.20 soles por kWh
Pide el consumo y calcula el monto a pagar.
"""

consumo = float(input("Ingrese el consumo en kWh: "))

if consumo < 100:
    tarifa = 0.80
elif 100 <= consumo <= 200:
    tarifa = 1.00
else:
    tarifa = 1.20

monto = consumo * tarifa

print(f"su Consumo fue: {consumo} kWh")
print(f"La tarifa aplicada es: S/. {tarifa} por kWh")
print(f"Monto total a pagar: S/. {monto:.2f}")