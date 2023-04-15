import pytest

# A test that verifies whether 1 + 1 is 2
def test_one_plus_one():
        assert 1 + 1 == 2

# A test that verifies whether a sum of 2 integer variables is equal to that integer value assigned to another variable 
def test_one_plus_two():
        a = 1
        b = 2
        c = 3
        assert a + b == c
    
#A test that verifies an exception
def test_devide_by_zero():
        with pytest.raises(ZeroDivisionError) as e:
            num = 1 / 0
        
        assert 'division by zero' in str(e.value)