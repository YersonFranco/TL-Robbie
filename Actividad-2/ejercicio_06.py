repetir = "si"

while repetir == "si":
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    op = input("Operación (+, -, *, /): ")

    if op == "+":
        print("Resultado:", a + b)
    elif op == "-":
        print("Resultado:", a - b)
    elif op == "*":
        print("Resultado:", a * b)
    elif op == "/":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("No se puede dividir entre cero")
    else:
        print("Operación inválida")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")