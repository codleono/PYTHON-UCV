"""
Enunciado:
Una tienda vende camisetas:
1 → Small → 35.00
2 → Medium → 40.00
3 → Large → 45.00

El cliente elige la talla (número), la cantidad de camisetas y la forma de pago.

Si compra 10 camisetas o más, recibe 20% de descuento.
Si paga con tarjeta, hay un recargo del 5%.
Si paga en efectivo, no hay recargo.
Se pide:

Mostrar la talla elegida y el precio unitario.
Mostrar si se aplicó descuento por cantidad.
Mostrar si hubo recargo por forma de pago.
Mostrar el monto final a pagar.

"""

# entrada
opcion = int(input("CAMISETAS DISPONIBLES\n1. Small -> S/.35.00\n2. Medium -> S/.40.00\n3. Large -> S/.45.00\nSeleccione una talla: "))
cantidad = int(input("Ingrese cantidad de camisetas: "))
pago = input("Forma de pago (efectivo/tarjeta): ").lower()

# selección de talla
match opcion:
    case 1:
        talla = "Small"
        precio = 35.00

    case 2:
        talla = "Medium"
        precio = 40.00

    case 3:
        talla = "Large"
        precio = 45.00

    case _:
        print("Talla no válida")
        precio = None

# validación
if precio is None or cantidad <= 0:
    print("Datos inválidos")

else:

    # total base
    total = precio * cantidad

    # valores iniciales
    descuento = 0
    recargo = 0

    mensaje_descuento = "Descuento no aplicado"
    mensaje_recargo = "Recargo no aplicado"

    # descuento por cantidad
    if cantidad >= 10:
        descuento = total * 0.20
        total -= descuento
        mensaje_descuento = "Se aplicó descuento"

    # recargo por tarjeta
    if pago == "tarjeta":
        recargo = total * 0.05
        total += recargo
        mensaje_recargo = "Se aplicó recargo"

    # salida
    print("="*30)
    print(f"Talla elegida: {talla}")
    print(f"Precio unitario: S/. {precio:.2f}")

    print(f"\n{mensaje_descuento}")
    print(f"Descuento aplicado: S/. {descuento:.2f}")

    print(f"\n{mensaje_recargo}")
    print(f"Recargo aplicado: S/. {recargo:.2f}")

    print(f"\nMonto final a pagar: S/. {total:.2f}")