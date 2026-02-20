# Ejercicio 06: inventario básico con clases

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


inventory = [
    Product("Laptop", 5000, 4),
    Product("Monitor", 1200, 6),
    Product("Mouse", 120, 15),
]

for item in inventory:
    print(f"{item.name} | Precio: {item.price} | Stock: {item.stock}")
