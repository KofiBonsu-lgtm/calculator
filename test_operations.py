from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
import pytest

def test_add():
    assert addition(2, 3) == 5
def test_subtract():
    assert subtraction(5, 3) == 2
def test_divide():
    assert division(6, 2) == 3    

