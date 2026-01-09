from inventory import Inventory

inv = Inventory()

while True:
    print("\n--- Inventory Management ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            pid = input("Product ID: ")
            name = input("Name: ")
            qty = int(input("Quantity: "))
            price = float(input("Price: "))
            inv.add_product(pid, name, qty, price)

        case "2":
            inv.view_products()

        case "3":
            pid = input("Product ID: ")
            qty = int(input("New Quantity: "))
            price = float(input("New Price: "))
            inv.update_product(pid, qty, price)

        case "4":
            pid = input("Product ID: ")
            inv.delete_product(pid)

        case "5":
            print("Exiting...")
            break

        case _:
            print("Invalid choice")
