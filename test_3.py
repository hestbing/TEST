# -*- coding: cp1251 -*-

import pytest

class Calc:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtraction(self, a, b):
        self.result = a - b
        return self.result

    def multiplication(self, a, b):
        self.result = a * b
        return self.result

    def division(self, a, b):
        if b == 0:
            raise ValueError("нельзя")
        self.result = a / b
        return self.result

    def get_result(self):
        return self.result

@pytest.fixture
def calc():
    return Calc()

def test_1(calc):
    calc.add(2, 3)
    assert calc.get_result() == 5

def test_2(calc):
    calc.subtraction(5, 2)
    assert calc.get_result() == 3

def test_3(calc):
    calc.multiplication(4, 3)
    assert calc.get_result() == 12

def test_4(calc):
    calc.division(10, 2)
    assert calc.get_result() == 5

def test_5(calc):
    with pytest.raises(ValueError, match="На ноль делить нельзя"):
        calc.divide(6, 0)
        
if __name__ == "__main__":
    pytest.main()