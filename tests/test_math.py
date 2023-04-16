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


#Multiplication test ideas

# two positive integers
# identity: multiplying any number by 1
# zero: multiplying any number by 0
# positive by a negative
# negative by a negative
# multiply floats


#def test_multiply_two_positive_ints():
#       assert 2 * 3 == 6

#def test_multiply_identity():
#       assert 6 * 1 == 6 

#def test_multiply_zero():
#       assert 6 * 0 == 0

#To avoid duplication of code, we parametirize the test.

products = [
       (2,3,6),         #postive by positive
       (99,1,99),       #identity
       (100,0,0),       #zero
       (10,-2,-20),     #negative by positive
       (-5,-3,15),      #negative by negative
       (0.5,0.5,0.25)      #floats
]
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
       assert a * b == product