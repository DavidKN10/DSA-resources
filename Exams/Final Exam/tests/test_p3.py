import pytest
import random
from p3_answers import Arraylist


def is_sorted(iterable, reverse=False):
    if reverse:
        return all(iterable[i] >= iterable[i + 1] 
                   for i in range(len(iterable) - 1))
    else:
        return all(iterable[i] <= iterable[i + 1] 
                   for i in range(len(iterable) - 1))
    

def test_given():
    l = Arraylist()

    for x in range(10):
        l.append(random.randint(0, 100))

    idx = 5
    s1 = set(l.data[:idx])
    s2 = set(l.data[idx:len(l)])

    l.sort_around(5)

    assert set(l.data[:idx]) == s1
    assert set(l.data[idx:len(l)]) == s2
    assert is_sorted(l.data[:idx])
    assert is_sorted(l.data[idx:len(l)], reverse=True)
