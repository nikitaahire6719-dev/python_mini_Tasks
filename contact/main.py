from contact_book import ContactBook

book = ContactBook()

while True:
    print("\n==== Contact Book ====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delet Contact")
    print("5. Exit")

    choice = input("Enter your choice:")

    match choice:
        case "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter E-mail: ")

            book.add_contact(name, phone, email)

        case "2":
            book.view_contacts()

        case "3":
            phone = input("Enter phone number to update: ")
            new_name = input("Enter new_name: ")
            new_email = input("Enter new_E-mail: ")
            book.update_contact(phone, new_name, new_email)

        case "4":
            phone = input("Enter phone number to delete: ")
            book.delete_contact(phone)

        case "5":
            print("Exiting contact Book")

        case _:
            print("Invalid contact. Try Again")