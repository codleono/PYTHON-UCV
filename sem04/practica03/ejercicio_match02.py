"""
Enunciado:
Un restaurante vende:
    1 → Pollo a la brasa → 25.00
    2 → Ceviche → 30.00
    3 → Lomo saltado → 28.00

El cliente elige un plato (número) y la cantidad.

Si compra más de 3 pollos a la brasa, se descuenta 1 pollo gratis.
Si compra más de 5 platos (cualquiera), se aplica un 5% de descuento adicional.
Se pide:

Mostrar el plato elegido.
Mostrar el precio unitario.
Indicar si se aplicó alguna promoción (pollo gratis o descuento).
Mostrar el monto final a pagar.

"""
opcion = int(input("Platos disponibles: \n1.Pollo a la Brasa (S/.25.00)\n2.Ceviche (S/.30.00)\n3.Lomo saltado (S/.28.00)\nElegir una opción: "))
cantidad = int(input("Ingrese la Cantidad de Platos: "))

match opcion:
    case 1:
        plato = "Pollo a la Brasa"
        precio = 25.00
    case 2:
        plato = "Ceviche"
        precio = 30.00
    case 3:
        plato = "Lomo saltado"
        precio = 28.00
    case _:
        print("Plato no disponible")
        precio = None

if precio is None or cantidad <= 0:
    print("Datos Invalidos")
else:
     # promoción pollo gratis
    if opcion == 1 and cantidad > 3:
        total = (cantidad - 1) * precio
        promo = "Se aplicó promoción: 1 pollo gratis"
    else:
        total = cantidad * precio
        promo = "No se aplicó promoción de pollo"

    # descuento adicional
    if cantidad > 5:
        descuento = total * 0.05
        total -= descuento
        promo += " + descuento del 5%"
    else:
        descuento = 0

    # salida
print("="*30)
print(f"\nPlato elegido: {plato}")
print(f"Precio unitario: S/. {precio:.2f}")
print(f"{promo}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"Monto final: S/. {total:.2f}")