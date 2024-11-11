# 1. Right-angle triangle
def right_angle_triangle(n):
    for i in range(1, n+1):
        print("* " * i)

# 2. Inverted right-angle triangle
def inverted_right_angle_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

# 3. Equilateral triangle
def equilateral_triangle(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

# 4. Square pattern
def square_pattern(n):
    for i in range(n):
        print("* " * n)

# 5. Diamond pattern
def diamond_pattern(n):
    for i in range(n):
        print("*" * (n - i - 1) + " " * (i + 1))
    for i in range(n - 2, -1, -1):
        print("*" * (n - i - 1) + " " * (i + 1))

# 6. Hollow square pattern
def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

# 7. Hourglass pattern
def hourglass_pattern(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)
    for i in range(2, n + 1):
        print(" " * (n - i) + "* " * i)

# 8. Right arrow triangle
def right_arrow_triangle(n):
    for i in range(n):
        print(" " * i + "* " * (n - i))
    for i in range(2, n + 1):
        print(" " * (n - i) + "* " * i)

# Function to display all patterns
def display_patterns():
    n = 5  # Change this value to adjust the size of patterns
    print("Right Angle Triangle:")
    right_angle_triangle(n)
    print("\nInverted Right Angle Triangle:")
    inverted_right_angle_triangle(n)
    print("\nEquilateral Triangle:")
    equilateral_triangle(n)
    print("\nSquare Pattern:")
    square_pattern(n)
    print("\nDiamond Pattern:")
    diamond_pattern(n)
    print("\nHollow Square Pattern:")
    hollow_square(n)
    print("\nHourglass Pattern:")
    hourglass_pattern(n)
    print("\nRight Arrow Triangle:")
    right_arrow_triangle(n)

# Call the function to display patterns
display_patterns()
