# src/calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Деление на ноль невозможно.")
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def factorial(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
