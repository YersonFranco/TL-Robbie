repetir = "si"

while repetir == "si":
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))

    if a > b:
        print(a, "es mayor que", b)
    elif b > a:
        print(b, "es mayor que", a)
    else:
        print("Los dos números son iguales")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")