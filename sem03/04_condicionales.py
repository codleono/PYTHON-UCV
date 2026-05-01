"""
solicita la edad de una persona y clasifícala segun los siguientes niveles:
    niño: 0 - 12
    adolecente: 13 - 17 
    adulto: 18 - 59
    adulto mayor. 60 a mas
"""

edad = int(input("Ingrese la edad: "))

if edad >= 0 and edad <= 12:
    print("Eres un Niño")
elif edad >= 13 and edad <= 17:
    print("Eres un Adolecente")
elif edad >= 18 and edad <= 59:
    print("Eres un Adulto")
elif edad >= 60:
    print("Eres un Adulto mayor")
else:
    print("Edad no valida")