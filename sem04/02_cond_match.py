"""
Una aerolínea tiene descuentos por cantidad de pasajes:
Los precios de los destinos son:
1. Cuzco > 325.72
2. Iquitos -> 413.40
3. Trujillo -> 210.00
El cliente elige el destino con un número y la cantidad de pasajes que desea.
Si compra 5 pasajes o más, recibe un 10% de descuento sobre el total.
En caso contrario, paga el precio normal.
Se solicita:
Mostrar el destino elegido.
Mostrar el precio unitario.
Mostrar el descuento aplicado.
Mostrar el monto final a pagar.
"""

# entrada
print("Destinos disponibles:")
print("1. Cuzco")
print("2. Iquitos")
print("3. Trujillo")

opcion = int(input("Seleccione destino (1-3): "))
cantidad = int(input("Ingrese la cantidad de pasajes: "))

# proceso: selección con match
match opcion:
    case 1:
        destino = "Cuzco"
        precio = 325.72
    case 2:
        destino = "Iquitos"
        precio = 413.40
    case 3:
        destino = "Trujillo"
        precio = 210.00
    case _:
        print("Destino no válido")
        exit()

# cálculo
total = precio * cantidad

# descuento
descuento = total * 0.10 if cantidad >= 5 else 0
monto_final = total - descuento

# salida
print(f"Destino: {destino}")
print(f"Precio unitario: S/. {precio:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {monto_final:.2f}")