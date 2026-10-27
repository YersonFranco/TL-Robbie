repetir = "si"

while repetir == "si":
    nota = int(input("Nota (0 a 100): "))

    if nota < 0 or nota > 100:
        print("Nota inválida: debe estar entre 0 y 100")
    elif nota >= 70:
        print("Aprobado")
    else:
        print("Reprobado")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")