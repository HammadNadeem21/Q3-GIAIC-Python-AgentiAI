#  The super() Function

# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name  
        print(f"Person created with name: {self.name}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the base class constructor
        self.subject = subject
        print(f"{self.name} is a teacher of {self.subject}")
    
# Example usage     
teacher1 = Teacher("Alice", "Mathematics")
teacher2 = Teacher("Bob", "Physics")
