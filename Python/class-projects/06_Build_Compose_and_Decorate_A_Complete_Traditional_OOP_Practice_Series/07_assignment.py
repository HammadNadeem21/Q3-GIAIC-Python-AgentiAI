# Access Modifiers: Public, Private, and Protected

# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

# Create an instance of Employee
employee = Employee("John Doe", 50000, "123-45-6789")
# Accessing the public variable
print(employee.name)
# Accessing the protected variable (not recommended, but possible)
print(employee._salary)
# Accessing the private variable
print(employee._Employee__ssn)  # This will work because we are using name mangling