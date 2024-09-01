
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


# To Perform this Library Management System
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View available books")
        print("5. View all books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = int(input("Enter publication year: "))
            book = Book(isbn=isbn, title=title, author=author, publication_year=year)
            try:
                library.add_book(book)
                print(f"Book '{title}' added successfully!")
            except ValueError as e:
                print(e)

        elif choice == '2':
            isbn = input("Enter ISBN of the book to borrow: ")
            try:
                library.borrow_book(isbn)
                print(f"Book with ISBN '{isbn}' borrowed successfully!")
            except (KeyError, BookNotAvailableError) as e:
                print(e)

        elif choice == '3':
            isbn = input("Enter ISBN of the book to return: ")
            try:
                library.return_book(isbn)
                print(f"Book with ISBN '{isbn}' returned successfully!")
            except KeyError as e:
                print(e)

        elif choice == '4':
            available_books = library.view_available_books()
            if available_books:
                print("\nAvailable Books:")
                for book in available_books:
                    print(book)
            else:
                print("No books available.")

        elif choice == '5':
            all_books = library.view_all_books()
            if all_books:
                print("\nAll Books in Library:")
                for book in all_books:
                    print(book)
            else:
                print("No books in the library.")

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

