from library import Library

lib = Library()

while True:
    print("\n==========Library Management==========")
    print("1. Add Book")
    print("2. View Book")
    print("3. update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice:")

    match choice:
        case "1":
            book_id = int(input("Enter book_id: "))
            title = input("Enter title: ")
            author = input("Enter author: ")

            lib.add_book(book_id, title, author)

        case "2":
            lib.view_books()

        case "3":
            book_id = int(input("enter book id to update:"))
            title = input("Enter new title:")
            author = input("enter author:")

            lib.update_book(book_id, title, author)

        case "4":
            book_id = int(input("Enter book id to delete:"))

            lib.delete_book(book_id)

        case "5":
            print("program exit")
            break

        case _:
            print("Invalid choice:")