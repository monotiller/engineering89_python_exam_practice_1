# Exam 1 practice
These are practice exam questions and answers for the first course exam taking place on the 2^nd July 2021

## Question 1
Declare a function called username that takes one argument as a string and return the name

<details>
  <summary>Click to show answer</summary>

```python
def username(name):
    return name


print(username("Leah"))
```
</details>

## Question 2
Declare a list with number 1 - 5. Iterate through the list and display the list

<details>
  <summary>Click to show answer</summary>

```python
ls = [1, 2, 3, 4, 5]

for i in ls:
    print(i)
```
</details>

## Question 3
`AND`, `&&,` `&`, `==`
Which one returns the boolean value?

<details>
  <summary>Click to show answer</summary>

```python
name = "Louis"

if name == "Louis": # It's the ==
```
</details>

## Question 4
What is the difference between a list and a tuple

<details>
  <summary>Click to show answer</summary>

A list is mutable, is defined with [ ]
A tuple is immutable, is defined with ( )
</details>

## Question 5
1. Can we add an element to a list?
2. Can we add an element to a tuple
3. Can the element of a tuple be different types

<details>
  <summary>Click to show answer</summary>

1. Yes
2. No
3. Yes
</details>

## Question 6
Create a dictionary with key: value pairs; "first_name" and "last_name"

<details>
  <summary>Click to show answer</summary>

```python
dict = {
    "first_name": "Joe",
    "last_name": "Bloggs",
}
```
</details>

## Question 7
Taking the dictionary from question 6, append a new key called "course" and then delete it

<details>
  <summary>Click to show answer</summary>

```python
dict = {
    "first_name": "Joe",
    "last_name": "Bloggs",
}

dict["course"] = "DevOps"
print(dict) # You won't need to include this in the exam, this is here for debugging

del dict["course"]
print(dict)
```
</details>

## Question 8
Create a class called Student, initialise the class and create an object of the class

<details>
  <summary>Click to show answer</summary>

```python
class Student:
    def __init__(self, name):
        self.name = name

devops_student = Student("Aman")
print(devops_student.name)
```
</details>

## Question 9
Create two functions that take two arguments each. func1 = add_value. func2 = subtract_value. Return both of these values

<details>
  <summary>Click to show answer</summary>

```python
def add_value(num1, num2):
    return num1 + num2

def subtract_value(num1, num2):
    return num1 - num2

print(add_value(1, 2))
print(subtract_value(1, 2))
```
</details>

## Question 10
Declare a dictionary with 3 shopping items, 1) eggs cost £1.20, milk is £2.30, bread is £1

Write a function that returns the total value

<details>
  <summary>Click to show answer</summary>

```python
def total_value(shopping):
    sub_total = 0
    for value in shopping:
        sub_total += value
    return sub_total

shopping = {
    "eggs": 1.20,
    "milk": 2.30,
    "bread": 1.00,
}

print(total_value(shopping.values()))
```
</details>

## Question 11
Prompt the user to enter an integer, declare a function that checks if the number is odd or even.

Display back to the user with the message "The number you chose is odd/even"

<details>
  <summary>Click to show answer</summary>

```python
num = int(input("Please input an integer: "))

def odd_check(num):
    if num % 2 == 0:
        print(f"Your number {num} is even!")
    else:
        print(f"Your number {num} is odd")

odd_check(num)
```
</details>

## Question 12
select the correct syntax- 1 `-super.__init()`. 2- `super()__init()`. 3 `super().__init()`. 4 - `Super().__init__()`

<details>
  <summary>Click to show answer</summary>

None of then, it's actually `super().__init__()`

Pay attention to cases
</details>

## Question 13
Declare a tuple with three values of your choice

Iterate through the tuple and display the values

<details>
  <summary>Click to show answer</summary>

```python
my_tuple = ("this", 2, "tuple")

for i in my_tuple:
    print(i)
```
</details>

Now delete the final value

<details>
  <summary>Click to show answer</summary>

Guess what! You can't, tuples are immutable
</details>

## Question 14
Create a class called "Student" with one method called "student_data" which returns "student_name"

Create a class called "DevOpsStudent" which inherits the "Student" class and prints the name

<details>
  <summary>Click to show answer</summary>

```python
class Student:
    def student_data(self):
        return "Salem"

class DevOpsStudent(Student):
    def __init__(self):
        super().__init__()

ds = DevOpsStudent()
print(ds.student_data())
```
</details>

## Question 15
Declare a variable called "city", declare a method that takes city as an argument and value of the city as "London" and method checks if valus is London the true if not false

<details>
  <summary>Click to show answer</summary>

```python
city = "London"

def check_cityname(city):
    if city.strip().lower() == "london":
        return True
    else:
        return False

print(check_cityname(city))
```
</details>

## Question 16
import `sys` module, import `math`, and create a function that takes two arguments and gives you the percentage of those two numbers

<details>
  <summary>Click to show answer</summary>

```python
import random
import sys
import math

def percentage(num1, num2):
    return (num1 * 100) / num2

print(percentage(random.randint(1, 100), random.randint(1, 100)))
```
</details>