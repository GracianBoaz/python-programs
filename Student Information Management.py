#4/12/2024
class Student:
    def __init__(self, name, roll_number):
        """
        Initialize student with name, roll number, and an empty marks dictionary.
        """
        self.name = name
        self.roll_number = roll_number
        self.marks = {}  

    def add_marks(self, subject, mark):
        """
        Add or update marks for a specific subject.
        """
        if mark < 0 or mark > 100:
            print("Mark should be between 0 and 100.")
            return
        self.marks[subject] = mark
        print(f"Added/Updated marks for {subject}: {mark}")

    def get_average(self):
        """
        Calculate and return the average marks.
        """
        if not self.marks:
            print("No marks available to calculate average.")
            return 0
        total_marks = sum(self.marks.values())
        average = total_marks / len(self.marks)
        return average

    def display_details(self):
        """
        Display the student's details, including name, roll number, and average marks.
        """
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        if self.marks:
            print("Marks:")
            for subject, mark in self.marks.items():
                print(f"- {subject}: {mark}")
            print(f"Average Marks: {self.get_average():.2f}")
        else:
            print("No marks available.")


student1 = Student("Alice", "S101")
student1.add_marks("Math", 85)
student1.add_marks("Science", 90)
student1.add_marks("English", 78)

student1.display_details()
