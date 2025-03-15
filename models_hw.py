import uuid


class Book:
    def __init__(self, book_name: str, author_name: str):
        self.book_name = book_name
        self.author_name = author_name
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return f"<Author name: {self.book_name} ,name of book: {self.author_name} - inn: {self.inn}>"


class Library:
    def __init__(self, name_of_library: str):
        self.name_of_library = name_of_library
        self.list_of_books: list[Book] = []

    def add_book(self, book: Book):
        if book not in self.list_of_books:
            self.list_of_books.append(book)

    def delete_book(self, book_inn):
        for book in self.list_of_books:
            if book.inn == book_inn:
                self.list_of_books.remove(book)
                break
