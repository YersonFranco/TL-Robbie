repetir = "si"

while repetir == "si":
    numero = int(input("Número: "))

    if numero > 0:
        print("Es positivo")
    elif numero < 0:
        print("Es negativo")
    else:
        print("Es cero")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")