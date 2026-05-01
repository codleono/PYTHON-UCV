"""
Pide tres lados y verifica si forman un triángulo válido con la regla:
La suma de dos lados debe ser mayor al tercer lado. 
(Si no cumple, no es triángulo).
"""

l1 = float(input("Ingrese el lado 1: "))
l2 = float(input("Ingrese el lado 2: "))
l3 = float(input("Ingrese el lado 3: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("los lados SI forman un triangulo valido")
else:
    print("los lados NO forman un triangulo")