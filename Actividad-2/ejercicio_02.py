repetir = "si"

while repetir == "si":
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))

    suma = a + b
    resta = a - b

    print("Suma:", suma)
    print("Resta:", resta)

    if suma > 10:
        print("La suma es mayor que 10")
    else:
        print("La suma no es mayor que 10")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")