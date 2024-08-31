import pytest

from library import Library, Book, BookNotAvailableError

@pytest.fixture
def library():
    # Fixture to initialize a library instance before each test.
    return Library()

def test_add_book(library):
    # Test adding a book to the library.
    book1 = Book(isbn="1234", title="Python", author="Karan", publication_year=2023)
    book2 = Book(isbn="0987", title="Java", author="Chinmay", publication_year=2022)
    book3 = Book(isbn="1122", title="JavaScript", author="Dev", publication_year=2021)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    assert book1.isbn in library.books
    assert book2.isbn in library.books
    assert book3.isbn in library.books



def test_borrow_book(library):
    # Test borrowing a book that is available in the library.
    book = Book(isbn="1234", title="Python", author="Karan", publication_year=2023)
    library.add_book(book)
    library.borrow_book("1234")
    assert not book.is_available

def test_borrow_nonexistent_book(library):
    # Test attempting to borrow a book that does not exist in the library.
    with pytest.raises(KeyError):
        library.borrow_book("0987")

def test_borrow_unavailable_book(library):
    # Test attempting to borrow a book that has already been borrowed.
    book = Book(isbn="1234", title="Python", author="Karan", publication_year=2023)
    library.add_book(book)
    library.borrow_book("1234")
    with pytest.raises(BookNotAvailableError):
        library.borrow_book("1234")

def test_return_book(library):
    # Test returning a borrowed book to the library.
    book = Book(isbn="1234", title="Python", author="Karan", publication_year=2023)
    library.add_book(book)
    library.borrow_book("1234")
    library.return_book("1234")
    assert book.is_available

def test_view_available_books(library):
    # Test viewing a list of all available books in the library.
    book1 = Book(isbn="1234", title="Python", author="Karan", publication_year=2023)
    book2 = Book(isbn="0987", title="Java", author="Chinmay", publication_year=2022)
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book("1234")
    available_books = library.view_available_books()
    assert book2 in available_books
    assert book1 not in available_books

def test_view_all_books(library):
    # Test viewing all books in the library, regardless of availability.
    book1 = Book(isbn="1234", title="Python", author="Karan", publication_year=2023)
    book2 = Book(isbn="0987", title="Java", author="Chinmay", publication_year=2022)
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book("1234")
    all_books = library.view_all_books()
    assert len(all_books) == 2
    assert book1 in all_books
    assert book2 in all_books

