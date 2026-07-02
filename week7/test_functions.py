from my_functions import add

# case 1
def test_add_01():
    a = 0
    b = 0
    expected = 0
    actual = add(a, b)
    assert actual == expected

# case 2
def test_add_02():
    a = 5
    b = 0
    expected = 5
    actual = add(a, b)
    assert actual == expected

# case 3
def test_add_03():
    a = -5
    b = 0
    expected = -5
    actual = add(a, b)
    assert actual == expected

# case 4
def test_add_04():
    a = 2
    b = 3
    expected = 5
    actual = add(a, b)
    assert actual == expected


# Test cases for rank function
from my_functions import rank

def test_rank_01():
    grade = -1                  # edge case
    expected = "invalid"
    actual = rank(grade)
    assert actual == expected

def test_rank_02():
    grade = -10                  # normal case
    expected = "invalid"
    actual = rank(grade)
    assert actual == expected

def test_rank_03(): 
    grade = 101                  # edge case
    expected = "invalid"
    actual = rank(grade)
    assert actual == expected

def test_rank_04():
    grade = 150                  # normal case
    expected = "invalid"
    actual = rank(grade)
    assert actual == expected