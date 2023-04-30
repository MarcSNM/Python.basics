def notafinal(n1, n2, n3):
    return (t1 * 0.3) + (t2 * 0.3) + (t3 * 0.4)
print("Cual es su nombre?")
Estudiante = input("")
t1 = float(input("Ingrese la nota:  "))
t2 = float(input("Ingrese la nota:  "))
t3 = float(input("Ingrese la nota:  "))

nota_final = notafinal(t1, t2, t3)
print("La nota final del estudiante", Estudiante, "es: ",round(nota_final), 2)
