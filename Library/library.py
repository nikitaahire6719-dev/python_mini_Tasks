from book import Book

class Library:
    def __init__ (self):
        self.books = []

    def add_book(self, book_id, title, author):
        for b in self.books:
            if b.book_id == book_id:
                print("Book is already exists")
                return
        
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print("Book added successfully")

    def view_books(self):
        if not self.books:
            print("no books available")
            return
        
        print("=====book list=====")
        for b in self.books:
            b.display()

    def update_book(self, book_id, new_title, new_author):
        for b in self.books:
            if b.book_id == book_id:
                b.title = new_title
                b.author = new_author
                print("Book updated successfully")
                return
            
        print("book not found")

    def delete_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                self.books.remove(b)
                print("Book deleted successfully")
                return
        print("book not found")
