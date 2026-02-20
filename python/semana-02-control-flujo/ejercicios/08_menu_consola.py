# Ejercicio 08: menú simple de consola

opcion = ""

while opcion != "3":
    print("1. Ver saludo")
    print("2. Ver fecha fija")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Hola, bienvenido")
    elif opcion == "2":
        print("Fecha de ejemplo: 2026-02-20")
    elif opcion == "3":
        print("Saliendo...")
    else:
        print("Opción no válida")
