import pytest
from p3_answers import ArrayList

@pytest.fixture
def lst0_9():
    l = ArrayList()
    for i in range(10):
        l.append(i)
    return l

def test_iter_in_order(lst0_9):
    assert lst0_9.iter_in_order([1, 2, 3])

def test_move_range(lst0_9):
    assert lst0_9.move_range(0, 5, 3) is None
