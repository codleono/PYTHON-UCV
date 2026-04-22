"""
Enunciado: Ingresar un número entero de 3 cifras y mostrar la multiplicación de sus dígitos.
"""
# entrada
numero = int(input("Ingrese un número de 3 cifras: "))

#proceso
centena = numero // 100
decena = (numero // 10) % 10
unidad = numero % 10

resultado = centena * decena * unidad

# salida
print(f"Digitos separados: {centena}, {decena}, {unidad}")
print(f"La multiplicación de sus digitos es: {resultado}")