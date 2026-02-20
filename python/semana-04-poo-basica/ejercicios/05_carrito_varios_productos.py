# Ejercicio 05: carrito con varios productos

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
cart.add_product(Product("Cuaderno", 3.5))
cart.add_product(Product("Lápiz", 1.0))
cart.add_product(Product("Mochila", 22.0))

for p in cart.products:
    print(f"- {p.name}: Q{p.price}")

print("Total:", cart.total())
