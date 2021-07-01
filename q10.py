# Declare a dictionary with 3 shopping items, 1) eggs cost £1.20, milk is £2.30, bread is £1
# Write a function that returns the total value

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