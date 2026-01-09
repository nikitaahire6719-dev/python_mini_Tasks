from product import Product
from storage import load_products, save_products

class Inventory:
    def __init__(self):
        self.products = load_products()

    def add_product(self, product_id, name, quantity, price):
        for p in self.products:
            if p[0] == product_id:
                print("Product already exists")
                return
        self.products.append([product_id, name, quantity, price])
        save_products(self.products)
        print("Product added")

    def view_products(self):
        if not self.products:
            print("No products available")
            return
        for p in self.products:
            print(f"ID:{p[0]} Name:{p[1]} Qty:{p[2]} Price:{p[3]}")

    def update_product(self, product_id, quantity, price):
        for p in self.products:
            if p[0] == product_id:
                p[2] = quantity
                p[3] = price
                save_products(self.products)
                print("Product updated")
                return
        print("Product not found")

    def delete_product(self, product_id):
        for p in self.products:
            if p[0] == product_id:
                self.products.remove(p)
                save_products(self.products)
                print("Product deleted")
                return
        print("Product not found")
