from pytest import approx
from functions import add, subtract, multiply
from functions import convert_fahrenheit_to_celsius as f2c

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def test_subtract():
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(2, 3) == 6

def test_f2c():
    assert f2c(32) == 0
    assert f2c(100) == approx(37.7778)
