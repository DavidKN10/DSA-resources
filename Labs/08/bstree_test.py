import pytest
from bstree import BSTree


@pytest.mark.points(3)
def test_count_less_than():
    t = BSTree()
    for x in [6, 3, 5, 4, 7, 1, 2, 9, 8, 0]:
        t.add(x)

    assert t.count_less_than(6) == 6
    assert t.count_less_than(0) == 0
    assert t.count_less_than(9) == 9
    assert t.count_less_than(100) == 10
    assert t.count_less_than(-100) == 0


@pytest.mark.points(3)
def test_successor():
    t = BSTree()
    for x in [6, 3, 5, 4, 7, 1, 2, 9, 8, 0]:
        t.add(x)

    assert t.successor(6) == 7
    assert t.successor(6.5) == 7
    assert t.successor(4) == 5
    assert t.successor(5) == 6
    assert t.successor(8) == 9
    assert t.successor(-1) == 0
    assert t.successor(9) is None
    assert t.successor(10) is None


@pytest.mark.points(3)
def test_descendants():
    t = BSTree()
    for x in [6, 3, 5, 4, 7, 1, 2, 9, 8, 0]:
        t.add(x)

    assert t.descendants(6) == [0, 1, 2, 3, 4, 5, 7, 8, 9]
    assert t.descendants(3) == [0, 1, 2, 4, 5]
    assert t.descendants(7) == [8, 9]
    assert t.descendants(1) == [0, 2]
    assert t.descendants(0) == []
    assert t.descendants(8) == []
    assert t.descendants(100) == []
    assert t.descendants(-100) == []
