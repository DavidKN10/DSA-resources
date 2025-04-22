# Your solutions to questions in part 6 on the exam will go in this file.
# Modify the code below per the provided specifications. Do NOT change the 
# names of functions/methods/classes nor their signatures.

from heap import Heap

def merge_sorted_lists(*lists):
    result = []
    heap = Heap(key=lambda x: x[-1])

    for lst in lists:
        if lst:
            heap.add(lst)

    while heap:
        lst = heap.pop()
        element = lst.pop()
        result.append(element)

        if lst:
            heap.add(lst)
    result.reverse()

    return result
