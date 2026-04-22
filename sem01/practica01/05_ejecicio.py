"""
Enunciado: Una tienda ofrece 25% de descuento en casacas.
Calcular el descuento y el monto final a pagar.
    entrada: precio_casaca
    proceso: descuento = precio_casaca * 0.25  
             precio_final = precio_casaca - descuento
    salida: precio_final
"""
# entrada
precio_casaca = float(input("Ingrese el precio de la casaca: "))

# proceso
descuento = precio_casaca * 0.25
precio_final = precio_casaca - descuento

# salida
print(f"Tu descuento del 25% equivale a: S/. {descuento:.2f}")
print(f"Precio Final a pagar: S/. {precio_final:.2f}")

