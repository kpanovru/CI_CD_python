# tests/test_calculator.py

import pytest
from src.calculator import add, subtract, multiply, divide, power  # добавляем power

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(0, 1) == 0

    # Проверка на деление на ноль
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Тест для функции power
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(0, 5) == 0
    assert power(1, 5) == 1
