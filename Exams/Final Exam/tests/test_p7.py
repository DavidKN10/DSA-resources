import pytest
from p7_answers import BSTree

@pytest.fixture
def bst_given():
    t = BSTree()
    for x in [50, 25, 75, 10, 30, 80, 5, 12, 35, 77]:
        t.add(x)
    return t


def test_ancestors_given(bst_given):
    assert bst_given.ancestors(35) == [50, 25, 30]


def test_left_children_given(bst_given):
    assert bst_given.left_children() == {5, 10, 25, 77}
