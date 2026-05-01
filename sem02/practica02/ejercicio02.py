"""
Pide la edad de una persona e indica si es mayor de edad (18 años o más) o menor de edad.
"""

edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad < 18:
    print("Eres menor de edad")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Edad no valida, ingresa un numero entero positivo")