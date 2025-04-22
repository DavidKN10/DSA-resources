import pytest
import sum

class TestSum:
    def test_sum_to(self):
        assert sum.sum_to(5) == 15
        assert sum.sum_to(10) == 55
        assert sum.sum_to(999) == 499500
        assert sum.sum_to(0) == 0
        assert sum.sum_to(-999) == 0
