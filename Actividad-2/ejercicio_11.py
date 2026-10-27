repetir = "si"

while repetir == "si":
    temperatura = float(input("Temperatura en °C: "))

    if temperatura < 10:
        print("Frío")
    elif temperatura < 25:
        print("Templado")
    elif temperatura < 35:
        print("Caluroso")
    else:
        print("Muy caluroso")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")