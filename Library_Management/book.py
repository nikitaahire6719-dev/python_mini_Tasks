class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        
    def display(self):
        print(f"id: {self.book_id} | Title: {self.title} | author: {self.author}")
