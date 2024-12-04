class HotelRoom:
    def __init__(self, room_number, rate_per_night):
        """
        Initialize the HotelRoom class with room number, occupancy status, and rate per night.
        Initially, the room is not occupied.
        """
        self.room_number = room_number
        self.is_occupied = False  # Room is initially unoccupied
        self.rate_per_night = rate_per_night

    def book_room(self):
        """
        Marks the room as occupied.
        """
        if self.is_occupied:
            print(f"Room {self.room_number} is already occupied.")
        else:
            self.is_occupied = True
            print(f"Room {self.room_number} has been successfully booked.")

    def checkout_room(self):
        """
        Marks the room as vacant.
        """
        if not self.is_occupied:
            print(f"Room {self.room_number} is already vacant.")
        else:
            self.is_occupied = False
            print(f"Room {self.room_number} has been successfully checked out.")

    def display_status(self):
        """
        Displays the room number, rate, and occupancy status.
        """
        status = "Occupied" if self.is_occupied else "Vacant"
        print(f"Room {self.room_number}: Rate = ${self.rate_per_night}/night, Status = {status}")

# Example Usage
# Create a HotelRoom object
room_101 = HotelRoom(101, 100)  # Room 101 with a rate of $100 per night

# Display room status before booking
room_101.display_status()

# Book the room
room_101.book_room()

# Display roo
