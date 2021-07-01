# Create a class called Student, initialise the class and create an object of the class

class Student:
    def __init__(self, name):
        self.name = name

devops_student = Student("Aman")
print(devops_student.name)