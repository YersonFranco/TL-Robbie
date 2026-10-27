repetir = "si"

while repetir == "si":
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Inválido: los lados deben ser mayores que cero")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("No es un triángulo válido")
    elif a == b and b == c:
        print("Triángulo equilátero")
    elif a == b or a == c or b == c:
        print("Triángulo isósceles")
    else:
        print("Triángulo escaleno")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")