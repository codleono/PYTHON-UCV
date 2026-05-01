"""
Solicita un número y verifica:
    ·	Si es múltiplo de 3.
    ·	Si es múltiplo de 5.
    ·	Si es múltiplo de ambos.
    ·	Si no es múltiplo de ninguno.
"""

numero = int(input("Ingrese un numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Es multiplo de 3 y de 5")
elif numero % 3 == 0:
    print("Es multiplo de 3")
elif numero % 5 == 0:
    print("Es multiplo de 5")
else:
    print("El numero no es multiplo de 3 ni de 5")