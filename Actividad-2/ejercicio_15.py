repetir = "si"

while repetir == "si":
    cliente = input("Nombre del cliente: ")
    producto = input("Producto: ")
    precio = int(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))

    if precio <= 0 or cantidad <= 0:
        print("El precio y la cantidad deben ser mayores que cero")
    else:
        subtotal = precio * cantidad

        if subtotal >= 500000:
            porcentaje = 15
        elif subtotal >= 200000:
            porcentaje = 10
        else:
            porcentaje = 0

        descuento = subtotal * porcentaje // 100
        total = subtotal - descuento

        print("")
        print("====== FACTURA ======")
        print("Cliente:", cliente)
        print("Producto:", producto)
        print("Precio unitario: $", precio)
        print("Cantidad:", cantidad)
        print("---------------------")
        print("Subtotal: $", subtotal)
        print("Descuento (", porcentaje, "%): $", descuento)
        print("Total a pagar: $", total)
        print("=====================")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")