from heap import Heap
from typing import Iterable


def running_medians(iterable: Iterable[float]) -> list[float]:
    min_heap = Heap(lambda x: -x)  # Min-heap for values greater than the median
    max_heap = Heap()  # Max-heap for values less than the median
    medians = []
    c_median = 0

    for i, x in enumerate(iterable):
        if x > c_median:
            min_heap.add(x)
        else:
            max_heap.add(x)

        if (len(min_heap.data) - len(max_heap.data)) > 1:
            pop_value = min_heap.pop()
            max_heap.add(pop_value)
        elif (len(max_heap.data) - len(min_heap.data)) > 1:
            pop_value = max_heap.pop()
            min_heap.add(pop_value)

        if len(min_heap.data) == len(max_heap.data):
            c_median = (min_heap.peek() + max_heap.peek()) / 2
        elif (len(min_heap.data) - len(max_heap.data)) == 1:
            c_median = min_heap.peek()
        elif (len(max_heap.data) - len(min_heap.data)) == 1:
            c_median = max_heap.peek()
        medians.append(c_median)
    return medians
