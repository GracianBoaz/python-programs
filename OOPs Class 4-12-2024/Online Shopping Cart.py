class ShoppingCart:
    def __init__(self):
        """
        Initialize the shopping cart with an empty dictionary.
        """
        self.items = {}

    def add_item(self, item, quantity):
        """
        Add a specified quantity of an item to the cart.
        """
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} of '{item}' to the cart.")

    def remove_item(self, item, quantity):
        """
        Remove a specified quantity of an item from the cart.
        If the quantity to remove exceeds the available quantity, remove the item completely.
        """
        if item in self.items:
            if quantity >= self.items[item]:
                self.items.pop(item)
                print(f"Removed all of '{item}' from the cart.")
            else:
                self.items[item] -= quantity
                print(f"Removed {quantity} of '{item}' from the cart.")
        else:
            print(f"'{item}' not found in the cart.")

    def view_cart(self):
        """
        Display all items in the cart along with their quantities.
        """
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Items in your shopping cart:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")

    def clear_cart(self):
        """
        Clear all items from the cart.
        """
        self.items.clear()
        print("The shopping cart has been cleared.")


# Example Usage
cart = ShoppingCart()

# Add items to the cart
cart.add_item("Apples", 5)
cart.add_item("Bananas", 3)

# View cart
cart.view_cart()

# Remove some items
cart.remove_item("Apples", 2)
cart.view_cart()

# Remove all of an item
cart.remove_item("Bananas", 3)
cart.view_cart()

# Add more items
cart.add_item("Oranges", 4)

# Clear the cart
cart.clear_cart()
cart.view_cart()
