def Calcular_incremento(sueldo, x):
    nuevo_sueldo = Salario_actual + (Salario_actual * (x/100))
    return nuevo_sueldo





Salario_actual = float(input("Ingrese su sueldo:  "))
Incremento = float(input("Ingrese el incremento de sueldo:  "))
nuevo_salario = Calcular_incremento(Salario_actual, Incremento)

print(("el nuevo salrio del trabajador es:", nuevo_salario))




