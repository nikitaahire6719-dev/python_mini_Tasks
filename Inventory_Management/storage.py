FILENAME = "inventory.txt"

def load_products():
    products = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                pid, name, qty, price = line.strip().split(",")
                products.append([pid, name, int(qty), float(price)])
    except FileNotFoundError:
        pass
    return products


def save_products(products):
    with open(FILENAME, "w") as file:
        for p in products:
            file.write(f"{p[0]},{p[1]},{p[2]},{p[3]}\n")
