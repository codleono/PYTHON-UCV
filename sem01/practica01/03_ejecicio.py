"""
Enunciado: Un auto cuesta un precio inicial. Calcular el 18% de impuesto y el precio final.
    entrada: precio_inicial
    proceso: 
             impuesto = precio_inicial * 0.18
             precio_final = precio_inicial  + impuesto
    salida: precio final
"""
#entrada
precio_inicial = float(input("Ingrese el valor Inicial del auto: "))

#proceso
impuesto = precio_inicial * 0.18
precio_final = precio_inicial  + impuesto

#salida
print(f"El Impuesto es: S/. {impuesto:.2f}")
print(f"El precio final es: S/. {precio_final:.2f}")