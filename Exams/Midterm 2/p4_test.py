import pytest
from p4 import Hashtable


@pytest.fixture
def ht1():
    ht = Hashtable()
    ht['a'] = 1
    ht['b'] = 2
    ht['c'] = 1
    ht['d'] = 2
    ht['e'] = 1
    return ht


def collect_nodes(ht):
    nodes = {}
    for n in ht.buckets:
        while n is not None:
            nodes[n.key] = n
            n = n.next
    return nodes


def test_given(ht1):
    assert ht1['a'] == 1
    assert ht1['b'] == 2
    assert ht1['c'] == 1
    assert ht1['d'] == 2
    assert ht1['e'] == 1

    old_buckets = ht1.buckets
    old_nodes = collect_nodes(ht1)

    ht1.del_all_by_val(2)

    assert old_buckets is ht1.buckets

    new_nodes = collect_nodes(ht1)
    assert len(new_nodes) == 3
    for k in new_nodes:
        assert k in old_nodes
        assert old_nodes[k] is new_nodes[k]

    assert ht1['a'] == 1
    assert ht1['c'] == 1
    assert ht1['e'] == 1
    assert len(ht1) == 3

    with pytest.raises(KeyError):
        ht1['b']
    with pytest.raises(KeyError):
        ht1['d']

