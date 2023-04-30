"""COMPROBAR SI UNA PALABRA O FRASE ES PALINDROMA-
EJEMPLOS:

-> RECONOCER
->Anna
->Ojo rojo
-La ruta nos aporto otro paso natural

tener en cuenta que no se tienen en cuenta ni los espacios ni las mayusculas ni las tildes.
"""

def Palindromo(palabra):
    #La ruta nos aporto otro paso natural
    #Larutanosaportootropasonatural
    palabra = palabra.lower()
    palabra = palabra.replace(" ", " ")
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")


palabra = input("Escribre tu palabra o frase:  ")   
a = 0
b = len(palabra) - 1

for i in range(a , len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False
return True
        
        

if Palindromo(palabra):
    print("es una palabra palindroma")
else:
    print("No es un palindromo")


         