"""
Enunciado:
Un cine ofrece:
1 → 2D → 15.00
2 → 3D → 22.00
3 → VIP → 35.00

El cliente elige la sala (número), el día de la función y la cantidad de entradas.

Si la función es sábado o domingo, hay un recargo del 20%.
Si compra más de 4 entradas, recibe un 15% de descuento.
Se pide:

Mostrar la sala elegida y su precio base.
Mostrar si se aplicó recargo por fin de semana.
Mostrar si se aplicó descuento por cantidad.
Mostrar el monto final a pagar.

"""

opcion = int(input("Salas disponibles: \n1. 2D -> S/.15.00\n2. 3D -> S/.22.00\n3. VIP -> S/.35.00\nElegir una opción: "))
dia = input("Ingrese el dia de la funcion: ").lower() #cambia de mayuscula a minuscula
cantidad = int(input("Ingrese cantidad de entradas: "))


match opcion:
    case 1:
        sala = "2D"
        precio = 15.00

    case 2:
        sala = "3D"
        precio = 22.00

    case 3:
        sala = "VIP"
        precio = 35.00

    case _:
        print("Sala no válida")
        precio = None


if precio is None or cantidad <= 0:
    print("Datos inválidos")

else:

    # total base
    total = precio * cantidad

    # valores iniciales
    recargo = 0
    descuento = 0

    # recargo por fin de semana
    if dia == "sabado" or dia == "domingo":
        recargo = total * 0.20
        total += recargo
        mensaje_recargo = "Sí se aplicó recargo"
    else:
        mensaje_recargo = "No se aplicó recargo"

    # descuento por cantidad
    if cantidad > 4:
        descuento = total * 0.15
        total -= descuento
        mensaje_descuento = "Sí se aplicó descuento"
    else:
        mensaje_descuento = "No se aplicó descuento"

print("="*30)
print(f"Sala elegida: {sala}")
print(f"Precio base: S/. {precio:.2f}")

print(f"\n{mensaje_recargo}")
print(f"Recargo aplicado: S/. {recargo:.2f}")

print(f"\n{mensaje_descuento}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"\nMonto final a pagar: S/. {total:.2f}")