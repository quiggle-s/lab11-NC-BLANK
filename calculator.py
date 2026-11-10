#https://github.com/quiggle-s/lab11-NC-BLANK
#Partner 1: Nicholas Chea
#Partner 2: None

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take square root of negative number")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def mult(a, b): 
    return a * b

def div(a, b): 
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")

def logarithm(a, b):
    try:
        return math.log(a, b)
    except (ValueError, TypeError):
        raise ValueError("Invalid input for logarithm")

def exp(a, b):
    return a ** b