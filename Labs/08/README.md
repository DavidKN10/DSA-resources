[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11381968&assignment_repo_type=AssignmentRepo)
# Lab: Binary Search Tree

## Overview

For this lab you will implement a handful of binary search tree methods, then adapt the binary search tree to implement the *Map* abstract data type.

## Exercise 1: BSTree methods

For this exercise you'll implement three additional methods in the binary search tree data structure completed in class, so that you have an opportunity to practice both using the recursive pattern covered in class and navigating the binary tree structure.

The methods you'll implement are:

1. `count_less_than`: takes an argument `x`, and returns the number of elements in the tree with values less than `x`
2. `successor`: takes an argument `x`, and returns the smallest value from the tree that is larger than `x` (note that `x` itself does not need to be in the tree); if there are no values larger than `x`, returns `None`
3. `descendants`: takes an argument `x`, and returns all descendants of `x` in the tree (i.e., all values in the subtree rooted at `x`), ordered by value; if `x` has no descendants or does not exist in the tree, returns an empty list


You'll find the `BSTree` class (based on the version implemented during lecture) in the "bstree.py" file. The methods you are to implement can be found at the bottom of the class listing. You should not modify any of the other methods in the class.


## Exercise 2: BSTree as a mapping structure

For this next exercise you will re-implement the binary search tree so that it can be used as a mapping structure. The `Node` class will be updated so as to hold separate key and value attributes (instead of a single value, as it currently does), and instead of the `add` method, you should implement the [`__getitem__`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__) and [`__setitem__`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__) methods in order to associate keys and values. `__delitem__`, `__contains__`, and `__iter__` will also need to be updated, to perform key-based removal, search, and iteration. Finally, the `keys`, `values`, and `items` methods will return iterators that allow the keys, values, and key/value tuples of the tree (all sorted in order of their associated keys) to be traversed.

If `__setitem__` is called with an existing key, the method will simply locate the associated node and update its value with the newly provided value (as you would expect a mapping structure to do). If either `__getitem__` or `__delitem__` are called with a key that does not exist in the tree, a `KeyError` should be raised.

The API described above will allow the tree to be used as follows:

    t = BSTree()
    t[0] = 'zero'
    t[5] = 'five'
    t[2] = 'two'

    print(t[5])
    
    t[5] = 'FIVE!!!'

    for k,v in t.items():
        print(k, '=', v)

    del t[2]

    print('length =', len(t))
    
The expected output of the above follows:

    five
    0 = zero
    2 = two
    5 = FIVE!!!
    length = 2

An updated `BSTree` stub class, containing the updated `Node` subclass and declarations for the methods you are to implement can be found in the "map.py" file.
