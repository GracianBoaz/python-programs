class Employee:
    def __init__(self, name, employee_id, salary):
        """
        Initialize the employee with a name, employee ID, and salary.
        """
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """
        Display the employee's details.
        """
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Current Salary: ${self.salary:.2f}")

    def give_raise(self, percent):
        """
        Increase the employee's salary by the specified percentage.
        """
        if percent > 0:
            raise_amount = self.salary * (percent / 100)
            self.salary += raise_amount
            print(f"Salary increased by {percent}%. New salary: ${self.salary:.2f}")
        else:
            print("Raise percentage must be positive.")


# Example Usage
# Creating an Employee object
employee = Employee("John Doe", "E12345", 50000)

# Display employee details
employee.display_details()

# Give a 10% raise
employee.give_raise(10)

# Display updated employee details
employee.display_details()

# Attempt to give a negative raise (error handling)
employee.give_raise(-5)
