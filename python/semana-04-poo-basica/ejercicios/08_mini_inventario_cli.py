# Ejercicio 08: mini inventario CLI

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


inventory = {
    "teclado": Product("teclado", 5),
    "mouse": Product("mouse", 8),
}

option = ""

while option != "3":
    print("\n1) Ver inventario")
    print("2) Registrar salida")
    print("3) Salir")
    option = input("Opción: ")

    if option == "1":
        for key, product in inventory.items():
            print(f"{key}: {product.stock}")
    elif option == "2":
        name = input("Producto: ").lower()
        if name in inventory and inventory[name].stock > 0:
            inventory[name].stock -= 1
            print("Salida registrada")
        else:
            print("Producto no disponible")
    elif option == "3":
        print("Cerrando inventario...")
    else:
        print("Opción inválida")
