import pytest
from mc_answers import answers

def test_mc():
    assert isinstance(answers, dict)
    assert len(answers) == 10
    assert sorted(answers.keys()) == list(range(1, 11))
    assert all(isinstance(v, str) for v in answers.values())
    assert all(len(v) == 1 for v in answers.values())
    assert all(v.lower() in 'abcde' for v in answers.values())
