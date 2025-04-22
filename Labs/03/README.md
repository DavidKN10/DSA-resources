# Lab: Array-Backed Lists

## Overview

For this assignment you will complete the implementation of the array-backed list data structure (`ArrayList`) started during class, so that it supports (nearly) all the [common](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) and [mutable](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) sequence operations.


## Implementation Details

For the `ArrayList`'s underlying data storage mechanism you will use the [NumPy array](https://numpy.org/doc/stable/reference/arrays.html), as described in class. You will be using a very limited subset of the available APIs for working with NumPy arrays, however. Specifically, you may use:

- [`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html) for creating empty arrays. You will be calling it like this (assuming the numpy library has been imported as `np`, as we always do): `np.empty(N, dtype=object)`. This will create an empty array of size `N`, each slot of which can be used to store a reference to an arbitrary Python object.

- Valid, *positive* indexes into arrays. It will be your job in the implementation of `ArrayList` to check for valid indexes and to translate negative indexes into positive ones.

- `len(arr)` to get the length (i.e., number of slots) of array `arr`. Note that this will not generally coincide with the number of actual elements in the list!

**You should not use any other array-related functions provided by NumPy!** Notably, `delete`, `insert`, `append`, `resize`, and others, are off limits. Using them to carry out list operations is, generally speaking, less efficient than the manual approach outlined in class. Also, it's important that you learn how to implement them yourself. Breaking this rule will result in significant score reduction(s).


### `ArrayList`

And now for the task at hand. We've broken down the `ArrayList` methods you need to implement (and the test cases that follow) into seven categories:

1. Subscript-based access [6 points]
2. Stringification [4 points]
3. Single-element manipulation [8 points]
4. Predicates (True/False queries) [4 points]
5. Queries [10 points]
6. Bulk operations [6 points]
7. Iteration [2 points]

All told, there are 21 methods --- a handful of which we implemented together in class --- whose behavior are specified in their docstrings. Stubs for all the methods are found in `arraylist.py`. Note that we left out API support for *slices* (e.g., `lst[start:stop:step]`); you can read about [how to support slices in the Python docs](https://docs.python.org/3/reference/datamodel.html#object.__length_hint__), but we just don't think it's worth the extra busywork.


### Hints / Advice

We strongly advise that you start with the first category of functions and move down the list sequentially, pausing after each to run the corresponding tests. The only method you may wish to jump ahead and implement early on is `__iter__`. Keep in mind that while you're not permitted to make use of NumPy APIs (beyond those listed above), you can certainly make use of `ArrayList` methods you've already implemented.

For instance, your implementations of `pop` and `remove` can (and should) use the `del` operator on your own list to remove elements from the middle, and it probably makes sense to use `extend` in your `__add__` and `copy` methods.

When in doubt as to how a method should behave, consult the [Python docs](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) for guidance. If you're still unsure, ask on Discord!
