# CS 331 Midterm Exam 2 (Summer 2023)

## Part 1: Multiple Choice

Your answers to the multiple choice questions in this section should go into the `answers` dictionary found in the file `mc_answers.py` (instructions on how to modify the dictionary are found in the file). Each question is worth 2 points.

1. Which operations are "most improved" in terms of runtime complexity, going from an array-backed to a linked list implementation?

    - a) random-access / indexing
    - b) appending
    - c) insertion and deletion
    - d) search / lookup
    - e) iteration

2. Why does it make sense to incorporate a cursor-driven API in a linked-list implementation?

    - a) it lets us take advantage of $O(1)$ insertion/deletion without incurring the $O(N)$ cost of indexing
    - b) it lets us implement binary search in $O(\log N)$ time
    - c) it takes advantage of fast indexing behavior
    - d) it enables us to prepend to the list in constant time
    - e) it lets us locate elements by key in $O(1)$ time

3. What would be the most significant downside(s) of implementing the circular doubly-linked list *without* the sentinel head node?

    - a) it would not be possible to insert in $O(1)$ time
    - b) it would not be possible to delete in $O(1)$ time
    - c) there would be no way to locate the tail (last) node efficiently
    - d) iteration would be much more difficult to implement
    - e) there would be a substantial number of edge cases to deal with


4. Given a hashtable with 500 buckets and 5 entries, what is approximate probability of there being at least one bucket containing a chain of length 2 or more? Assume uniform hashing. 

    - a) $1 - (\frac{499}{500})^5 \approx 1.00\%$
    - b) $1 - \frac{499}{500} \times \frac{498}{500} \times \frac{497}{500} \times \frac{496}{500} \approx 1.99\%$
    - c) $5 \times (1 - \frac{495}{500}) \approx 5.00\%$
    - d) $(\frac{499}{500} + \frac{498}{500} + \frac{497}{500} + \frac{496}{500} + \frac{495}{500})/100 \approx 4.97\%$
    - e) $\frac{2 \times 5}{500} \approx 2\%$

5.  A student suggests that one way to improve on the worst-case runtime complexity of hashtable lookups is to keep linked-list chains sorted based on keys, and to perform binary search instead of linear search on the chain after hashing a key to its bucket. Would this work, and what would be the resulting worst-case runtime complexity of hashtable lookups?

    - a) This would improve the worst-case runtime complexity to $O(1)$
    - b) This would improve the worst-case runtime complexity to $O(\log N)$
    - c) This would not work, as it would result in more collisions. The runtime complexity is $O(N^2)$.
    - d) This would not work, as binary search on a linked list does not have good performance. The runtime complexity is $O(N)$.
    - e) This would not work, as it is not possible to keep linked lists sorted. The runtime complexity is $O(N \log N)$.

6.  What might be a reasonable justification for choosing a circular array-backed queue implementation over a linked implementation?

    - a) memory efficiency: the circular array-backed implementation does not require repeated allocations of constituent data containers
    - b) improved runtime complexity: the enqueue and dequeue operations have better runtime complexity in the circular array-backed implementation
    - c) faster indexing: accessing arbitrary elements, which is a necessary operation in a queue, is faster with an array
    - d) scalability: it is easier for the array-backed implementation to accommodate an arbitrary number of elements
    - e) ease of implementation: the array-backed implementation is much less complex than the linked one

7. If you were tasked with choosing a data structure for storing an ordered collection of elements (allowing for duplicates), which supports rapid random access to individual elements based on their position, which would you pick (based on runtime efficiency)?

    - a) array-backed list
    - b) doubly-linked list
    - c) hashtable
    - d) stack
    - e) queue

8. If you were tasked with choosing a data structure for storing an ordered collection of elements (allowing for duplicates), which would be used to simulate the allocation of resources in a "fair" scheduling system, and ensures constant runtime complexity for all operations, which would you pick?

    - a) array-backed list
    - b) doubly-linked list
    - c) hashtable
    - d) stack
    - e) queue

9. If you were tasked with choosing a data structure for maintaining a collection of unique elements, which allows for -- on average -- rapid search/lookup (e.g., to determine whether a given value is contained within the collection), which would you pick?

    - a) array-backed list
    - b) doubly-linked list
    - c) hashtable
    - d) stack
    - e) queue

10. Which data structure is best used to maintain the collection of unexplored locations in the implementation of a depth-first search algorithm?

    - a) array-backed list
    - b) doubly-linked list
    - c) hashtable
    - d) stack
    - e) queue

## Part 2: Data Structure Application

Each of the questions in this section specifies the behavior for a function you are to implement. Your solution to each question should go into the function `fXX`, where `XX` corresponds to the question number (e.g., your solution to question 1 should go into the function `f01`). All functions have been stubbed out for you in the file `p2_answers.py`. Each question is worth 5 points.

1. Input: a string `s` of whitespace-delimited words. Output: a dictionary mapping keys of type `int` to sets of words from `s` with length corresponding to the associated key. E.g., 
   
        Input: 'i really like python and like cake'
        Output: {1: {'i'}, 
                 3: {'and'},
                 4: {'cake', 'like'},
                 6: {'python', 'really'}}

2. Input: a dictionary `docs` mapping document names to bodies (both strings). Output: an inverted index mapping words appearing across all document bodies to sets of tuples, where each tuple contains an index and document name where the corresponding word appears. E.g.,

        Input: {'a': 'the cat chased the mouse', 
                'b': 'the dog chased the cat'}
        Output: {'the': {(0, 'a'), (0, 'b'), (3, 'a'), (3, 'b')},
                 'cat': {(1, 'a'), (4, 'b')},
                 'chased': {(2, 'a'), (2, 'b')},
                 'mouse': {(4, 'a')},
                 'dog': {(1, 'b')}}


## Part 3: Linked List

For this part you are to complete the `LinkedList` implementation found in the file `p3_answers.py`. This singly-linked list only keeps track of the `tail` (which corresponds to the the *last* element) and `size` attributes. Complete the implementations of `__getitem__`, `__setitem__`, and `__delitem__` so as to correctly access, update, and delete elements at the corresponding indexes.

Here are the rules for your implementation:

- assume that the argument indexes are non-negative and valid
- do not call, modify, nor add any other `LinkedList` methods (including the provided ones)
- do not add attributes to any classes
- do not create any new `Node` instances

This part is worth 15 points. Some basic tests are included.


## Part 4: Hashtable

For this part you are to complete the `del_all_by_val` method of class `Hashtable`, found in the file `p4_answers.py`. The method deletes all entries (i.e., key/value pairs) in the hashtable whose values are equal to the argument.

E.g., if the hashtable contains the following entries to start:

    {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1}

Calling `del_all_by_val(2)` on the hashtable would leave only the following entries:

    {'a': 1, 'c': 1, 'e': 1}

Here are the rules for your implementation:

- do not call, modify, nor add any other `Hashtable` methods (including `__delitem__`, which is intentionally left out)
- do not add attributes to any classes
- do not create a new `buckets` container, nor any new `Node` instances
- be sure to correctly update the `size` attribute

This part is worth 10 points. Some basic tests are included.


## Part 5: Stack & Queue

For this part you are to complete the implementation of the combination singly-linked stack and queue data structure, which we call a "`Staque`", defined in the file `p5_answers.py`. In a staque, the "top" of the stack and "head" of the queue refer to the same element, which means that `pop` and `dequeue` would remove and return the same element from a non-empty staque. `push`, however, adds a new element at the "top" position (also updating "head"), while `enqueue` adds a new element at the "tail" position. 

E.g., consider a staque constructed as follows:

    sq = Staque()
    sq.push(1)
    sq.push(2)
    sq.enqueue(3)
    sq.enqueue(4)

Running the following loop:

    while sq:
        print(sq.pop()) # or, equivalently, `print(sq.dequeue())`

Would produce the output:

    2
    1
    3
    4

Here are the rules for your implementation:

- do not add/modify any methods other than push, pop, enqueue, and dequeue
- do not add attributes to any classes
- take care to reset `top`, `head`, and `tail` to `None` when the staque is emptied
- assume that `pop` and `dequeue` are only called on non-empty staques
- all methods should have $O(1)$ runtime complexity (none of your methods should require loops) --- you should carefully consider which "direction" your `next` references point

This part is worth 10 points. Some basic tests are included.



## Testing & Submission

Tests are included with this repository that help ensure your solutions return the expected types. Note that the included tests DO NOT check that your solutions are logically correct! I.e., passing the tests does not mean that you will receive any/full credit. If your code fails to run at all (e.g., due to syntax errors), you will receive no credit for the corresponding question(s).

To submit your work, simply commit and push your changes to your repository. You can commit and push as many times as you like; I will only grade the version that was last pushed before the deadline.
