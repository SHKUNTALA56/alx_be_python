class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is available.

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"'{self.title}' is not checked out.")

    def __str__(self):
        """Return a string representation of the book."""
        availability = "Checked out" if self._is_checked_out else "Available"
        return f"{self.title} by {self.author} - {availability}"


class Library:
    def __init__(self):
        self._books = []  # Initialize an empty list of books.

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all books that are available."""
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")
