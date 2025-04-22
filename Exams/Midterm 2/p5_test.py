from p5 import Staque
import pytest

@pytest.fixture
def sq1():
    sq = Staque()
    sq.push(1)
    sq.push(2)
    sq.enqueue(3)
    sq.enqueue(4)
    return sq


def test_given(sq1):
    assert sq1.pop() == 2
    assert sq1.pop() == 1
    assert sq1.dequeue() == 3
    assert sq1.dequeue() == 4
    assert not sq1
    assert sq1.top is None
    assert sq1.head is None
    assert sq1.tail is None
