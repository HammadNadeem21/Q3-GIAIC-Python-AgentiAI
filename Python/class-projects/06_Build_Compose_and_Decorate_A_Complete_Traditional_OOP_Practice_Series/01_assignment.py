class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)    
    

std1 = Student("John", 89)
std2 = Student("harry", 99)

std1.display()
std2.display()
print(std1.name)


