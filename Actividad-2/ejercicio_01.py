repetir = "si"

while repetir == "si":
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    print("Nombre:", nombre)

    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")