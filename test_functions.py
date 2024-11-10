from functions import add, subtract, multiply
from functions import convert_fahrenheit_to_celsius as f2c

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
