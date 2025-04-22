import pytest
from p5_answers import Hashtable

def list_from_chain(n):
    l = []
    while n:
        l.append((n.key, n.val))
        n = n.next
    return l


@pytest.fixture
def ht100():
    ht = Hashtable(10)
    for x in range(100):
        ht[x] = x
    return ht


def test_given(ht100):
    for x in range(100):
        assert ht100[x] == x

    ht100[0]
    assert ht100.buckets[0].key == 0

    ht100[10]
    assert ht100.buckets[0].key == 10
