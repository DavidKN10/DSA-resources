import pytest
from p3_answers import LinkedList

@pytest.fixture
def ll1():
    ll = LinkedList()
    for i in range(10):
        ll.append(i)
    return ll


def test_unmodified(ll1):
    assert ll1.tail.value == 9
    assert ll1.size == 10
    n = ll1.tail
    for _ in range(9):
        n = n.prior
    assert n.value == 0
    assert n.prior is None


def test_basic(ll1):
    for i in range(10):
        assert ll1[i] == i
    for i in range(10):
        ll1[i] = str(i)
    for i in range(10):
        assert ll1[i] == str(i)
    del ll1[0]
    for i in range(9):
        assert ll1[i] == str(i+1)
