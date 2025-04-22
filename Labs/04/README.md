# Lab: Linked List

## Overview

For this assignment you will complete the implementation of the linked list data structure (`LinkedList`) started during class, so that it supports (nearly) all the [common](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) and [mutable](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) sequence operations. You will also be adding APIs for *cursor-driven* operations, which allow for better performance than the more familiar index-driven ones.

Your implementation should make use of doubly-linked nodes (i.e., each containing a `prior` and `next` reference), an ever-present sentinel `head` node (to simplify edge cases), and a "circular" topology (where the head and tail nodes are neighbors).

## Implementation Details

As with the previous assignment, we've partitioned the `LinkedList` methods you need to implement (and the corresponding test cases that follow) into categories:

1. Subscript-based access [6 points]
2. Cursor-based access [6 points]
3. Stringification [2 points]
4. Single-element manipulation [6 points]
5. Predicates (True/False queries) [4 points]
6. Queries [6 points]
7. Bulk operations [6 points]
8. Iteration [2 points]

All your code will go in `linkedlist.py`, where you will find stubs for all the methods you need to implement, along with further documentation. You may add additional private methods if you find it helpful to do so.

Besides (2), you should be familiar with the APIs from all the other categories, as you implemented them for the previous lab. The cursor-based methods are detailed in the next section.

## Cursor-based access

As discussed in lecture, a cursor-driven API makes sense for a linked list, as it allows us to avoid repeated $O(N)$ indexing when manipulating adjacent elements.

The cursor-based APIs you will implement are as follows:

- `cursor_get`: retrieves the value at the current cursor position (if valid)
- `cursor_set`: sets the cursor to the node at the provided index
- `cursor_move`: moves the cursor forward or backward by the provided offset (a positive or negative integer);  note that it is possible to advance the cursor past the beginning or end of the list, in which case the cursor will just "wrap around", skipping over the sentinel node
- `cursor_insert`: inserts a new value after the cursor and sets the cursor to the new node
- `cursor_delete`: deletes the node the cursor refers to and sets the cursor to the following node

### Hints / Advice

While you will have to implement some of the methods from scratch — i.e., in terms of the new underlying linked storage mechanism — you should be able to reuse quite a few of your method implementations from the previous assignment (the array-backed list), providing you defined them in terms of other, lower-level methods. This may not always be the most efficient (e.g., loops that repeatedly make use of `__getitem__` to access succeeding elements are clear offenders), but while we recommend that you try to optimize for improved run-time efficiency it is not a grading criterion for this assignment.
