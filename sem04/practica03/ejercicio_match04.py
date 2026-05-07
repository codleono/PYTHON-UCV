"""
Enunciado:
Un gimnasio ofrece:
1 → Plan mensual → 120.00
2 → Plan trimestral → 300.00
3 → Plan anual → 1000.00

El cliente elige el plan y se ingresa su edad.

Si tiene menos de 18 años, recibe 20% de descuento.
Si tiene más de 60 años, recibe 30% de descuento.
Caso contrario, paga tarifa normal.
Se pide:

Mostrar el plan elegido.
Mostrar el precio base.
Indicar si se aplicó un descuento y de cuánto.
Mostrar el monto final a pagar.

"""


opcion = int(input("Planes disponibles: \n1. Plan mensual -> S/.120.00\n2. Plan trimestral -> S/.300.00\n3. Plan anual -> S/.1000.00\nElegir Plan: "))
edad = int(input("Ingrese su edad: "))

# selección del plan
match opcion:
    case 1:
        plan = "Plan mensual"
        precio = 120.00

    case 2:
        plan = "Plan trimestral"
        precio = 300.00

    case 3:
        plan = "Plan anual"
        precio = 1000.00

    case _:
        print("Plan no válido")
        precio = None

# validación
if precio is None or edad <= 0:
    print("Datos inválidos")

else:

    # valores iniciales
    descuento = 0
    mensaje = "No se aplicó descuento"

    # descuento por edad
    if edad < 18:
        descuento = precio * 0.20
        mensaje = "Se aplicó descuento del 20%"

    elif edad > 60:
        descuento = precio * 0.30
        mensaje = "Se aplicó descuento del 30%"

    # total final
    total = precio - descuento

    # salida
print("="*30)
print(f"Plan elegido: {plan}")
print(f"Precio base: S/. {precio:.2f}")
print(f"\n{mensaje}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"\nMonto final a pagar: S/. {total:.2f}")