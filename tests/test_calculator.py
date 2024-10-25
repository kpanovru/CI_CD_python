# tests/test_calculator.py

import pytest
from src.calculator import add, subtract, multiply, divide, modulus, power, factorial

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(6, 0)

def test_modulus():
    assert modulus(5, 3) == 2

def test_power():
    assert power(2, 3) == 8

def test_factorial():
    assert factorial(0) == 1 
    assert factorial(1) == 1 
    assert factorial(5) == 120 
    assert factorial(6) == 720

    with pytest.raises(ValueError):
        factorial(-1)
