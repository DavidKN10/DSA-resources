# Lab: Ordered Hashtable

## Overview

For this assignment you will update and complete the implementation of the hashtable data structure presented in class, which exposes an API mirroring that of the built-in Python `dict`. When iterating over its contents (supported by the `__iter__`, `keys`, `values`, and `items` methods), your updated implementation will also reflect the order in which key/value pairs were originally inserted into the hashtable. In order to maintain $O(1)$ (amortized) runtime complexity, you will need to implement the two-tiered list system presented in lecture.

The operations you will implement are listed alongside their descriptions below (`h` refers to a hashtable):

| Operation | Description |
|-----------|-------------|
| `h[k] = v` | If `h` does not contain key `k`, a new `k`&rightarrow;`v` mapping is added, else the value for key `k` is updated to `v`. |
| `h[k]`    | If `h` contains key `k`, the corresponding value is returned, else a `KeyError` is raised. |
| `del h[k]` | If `h` contains key `k`, it is removed along with its value, else a `KeyError` is raised. Note that if `k` is re-inserted at some later point it is considered a new key (for ordering purposes). |
| `k in h` | Returns `True` if key `k` is in `h`. |
| `len(h)` | Returns the number of keys in `h`. |
| `iter(h)` | Returns an iterator over all the keys in `h`, in the order they were added. |
| `h.keys()` | (Same as above) |
| `h.values()` | Returns an iterator over all the values in `h`, in the order they were added. |
| `h.items()` | Returns an iterator over all the key/value pairs (as tuples) in `h`, in the order they were added. |

Your hashtable will be provided with the initial number of buckets on creation (i.e., in `__init__`); your implementation must heed this value, as there may be performance ramifications if it does not.

## Implementation Details

All your code will go into `hashtable.py`, where we include stubs for all the methods you will need to implement. You may add additional methods, but you may not change the signatures of the existing methods. You may assume that all keys are hashable.
