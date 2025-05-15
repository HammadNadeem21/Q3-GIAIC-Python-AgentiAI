# Public Variables and Methods

# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"The {self.brand} car has started.")


# Create an instance of Car
my_car = Car("Toyota")
# Access the public variable and method
print(my_car.brand)  # Accessing public variable
my_car.start()  # Calling public method
        