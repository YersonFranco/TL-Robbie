repetir = "si"

while repetir == "si":
    edad = int(input("Edad: "))

    if edad < 0:
        print("Edad inválida: no puede ser negativa")
    elif edad >= 18:
        print("Puede ingresar al evento")
    else:
        print("No puede ingresar: el evento es para mayores de 18 años")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")