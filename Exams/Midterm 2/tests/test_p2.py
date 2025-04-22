import pytest
from p2_answers import f01, f02

# f01

def test_f01():
    assert isinstance(f01('foo'), dict)


# f02    

def test_f02():
    assert isinstance(f02({}), dict)
