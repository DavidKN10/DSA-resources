import pytest
from p2_answers import schedule_slots

def test_given():
    input = { '2023-06-10': {'Derek', 'Eve', 'Frank'},
              '2023-06-11': {'Adam', 'Bob', 'Chad', 'Derek'},
              '2023-06-12': {'Bob', 'Eve', 'Frank'},
              '2023-06-13': {'Greg'},
              '2023-06-14': {'Frank'} }
    expected = { '2023-06-11': {'Adam', 'Bob', 'Chad', 'Derek'},
                 '2023-06-10': {'Eve', 'Frank'},
                 '2023-06-13': {'Greg'} }
    assert schedule_slots(input) == expected
