
class Book:
    """
    Represents a book in the library.

    Attributes:
        isbn (str): The unique identifier for the book.
        title (str): The title of the book.
        author (str): The author of the book.
        publication_year (int): The year the book was published.
        is_available (bool): Indicates if the book is available for borrowing.
    """
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def __repr__(self):
        return f"<Book {self.isbn} - {self.title}>"

class BookNotAvailableError(Exception):
    # Exception raised when a book is not available for borrowing.
    pass

class Library:
    """
    Represents a library that manages a collection of books.

    Methods:
        add_book(book): Adds a book to the library's collection.
        borrow_book(isbn): Borrows a book from the library by ISBN.
        return_book(isbn): Returns a borrowed book to the library by ISBN.
        view_available_books(): Returns a list of all available books in the library.
    """
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        # Adds a book to the library. Raises an error if the book already exists.
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists in the library.")
        self.books[book.isbn] = book

    def borrow_book(self, isbn, borrower=None):
        """
        Borrows a book from the library by ISBN.

        Raises:
            KeyError: If the book with the given ISBN is not found.
            BookNotAvailableError: If the book is already borrowed.
        """
        if isbn not in self.books:
            raise KeyError(f"No book found with ISBN {isbn}")

        book = self.books[isbn]
        if not book.is_available:
            raise BookNotAvailableError(f"Book with ISBN {isbn} is not available.")

        book.is_available = False
        book.borrower = borrower

    def return_book(self, isbn):
        """
        Returns a borrowed book to the library by ISBN.

        Raises:
            KeyError: If the book with the given ISBN is not found.
        """
        if isbn not in self.books:
            raise KeyError(f"No book found with ISBN {isbn}")

        book = self.books[isbn]
        book.is_available = True
        book.borrower = None

    def remove_book(self, isbn):
        # Removes a book from the library by ISBN. Raises an error if the book does not exist.
        if isbn not in self.books:
            raise KeyError(f"No book found with ISBN {isbn}")
        del self.books[isbn]

    def view_available_books(self):
        # Returns a list of all available books in the library.
        return [book for book in self.books.values() if book.is_available]

    def view_all_books(self):
        # Returns a list of all books in the library, regardless of availability.
        return list(self.books.values())

