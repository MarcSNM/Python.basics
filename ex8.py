#Programa para covertir una unidad en dias, horas, minuts, segundos.
def calcular_segundos(d, h , m, s):
    segundos_totales = 0
    segundos_totales += s
    segundos_totales += m * 60
    segundos_totales += h * 60 * 60
    segundos_totales += d * 24 * 60 * 60
    return segundos_totales



dias = int(input("Intruzca los dias:  "))
horas = int(input("Intruzca las horas:  "))
minutos = int(input("Intruzca los minutos:  "))
segundos = int(input("Intruzca los segundos:  "))

segundos_total = calcular_segundos(dias, horas, minutos ,segundos)
print("la cantidad de segundos en el tiempo ingresado es de:  ", segundos_total)
