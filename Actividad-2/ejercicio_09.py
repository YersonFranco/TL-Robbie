repetir = "si"

while repetir == "si":
    precio = int(input("Precio de la compra: "))

    if precio >= 200000:
        descuento = 20
    elif precio >= 100000:
        descuento = 10
    else:
        descuento = 0

    valor_descuento = precio * descuento // 100
    total = precio - valor_descuento

    print("Descuento:", descuento, "%")
    print("Valor del descuento: $", valor_descuento)
    print("Total a pagar: $", total)

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")