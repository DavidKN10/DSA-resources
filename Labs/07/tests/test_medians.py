import pytest
import random
from medians import running_medians


def running_medians_naive(iterable):
    values = []
    medians = []
    for i, x in enumerate(iterable):
        values.append(x)
        values.sort()
        if i%2 == 0:
            medians.append(values[i//2])
        else:
            medians.append((values[i//2] + values[i//2+1]) / 2)
    return medians


@pytest.mark.points(2)
def test_medians_basic():
    assert running_medians([3, 1, 9, 25, 12]) == [3, 2.0, 3, 6.0, 9]


@pytest.mark.points(2)
def test_medians_vs_naive():
    vals = [random.randrange(10000) for _ in range(1000)]
    assert running_medians(vals) == running_medians_naive(vals)


@pytest.mark.points(4)
def test_medians_stress():
    vals = [random.randrange(100000) for _ in range(100001)]
    m_mid   = sorted(vals[:50001])[50001//2]
    m_final = sorted(vals)[len(vals)//2]
    running = running_medians(vals)
    assert running[50000] == m_mid
    assert running[-1] == m_final
