class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.product_id},{self.name},{self.quantity},{self.price}"
