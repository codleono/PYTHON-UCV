"""
Enunciado: Una empresa de juguetes realiza una donación solidaria para Navidad. 
Deciden repartir los juguetes entre cuatro distritos de la siguiente manera:
    •	Carabayllo: 35%
    •	Ventanilla: 30%
    •	San Martín: 25%
    •	Comas: lo que quede
Objetivo: El programa debe calcular cuántos juguetes le corresponde a cada distrito en base al total donado.

"""

# entrada
Cant_total = int(input("Ingrese el total de juguetes donados: "))

# proceso
carabayllo = Cant_total * 0.35
ventanilla = Cant_total * 0.30
san_martin = Cant_total * 0.25
comas = Cant_total - (carabayllo + ventanilla + san_martin)

# salida
print(f"Al distrito de Carabayllo le corresponde: {carabayllo} juguetes.")
print(f"Al distrito de Ventanilla le corresponde: {ventanilla} juguetes.")
print(f"Al distrito de San Martin le corresponde: {san_martin} juguetes.")
print(f"Al distrito de Comas le corresponde: {comas} juguetes.")