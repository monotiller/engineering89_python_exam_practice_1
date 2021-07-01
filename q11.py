# Prompt the user to enter an integer, declare a function that checks if the number is odd or even.
# Display back to the user with the message "The number you chose is odd/even"

num = int(input("Please input an integer: "))

def odd_check(num):
    if num % 2 == 0:
        print(f"Your number {num} is even!")
    else:
        print(f"Your number {num} is odd")

odd_check(num)