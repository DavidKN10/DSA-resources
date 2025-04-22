import pytest
from pytest import approx
import basics

class TestExercise:
    def test_is_perfect(self):
        assert basics.is_perfect(6) == True
        assert basics.is_perfect(7) == False
        assert basics.is_perfect(28) == True
        assert basics.is_perfect(496) == True
        assert basics.is_perfect(8128) == True
        assert basics.is_perfect(33550336) == True
        assert basics.is_perfect(33550337) == False

    def test_integer_right_triangles(self):
        assert basics.integer_right_triangles(60)  == 2
        assert basics.integer_right_triangles(100) == 0
        assert basics.integer_right_triangles(180) == 3
        assert basics.integer_right_triangles(840) == 8
        assert basics.integer_right_triangles(3300) == 7

    def test_two_pair_prob(self):
        assert basics.two_pair_prob(1, 10000) == 0.0
        assert basics.two_pair_prob(2, 10000) == 0.0
        assert basics.two_pair_prob(3, 10000) == 0.0
        assert basics.two_pair_prob(4, 10000) == approx(0.074, abs=0.02)
        assert basics.two_pair_prob(4, 1_000_000) == approx(0.074, abs=0.005)
        assert basics.two_pair_prob(5, 1_000_000) == approx(0.290, abs=0.005)
        assert basics.two_pair_prob(6, 1_000_000) == approx(0.598, abs=0.005)
        assert basics.two_pair_prob(10, 1_000_000) == 1.0
