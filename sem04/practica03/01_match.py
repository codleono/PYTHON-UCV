#condicionales
#if-> rangos y comparaciones
#match-> clases, tipos, niveles





"""
Una aerolínea tiene descuestos por cantidad de pasajes:
los precios de los destinos son:
1 → Cusco → 325.72
2 → Iquitos → 413.40
3 → Trujillo → 210.00

El cliente elige el destino con un número y la cantidad de pasajes que desea.

Si compra 5 pasajes o más, recibe un 10% de descuento sobre el total.
En caso contrario, paga el precio normal.
Se pide:

Mostrar el destino elegido.
Mostrar el precio unitario.
mostrar el descuento indicado.
Mostrar el monto final a pagar.

"""
opc_destino = int(input("DESTINOS:\n1.Cuzco (S/.325.72)\n2.Iquitos\n3.Trujillo\nElegir una opción: "))
cant_pasajes = int(input("Ingrese cantidad de pasajes al mismo destino: "))

match opc_destino:
    case 1:
        nom_destino = "Cuzco"
        precio = 325.72
    case 2:
        nom_destino = "Iquitos"
        precio = 413.40
    case 3:
        nom_destino = "Trujillo"
        precio = 210.00
    case _:
        print("Destino no disponible")
        precio = None

# validación temprana (mejor práctica)
if precio is None or cant_pasajes <= 0:
    print("Datos inválidos")
else:
    total = precio * cant_pasajes
    descuento = total * 0.10 if cant_pasajes >= 5 else 0
    monto_final = total - descuento

    print(f"\nDestino elegido: {nom_destino}")
    print(f"Precio unitario: S/. {precio:.2f}")
    print(f"Descuento aplicado: S/. {descuento:.2f}")
    print(f"Monto final: S/. {monto_final:.2f}")