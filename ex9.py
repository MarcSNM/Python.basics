"""programa para calcular el INC
# < 18.5 -> BAJO PESO
# < 18.5 - 24,9 > NORMAL
# < 25.0 - 29.9 > SOBREPESO
# < 30.0 34.9 > OBESIDAD 1
# < 35.0 - 39.9 > OBESIDAD 2
# < 40.0 - 49.9 > OBESIDAD 3
# < 50.0 > OBESIDAD 4

IMC = peso / (estaruta * estatura)
"""


def Calcular_IMC(p, a):
    return p / (a * a)

def Nivel_de_peso(imc):
    if imc < 18.5:
        return "bajo peso"
    elif 18.5 <= imc <= 24.9:
        return "peso normal"
    elif 25 <= imc <= 29.9:
        return "sobrepeso"
    elif 30 <= imc <= 34.9:
        return "OBESIDAD 1"
    elif 35 <= imc <= 39.9:
        return "OBESIDAD 2"
    elif 40 <= imc <= 49.9:
        return "OBESIDAD 3"
    elif imc >= 50.0:
        return "OBESIDAD 4"



Peso = float(input("Introduzca su peso en KG:  "))
Altura = float(input("Introduzca su altura:  "))

print("Su nivel de peso es:  ", Nivel_de_peso(Calcular_IMC(Peso, Altura)))