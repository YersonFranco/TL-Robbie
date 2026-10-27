repetir = "si"

while repetir == "si":
    numero = int(input("Número entero: "))

    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")