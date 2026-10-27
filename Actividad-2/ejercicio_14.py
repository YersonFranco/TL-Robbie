saldo = 500000
repetir = "si"

while repetir == "si":
    print("--- CAJERO ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("Saldo actual: $", saldo)
    elif opcion == "2":
        retiro = int(input("Valor a retirar: "))
        if retiro <= 0:
            print("El valor debe ser mayor que cero")
        elif retiro > saldo:
            print("Fondos insuficientes")
        else:
            saldo = saldo - retiro
            print("Retiro exitoso. Nuevo saldo: $", saldo)
    elif opcion == "3":
        deposito = int(input("Valor a depositar: "))
        if deposito <= 0:
            print("El valor debe ser mayor que cero")
        else:
            saldo = saldo + deposito
            print("Depósito exitoso. Nuevo saldo: $", saldo)
    elif opcion == "4":
        repetir = "no"
    else:
        print("Opción inválida")

print("Gracias por usar el cajero. ¡Adiós!")