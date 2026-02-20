# Ejercicio 07: mini carrito CLI

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total(self):
        return sum(product.price for product in self.products)


catalog = {
    "1": Product("Teclado", 120),
    "2": Product("Mouse", 80),
    "3": Product("USB", 45),
}

cart = Cart()
option = ""

while option != "0":
    print("\n1) Teclado\n2) Mouse\n3) USB\n0) Finalizar")
    option = input("Elige producto: ")

    if option in catalog:
        cart.add_product(catalog[option])
        print("Agregado al carrito")
    elif option == "0":
        print("Finalizando compra...")
    else:
        print("Opción inválida")

print("Total a pagar:", cart.total())
