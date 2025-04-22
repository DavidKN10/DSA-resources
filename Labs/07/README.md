[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11370565&assignment_repo_type=AssignmentRepo)
# Lab: Heap

## Overview

For this assignment you will start by modifying the heap data stucture implemented in class to allow it to keep its elements sorted by an arbitrary priority (identified by a `key` function), then use the augmented heap to efficiently compute the running median of a set of numbers.


## 1. Augmenting the Heap with a `key` function

The heap implementation covered in class is for a so-called "max-heap" — i.e., one where elements are organized such that the one with the maximum value can be efficiently extracted.

This limits our usage of the data structure, however. Our heap can currently only accommodate elements that have a natural ordering (i.e., they can be compared using the '`>`' and '`<`' operators as used in the implementation), and there's no way to order elements based on some partial or computed property.

To make our heap more flexible, you'll update it to allow a `key` function to be passed to its initializer. This function will be used to extract a value from each element added to the heap; these values, in turn, will be used to order the elements. 

We can now easily create heaps with different semantics, e.g.,

- `Heap(len)` will prioritize elements based on their length (e.g., applicable to strings, sequences, etc.)
- `Heap(lambda x: -x)` can function as a *min-heap* for numbers
- `Heap(lambda x: x.prop)` will prioritize elements based on their `prop` attribute

If no `key` function is provided, the default max-heap behavior should be used — the "`lambda x:x`" default value for the `__init__` method does just that. 

You will, at the very least, need to update the `_heapify` and `add` methods, below, to complete this assignment. (Note, also, that `pop_max` has been renamed `pop`, while `max` has been renamed `peek`, to reflect their more general nature.)

Your implementation will go into the `heap.py` file, where you will find a stub for class `Heap`.


## 2. Computing the Running Median

The median of a series of numbers is simply the middle term if ordered by magnitude, or, if there is no middle term, the average of the two middle terms. E.g., the median of the series [3, 1, 9, 25, 12] is **9**, and the median of the series [8, 4, 11, 18] is **9.5**.

If we are in the process of accumulating numerical data, it is useful to be able to compute the *running median* — where, as each new data point is encountered, an updated median is computed. This should be done, of course, as efficiently as possible.

The following function demonstrates a naive way of computing the running medians based on the series passed in as an iterable.

```python
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
```

E.g., `running_medians_naive([3, 1, 9, 25, 12])` returns `[3, 2, 3, 6, 9]`.

E.g., `running_medians_naive([8, 4, 11, 18])` returns `[8, 6, 8, 9.5]`.

Note that the function keeps track of all the values encountered during the iteration and uses them to compute the running medians, which are returned at the end as a list. The final running median, naturally, is simply the median of the entire series.

Unfortunately, because the function sorts the list of values during every iteration it is incredibly inefficient. Your job is to implement a version that computes each running median in $O(\log N)$ time using, of course, the heap data structure!

Your implementation will go into the `medians.py` file, where you will find a stub for the function `running_medians`. Note that your function must complete its last test (which runs it on a large series of random numbers) in under 10 seconds to be considered correct.


### Hints

- You will need to use two heaps for your solution: one min-heap, and one max-heap. 
- The min-heap should be used to keep track of all values *greater than* the most recent running median, and the max-heap for all values *less than* the most recent running median — this way, the median will lie between the minimum value on the min-heap and the maximum value on the max-heap (both of which can be efficiently extracted)
- In addition, the difference between the number of values stored in the min-heap and max-heap must never exceed 1 (to ensure the median is being computed). This can be taken care of by carefully `pop`-ping/`add`-ing elements between the two heaps.
