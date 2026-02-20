# Ejercicio 03: clase Product

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Teclado", 25.5)
print("Producto:", product.name)
print("Precio:", product.price)
