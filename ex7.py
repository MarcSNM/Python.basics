def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def mutiplicacion(a, b):
    return a * b
def divsion(a, b):
    return a/b
def eexonciacion(a, b):
    return a ** b
def radicacion(a, b):
    return a ** (1/b)




n1 = float(input("inserta el primer numero: "))
n2 = float(input("inseerta el segundo numero: "))
print("1.  suma")
print("2.  resta")
print("3.  multiplicacion")
print("4.  division")
print("5.  exonciacion")
print("6.  radicacion")
opcion = int(input("ingrese la opcion que desee: "))

if opcion == 1:
    print(n1, "+", n2, "=",suma(n1, n2) )
elif opcion == 2:
    print(n1, "-", n2, "=",resta(n1, n2) )
elif opcion == 3:
    print(n1, "*", n2, "=",mutiplicacion(n1, n2) )
elif opcion == 4:
    print(n1, "/", n2, "=",divsion(n1, n2) )
elif opcion == 5:
    print(n1, "^", n2, "=",eexonciacion(n1, n2) )
elif opcion == 6:
    print(n1, "^ 1/", n2, "=",radicacion(n1, n2) )   
else:
    ValueError
    print ("Introduzca un numero de elecion")