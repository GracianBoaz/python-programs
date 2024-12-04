class Library:
    def __init__(self):
        """
        Initialize the library with an empty dictionary to store books and their availability.
        """
        self.books = {}  # Dictionary to store book titles and availability status

    def add_book(self, title):
        """
        Add a new book to the library.
        """
        if title in self.books:
            print(f"The book '{title}' already exists in the library.")
        else:
            self.books[title] = True  # True indicates the book is available
            print(f"Book '{title}' has been added to the library.")

    def borrow_book(self, title):
        """
        Borrow a book from the library if it is available.
        """
        if title not in self.books:
            print(f"Sorry, the book '{title}' is not in the library.")
        elif not self.books[title]:
            print(f"Sorry, the book '{title}' is currently borrowed.")
        else:
            self.books[title] = False  # Mark the book as borrowed
            print(f"You have borrowed the book '{title}'.")

    def return_book(self, title):
        """
        Return a book to the library and mark it as available.
        """
        if title not in self.books:
            print(f"The book '{title}' does not belong to this library.")
        elif self.books[title]:
            print(f"The book '{title}' was not borrowed.")
        else:
            self.books[title] = True  # Mark the book as available
            print(f"Thank you for returning the book '{title}'.")

    def view_books(self):
        """
        Display the list of all books and their availability status.
        """
        if not self.books:
            print("The library has no books.")
        else:
            print("\nBooks in the Library:")
            for title, available in self.books.items():
                status = "Available" if available else "Borrowed"
                print(f"- {title}: {status}")


# Example Usage
library = Library()

# Adding books
library.add_book("The Great Gatsby")
library.add_book("To Kill a Mockingbird")
library.add_book("1984")

# Viewing books
library.view_books()

# Borrowing a book
library.borrow_book("1984")
library.borrow_book("The Great Gatsby")

# Viewing books after borrowing
library.view_books()

# Returning a book
library.return_book("1984")

# Viewing books after returning
library.view_books()
