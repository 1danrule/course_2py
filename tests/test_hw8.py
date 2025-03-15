class TestLibrary:
    def test_add_book_in_library(self, book, library):
        library.add_book(book)
        assert book in library.list_of_books

    def test_delete_book_from_library(self, book, library):
        library.delete_book(book_inn=book.inn)
        assert book not in library.list_of_books

    def test_if_library_is_empty(self, library):
        assert not library.list_of_books, "Library should be empty initially"

    def test_is_book_in_library(self, library, book):
        library.add_book(book)
        book_found = False
        for book_item in library.list_of_books:
            if book_item == book:
                book_found = True
                break
        assert book_found, f"Book: {book.book_name} not found in library"

    def test_library_name(self, library):
        assert library.name_of_library == "Yale"

    def test_add_duplicate_book(self, book, library):
        library.add_book(book)
        library.add_book(book)
        assert library.list_of_books.count(book) == 1, "Duplicate book was added"

    def test_unique_inn(self, book, book0):
        assert book.inn != book0.inn, "Inns are not unique"
