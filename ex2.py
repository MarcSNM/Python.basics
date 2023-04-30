def calcularIVA(y):
    IVA = y * 0.19
    return IVA

precio_compra = float (input("ingrese el improte de su compra"))

iva = calcularIVA(precio_compra)
print("el valor de la compra sin iva es: ", precio_compra)
print("el valor total de la compra (CON IVA INCLUIDO) es ", precio_compra + iva)