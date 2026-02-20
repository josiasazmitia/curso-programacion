# Ejercicio 04: clase Cart con add_product y total

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


cart = Cart()
cart.add_product(Product("Mouse", 15.0))
cart.add_product(Product("Audífonos", 30.0))
print("Total carrito:", cart.total())
