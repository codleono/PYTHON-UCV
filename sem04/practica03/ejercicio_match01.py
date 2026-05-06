"""
Enunciado:
Una aerolínea tiene estos destinos:
1 → Cusco → 325.72
2 → Iquitos → 413.40
3 → Trujillo → 200.00

El cliente elige el destino con un número y la cantidad de pasajes que desea.

Si compra 5 pasajes o más, recibe un 10% de descuento sobre el total.
En caso contrario, paga el precio normal.
Se pide:

Mostrar el destino elegido.
Mostrar el precio unitario.
Indicar si hubo descuento o no.
Mostrar el monto final a pagar.

"""
destino = int(input("SELECCIONAR DESTINO: \n1.Cuzco (S/.325.72)\n2.Iquitos (S/.413.40)\n3.Trujillo (S/.200.00)\nElegir una opción: "))
cant_pasajes = int(input("Ingrese cantidad de pasajes al mismo destino: "))

match destino:
    case 1:
        nom_destino = "Cusco"
        costo = 325.72
    case 2:
        nom_destino = "Iquitos"
        costo = 413.40
    case 3:
        nom_destino = "Trujillo"
        costo = 200.00
    case _:
        print("Selecciona Un Destino Disponible")
        costo = None
if costo is None or cant_pasajes <= 0:
    print("Datos Invalidos")
else:
    total = costo * cant_pasajes
    descuento = total * 0.10 if cant_pasajes >= 5 else 0
    monto_pagar = total - descuento

    print(f"\nDestino elegido: {destino}")
    print(f"Precio unitario: S/. {costo:.2f}")
    print(f"Descuento aplicado: S/. {descuento:.2f}")
    print(f"Monto final: S/. {monto_pagar:.2f}")


