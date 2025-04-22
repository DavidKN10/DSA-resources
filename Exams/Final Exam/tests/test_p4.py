import pytest
from p4_answers import LinkedList


def list_from_ll(ll):
    l = []
    n = ll.head
    while n:
        l.append(n.val)
        n = n.next
    return l


@pytest.fixture
def ll1_10():
    l = LinkedList()
    for i in range(10, 0, -1):
        l.prepend(i)
    return l


def test_given_1(ll1_10):
    assert list_from_ll(ll1_10) == list(range(1, 11))
    ll1_10.interpolate(0, 1)
    assert list_from_ll(ll1_10) == [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 
                                    6, 0, 7, 0, 8, 0, 9, 0, 10, 0]


def test_given_2(ll1_10):
    assert list_from_ll(ll1_10) == list(range(1, 11))
    ll1_10.interpolate(0, 3)
    assert list_from_ll(ll1_10) == [0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 10]
