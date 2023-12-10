import pytest

def add(a, b):
    return a + b

def test_1():
    assert add(2, 3) == 5

def test_2():
    assert add(-2, -3) == -5

if __name__ == "__main__":
    pytest.main()