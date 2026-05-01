"""
Pide peso (kg) y estatura (m). 
Calcula el IMC = peso / (estatura**2) 
clasifica:
    ·        Bajo peso: IMC < 18.5
    ·        Normal: 18.5 a 24.9
    ·        Sobrepeso: 25 a 29.9
    ·        Obesidad: ≥ 30

"""


peso = float(input("Ingrese su peso  en Kg: "))
estatura = float(input("Ingrese su estatura en Metros: "))

imc = peso / (estatura ** 2)

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"IMC: {imc:.2f}")
print(f"Su categoria es: {categoria}")

