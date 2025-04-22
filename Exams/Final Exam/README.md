# Final Exam (Summer 2023)

## Part 1: Multiple Choice

Your answers to the multiple choice questions in this section should go into the `answers` dictionary found in the file `mc_answers.py` (instructions on how to modify the dictionary are found in the file). Each question is worth 2 points.


1. What is the worst-case runtime complexity for adding $N$ elements to a hash table (which starts out empty)?

    - a) $O(1)$
    - b) $O(\log N)$
    - c) $O(N)$
    - d) $O(N \log N)$
    - e) $O(N^2)$

2. What is the worst-case runtime complexity for adding $N$ elements to a binary search tree (which starts out empty)?
   
    - a) $O(1)$
    - b) $O(\log N)$
    - c) $O(N)$
    - d) $O(N \log N)$
    - e) $O(N^2)$

3. What is the worst-case runtime complexity for adding $N$ elements to a max-heap (which starts out empty)?

    - a) $O(1)$
    - b) $O(\log N)$
    - c) $O(N)$
    - d) $O(N \log N)$
    - e) $O(N^2)$

4. What is the worst-case runtime complexity of inserting a new element into a binary search tree of $N$ elements, assuming that the new element’s value is neither the new minimum nor maximum value after insertion?

    - a) $O(1)$
    - b) $O(\log N)$
    - c) $O(N)$
    - d) $O(N \log N)$
    - e) $O(N^2)$

5. At most how many swaps would be needed to "re-heapify" a max-heap of 100 elements after removing the maximum value?

    - a) 3
    - b) 7
    - c) 12
    - d) 18
    - e) 50

6. Which of the following array-based representations of complete binary trees (using the parent/left/right index mappings described in class) is not a valid heap?

	- a) [12, 6, 4, 5, 3, 2, 1]
	- b) [12, 3, 6, 1, 2, 5, 4]
	- c) [12, 4, 6, 2, 3, 5, 1]
	- d) [12, 3, 6, 4, 1, 5, 2] 
	- e) [12, 6, 5, 4, 3, 2, 1]


7. Assuming that a binary search tree is implemented such that its height is always $O(\log N)$, where $N$ is the number of elements in the tree, what is the primary benefit to using this binary search tree as a mapping structure over the hashtable?

    - a) faster amortized search
    - b) faster amortized deletion 
    - c) faster amortized insertion
    - d) improved memory efficiency
    - e) efficient ordered traversal


8. Which of the following data structures would you choose to use if you needed to efficiently track a set of unique values and be able to quickly add and remove elements and determine membership?

    - a) array-backed list
    - b) linked list
    - c) hashtable
    - d) heap
    - e) binary search tree


9. Which of the following data structures would you choose to use if you needed to efficiently track a set of unique values and be able to quickly locate and remove either the smallest or largest value?

    - a) array-backed list
    - b) linked list
    - c) hashtable
    - d) heap
    - e) binary search tree

10. Which was your favorite data structure that we covered in this course?

    - a) array-backed list
    - b) linked list
    - c) hashtable
    - d) stack
    - e) queue
    - f) heap
    - g) binary search tree
    - h) AVL tree


## Part 2: Data Structure Application

For this part you will implement the function `schedule_slots`, found in the file "p2_answers.py". The function accepts a dictionary mapping strings representing dates to sets of strings representing names of persons available on those dates. The function should process the input dictionary and return a dictionary of the same type, but such that each person is assigned to exactly one date. 

`schedule_slots` will apply the following rules in an attempt to minimize the number of dates required to schedule all persons:

- the date with the most available persons should be selected first
- if multiple dates have the same number of available persons, the date with the earliest (alphabetically) date string should be selected first
- once a person is assigned to a date, they should not be considered for any other dates

E.g., if `schedule_slots` is called with the following input:

    { '2023-06-10': {'Derek', 'Eve', 'Frank'},
      '2023-06-11': {'Adam', 'Bob', 'Chad', 'Derek'},
      '2023-06-12': {'Bob', 'Eve', 'Frank'},
      '2023-06-13': {'Greg'},
      '2023-06-14': {'Frank'} }

It should return:

    { '2023-06-11': {'Adam', 'Bob', 'Chad', 'Derek'},
      '2023-06-10': {'Eve', 'Frank'},
      '2023-06-13': {'Greg'} }

This part is worth 10 points. Some basic tests are included.


## Part 3: Array-backed List

For this part you will implement the `sort_around` method of the array-backed list implementation found in class `ArrayList`, in the file "p3_answers.py". The method accepts a single integer argument `idx`, which represents a positive, valid index in the list. The method should sort the elements in the list such that all elements before `idx` are in ascending order, and all elements after `idx` are in descending order. 

E.g., if the list contains the following elements to start:

    [24, 78, 82, 18, 54, 65, 16, 70, 8, 75]

Calling `sort_around(5)` on the list would result in the following arrangement:

    [18, 24, 54, 78, 82, 75, 70, 65, 16, 8]

Here are the rules for your implementation:

- you may use any sort algorithm, but you must implement it yourself (i.e., you may not call any other sort methods)
- you may not use any additional data structures (e.g., lists, sets, etc.)
- you should not create any new arrays (i.e., you should sort the elements within the existing array)

This part is worth 10 points. Some basic tests are included.


## Part 4: Linked List

For this part you will implement the `interpolate` method of the singly-linked list implementation found in class `LinkedList`, in the file "p4_answers.py". The method accepts two arguments: `val` (an arbitrary value) and `k` (an integer), and updates the list by inserting `val` after every `k` elements in the list. Note that if the list contains a multiple of `k` elements, then `val` will be appended after the last element in the list.

E.g., if the list contains the following elements to start:

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Calling `interpolate(0, 1)` on the list would result in the following arrangement:

    [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]

On the other hand, calling `interpolate(0, 3)` on the original list would result in the following arrangement:

    [0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 10]

Here are the rules for your implementation:

- you may not call any other `LinkedList` methods, nor introduce any new attributes/methods
- you should only create as many new `Node`s as strictly necessary (i.e., corresponding to the interpolated values)
- you may not use any additional data structures (e.g., lists, sets, etc.)

This part is worth 10 points. Some basic tests are included.

## Part 5: Hashtable

For this part you are to update the hashtable implementation found in class `Hashtable`, in the file "p5_answers.py". Specifically, you are to update the `__getitem__` method so that, each time a key is accessed, the corresponding node is moved to the front of the bucket list (so as to speed up future accesses).

E.g., if the hashtable contains the following nodes (of <key,value> pairs) in a particular chain:

    <'a', 'apple'> -> <'b', 'bee'> -> <'c', 'cat'> -> <'d', 'dog'>

Then, if the key `'c'` is accessed, the chain should be updated to the following:

    <'c', 'cat'> -> <'a', 'apple'> -> <'b', 'bee'> -> <'d', 'dog'>

Here are the rules for your implementation:

- do not call, modify, nor add any other `Hashtable` methods (including `__delitem__`, which is intentionally left out)
- do not add attributes to any classes
- do not create a new `buckets` container, nor any new `Node` instances (i.e., you should only move existing nodes around)
- your implementation should raise a `KeyError`, as before, if the key is not found

This part is worth 10 points. Some basic tests are included.


## Part 6: Heap

For this part you are to implement the function `merge_sorted_lists`, found in the file "p6_answers.py". The function accepts one or more lists of integers sorted in ascending order, and returns a single list containing all of the elements from the input lists, sorted in ascending order.

You must implement the function using a heap (a working heap implementation is provided in "heap.py", which is already imported for you in "p6_answers.py"), to achieve linearithmic runtime complexity. Here is the algorithm you should follow:

1. Create a new heap, and add each of the input lists to the heap; the heap should be keyed to the last element in each list (i.e., the largest element in each list)
2. While the heap is not empty:
    - Pop a list from the heap, and remove and add its last element to the result list
    - If the list isn't empty, add it back to the heap
3. Reverse and return the result list

Here are the rules for your implementation:

- you may not use any additional data structures (e.g., lists, sets, etc.)
- you should not manually search for the min/max element across the lists (i.e., you must use the heap to do this)

This part is worth 10 points. Some basic tests are included.


## Part 7: Binary Search Tree

For this part, you are to implement two separate binary search tree methods: `ancestors`, and `left_children`, both found in class `BSTree`, in the file "p7_answers.py". The methods are described below.

- The `ancestors` method accepts a single argument `val`, and returns a list of all ancestors of the node containing `val`, starting at the root of the tree. If `val` is found in the root of the tree, the list should be empty. If `val` isn't in the tree, the method should return `None`.

  E.g., given the following tree:

                50
              /     \
            25       75
           /  \        \
         10    30       80
        /  \     \     /
       5   12    35  77

  Calling `ancestors(35)` would return the following list:

      [50, 25, 30]

- The `left_children` method takes no arguments, and simply returns a set of all values found in the left child of any node in the tree. E.g., given the same tree as above, the method would return the following set:

      {5, 10, 25, 77}

Here are the rules for your implementation:

- you may not call any other `BSTree` methods, nor introduce any new attributes/methods
- you may not modify the underlying tree

This part is worth 10 points. Some basic tests are included.


## Testing & Submission

Tests are included with this repository that help ensure your solutions return the expected types. Note that the included tests DO NOT check that your solutions are logically correct! I.e., passing the tests does not mean that you will receive any/full credit. If your code fails to run at all (e.g., due to syntax errors), you will receive no credit for the corresponding question(s).

To submit your work, simply commit and push your changes to your repository. You can commit and push as many times as you like; I will only grade the version that was last pushed before the deadline.
