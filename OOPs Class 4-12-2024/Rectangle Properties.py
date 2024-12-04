class Rectangle:
    def __init__(self, length, width):
        """
        Initialize the rectangle with length and width.
        """
        self.length = length
        self.width = width

    def calculate_area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.length * self.width

    def calculate_perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)

    def is_square(self):
        """
        Check if the rectangle is a square.
        """
        return self.length == self.width


# Example Usage
# Create a rectangle object
rect = Rectangle(10, 5)

# Calculate area
print("Area of the rectangle:", rect.calculate_area())

# Calculate perimeter
print("Perimeter of the rectangle:", rect.calculate_perimeter())

# Check if it's a square
if rect.is_square():
    print("The rectangle is a square.")
else:
    print("The rectangle is not a square.")

# Another Example with a square
square = Rectangle(7, 7)
print("\nFor a rectangle with equal length and width:")
print("Area:", square.calculate_area())
print("Perimeter:", square.calculate_perimeter())
print("Is it a square?", "Yes" if square.is_square() else "No")
