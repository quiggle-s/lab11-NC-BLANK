"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")

def logarithm(a, b):
    try:
        return math.log(a, b)
    except (ValueError, TypeError):
        raise ValueError("Invalid input for logarithm")

def exponent(a, b):
    return a ** b