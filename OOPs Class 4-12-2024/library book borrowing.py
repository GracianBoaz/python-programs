class Member:
    def __init__(self, name, membership_id):
        """
        Initialize the member with a name, membership ID, and an empty borrowed books list.
        """
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Add a book to the list of borrowed books.
        """
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            print(f"{book} has been borrowed by {self.name}.")
        else:
            print(f"{self.name} already borrowed {book}.")

    def return_book(self, book):
        """
        Remove a book from the list of borrowed books.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{book} has been returned by {self.name}.")
        else:
            print(f"{self.name} has not borrowed {book}.")

    def display_borrowed_books(self):
        """
        Display the list of borrowed books.
        """
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Example Usage
# Create a Member object
member = Member("Alice", "M1001")

# Borrow books
member.borrow_book("The Great Gatsby")
member.borrow_book("1984")
member.borrow_book("The Great Gatsby")  # Attempt to borrow the same book again

# Display borrowed books
member.display_borrowed_books()

# Return a book
member.return_book("1984")

# Attempt to return a book not borrowed
member.return_book("To Kill a Mockingbird")

# Display updated borrowed books
member.display_borrowed_books()
