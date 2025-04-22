import pytest
import random
from heap import Heap

@pytest.mark.points(1)
def test_heap_basic():
    h = Heap()
    random.seed(0)
    for _ in range(10):
        h.add(random.randrange(100))

    assert h.data == [97, 61, 65, 49, 51, 53, 62, 5, 38, 33]

@pytest.mark.points(1)
def test_heap_minheap():
    h = Heap(lambda x:-x)
    random.seed(0)
    for _ in range(10):
        h.add(random.randrange(100))

    assert h.data == [5, 33, 53, 38, 49, 65, 62, 97, 51, 61]

@pytest.mark.points(2)
def test_heap_lenkey():
    h = Heap(lambda s:len(s))
    h.add('hello')
    h.add('hi')
    h.add('abracadabra')
    h.add('supercalifragilisticexpialidocious')
    h.add('0')
    assert (h.data ==
            ['supercalifragilisticexpialidocious', 
             'abracadabra', 'hello', 'hi', '0'])

@pytest.mark.points(2)
def test_heap_max_order():
    h = Heap()

    random.seed(0)
    lst = list(range(-1000, 1000))
    random.shuffle(lst)

    for x in lst:
        h.add(x)

    for x in range(999, -1000, -1):
        assert h.pop() == x


@pytest.mark.points(2)
def test_heap_abs_order():
    h = Heap(lambda x:abs(x))
    
    random.seed(0)
    lst = list(range(-1000, 1000, 3))
    random.shuffle(lst)

    for x in lst:
        h.add(x)

    for x in reversed(sorted(range(-1000, 1000, 3), key=lambda x:abs(x))):
        assert h.pop() == x
