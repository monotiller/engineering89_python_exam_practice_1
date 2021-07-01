# Create a class called "Student" with one method called "student_data" which returns "student_name"
# Create a class called "DevOpsStudent" which inherits the "Student" class and prints the name

class Student:
    def student_data(self):
        return "Salem"

class DevOpsStudent(Student):
    def __init__(self):
        super().__init__()

ds = DevOpsStudent()
print(ds.student_data())