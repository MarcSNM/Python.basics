def comprobar_contraseña():
    largo = False
    Mayus = False
    Num = False
    if len(Contraseña) > 8:
        largo = True
    for i in range(len(Contraseña)):
        if Contraseña[i].isupper():
            Mayus = True
        if Contraseña[i].isnumeric():
            Num = True
    
    if largo and Mayus and Num:
        return True
    else:
        return False

Contraseña = input("Introduce tu contraseña:  ")
verificacion = comprobar_contraseña(Contraseña)

if verificacion:
    print("Es una contraseña segura.")
else:
    print("La contraseña no es segura, revisa los pasoa seguir")