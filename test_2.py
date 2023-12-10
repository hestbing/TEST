import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, ab", [(2, 3, 5), (-2, -3, -5), (0, 0, 0)])
def test_1(a, b, ab):
    result = add(a, b)
    assert result == ab
    
if __name__ == "__main__":
    pytest.main()
