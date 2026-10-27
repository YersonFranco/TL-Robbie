usuario_correcto = "franco"
clave_correcta = "1234"

repetir = "si"

while repetir == "si":
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso permitido")
    else:
        print("Acceso denegado: usuario o contraseña incorrectos")

    repetir = input("¿Continuar? si/no: ")

print("Adiós!")