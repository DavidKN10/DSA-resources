import pytest
from p2_answers import f01, f02, f03, f04, f05

@pytest.fixture
def list_str():
    return [str(x) for x in range(10)]

@pytest.fixture
def dict_str_set_int():
    return {'a': {1, 2, 3}, 'b': {4, 5, 6}, 'c': {7, 8, 9}}

@pytest.fixture
def dict_str_str():
    return {'a': 'b', 'c': 'd', 'e': 'f'}

def test_f01(list_str):
    assert isinstance(f01(list_str), set)

def test_f02(dict_str_set_int):
    assert isinstance(f02(dict_str_set_int), dict)

def test_f03():
    assert isinstance(f03(1, 2, 'a'), list)
    assert isinstance(f03(1, 2, 'a')[0], str)

def test_f04(dict_str_str):
    assert isinstance(f04('a b c', dict_str_str), str)

def test_f05():
    assert isinstance(f05('a b c', 'a b d'), list)
