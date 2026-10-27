repetir = "si"

while repetir == "si":
    print("--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))

        if opcion == "1":
            print("Resultado:", a + b)
        elif opcion == "2":
            print("Resultado:", a - b)
        elif opcion == "3":
            print("Resultado:", a * b)
        else:
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("No se puede dividir entre cero")
    else:
        print("Opción inválida")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")