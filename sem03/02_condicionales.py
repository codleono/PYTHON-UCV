"""
solicita el costo del producto. si el costo es mas de 100 soles, aplicar un descuento del 10%
mostrar el costo final y descuento

"""

costo_Inicial = float(input("Ingrese el costo del Producto: "))

if costo_Inicial > 100 :
    descuento = 0.10 * costo_Inicial
else : 
    descuento = 0
costo_final = costo_Inicial - descuento  

print(f"el descuento es: {descuento:.2f}")
print(f"el precio final es: {costo_final}")
