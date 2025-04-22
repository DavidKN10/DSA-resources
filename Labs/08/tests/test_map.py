import pytest
import random
from map import BSTree

@pytest.mark.points(2)
def test_simple_search():
    t = BSTree()
    assert len(t) == 0
    assert 0 not in t
    t[0] = 'zero'
    assert 0 in t
    assert len(t) == 1


@pytest.mark.points(2)
def test_simple_map():
    t = BSTree()
    assert len(t) == 0
    t[0] = 'zero'
    assert t[0] == 'zero'


@pytest.mark.points(2)
def test_simple_deletion():
    t = BSTree()
    assert len(t) == 0
    t[0] = 'zero'
    del t[0]
    assert 0 not in t
    assert len(t) == 0


@pytest.mark.points(2)
def test_key_iter():
    t = BSTree()
    key_vals = [(0, 'zero'), (2, 'two'), (1, 'one')]
    sorted_key_vals = sorted(key_vals)

    for k,v in key_vals:
        t[k] = v

    for i,k in enumerate(t.keys()):
        assert k == sorted_key_vals[i][0]


@pytest.mark.points(1)
def test_value_iter():
    t = BSTree()
    key_vals = [(0, 'zero'), (2, 'two'), (1, 'one')]
    sorted_key_vals = sorted(key_vals)

    for k,v in key_vals:
        t[k] = v

    for i,v in enumerate(t.values()):
        assert v == sorted_key_vals[i][1]


@pytest.mark.points(1)
def test_item_iter():
    t = BSTree()
    key_vals = [(0, 'zero'), (2, 'two'), (1, 'one')]
    sorted_key_vals = sorted(key_vals)

    for k,v in key_vals:
        t[k] = v

    for i,(k,v) in enumerate(t.items()):
        assert k == sorted_key_vals[i][0]
        assert v == sorted_key_vals[i][1]


@pytest.mark.points(3)
def test_many_entries():
    t = BSTree()
    keys = list(range(100, 1000, 11))
    random.shuffle(keys)
    vals = [random.randrange(1000) for _ in range(100, 1000, 11)]

    for i in range(len(keys)):
        t[keys[i]] = vals[i]

    for i in range(len(keys)):
        assert t[keys[i]] == vals[i]


@pytest.mark.points(3)
def test_iterators_large():
    t = BSTree()
    keys = list(range(100, 1000, 11))
    shuffled_keys = keys.copy()
    random.shuffle(shuffled_keys)

    for k in shuffled_keys:
        t[k] = str(k)

    for i,k in enumerate(t.keys()):
        assert k == keys[i]

    for i,v in enumerate(t.values()):
        assert v == str(keys[i])

    for i,(k,v) in enumerate(t.items()):
        assert k == keys[i]
        assert v == str(keys[i])


@pytest.mark.points(3)
def test_keyerror():
    t = BSTree()
    keys = list(range(0, 100, 2))
    random.shuffle(keys)

    for x in keys:
        t[x] = x*2

    for k in range(1, 101, 2):
        with pytest.raises(KeyError):
            v = t[k]
