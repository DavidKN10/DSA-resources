import pytest
import random
from p6_answers import merge_sorted_lists


def test_given():
    sorted_lists = [[random.randint(0, 100) 
                     for _ in range(random.randint(5, 10))]  
                    for _ in range(10)]
    
    for l in sorted_lists:
        l.sort()

    sorted_answer = [x for l in sorted_lists for x in l]
    sorted_answer.sort()

    assert merge_sorted_lists(*sorted_lists) == sorted_answer
