class Car:
    def __init__(self, make, model, fuel_level=100):
        """
        Initialize the car with make, model, and fuel level (default is 100).
        """
        self.make = make
        self.model = model
        self.fuel_level = fuel_level

    def drive(self, distance):
        """
        Simulate driving the car. Reduces fuel based on distance driven.
        Assumes 1 unit of fuel is consumed for every 10 km.
        """
        fuel_needed = distance / 10  # 1 unit of fuel per 10 km
        if self.fuel_level >= fuel_needed:
            self.fuel_level -= fuel_needed
            print(f"Driving {distance} km. Fuel used: {fuel_needed} units.")
        else:
            print(f"Not enough fuel to drive {distance} km. Please refuel!")

    def refuel(self, amount):
        """
        Increase the fuel level by the specified amount.
        """
        self.fuel_level += amount
        print(f"Refueled {amount} units. Current fuel level: {self.fuel_level}.")

    def display_status(self):
        """
        Displays the car’s make, model, and current fuel level.
        """
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Fuel Level: {self.fuel_level}%")

# Example Usage
# Create a Car object
my_car = Car("Toyota", "Corolla")

# Display the initial status
my_car.display_status()

# Drive the car for a certain distance
my_car.drive(50)  # Drive 50 km

# Display the status after driving
my_car.display_status()

# Refuel the car
my_car.refuel(30)

# Display the updated status
my_car.display_status()

# Attempt to drive more than the fuel level allows
my_car.drive(300)  # Attempt to drive 300 km with insufficient fuel
