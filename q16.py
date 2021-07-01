# import sys module, import math, and create a function that takes two arguments and gives you the percentage of those two numbers

import random
import sys
import math

def percentage(num1, num2):
    return (num1 * 100) / num2

print(percentage(random.randint(1, 100), random.randint(1, 100)))