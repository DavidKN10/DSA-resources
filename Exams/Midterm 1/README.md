# Midterm Exam 1 (Summer 2023)

## Part 1: Multiple Choice

Your answers to the multiple choice questions in this section should go into the `answers` dictionary found in the file `mc_answers.py` (instructions on how to modify the dictionary are found in the file). Each question is worth 2 points.

1. Which of the following data types in Python is *mutable*?

    - a) `str` (string)
    - b) `int`
    - c) `tuple`
    - d) `list`
    - e) `range`

2. Which of the following relations is true?

    - a) $n^2 = O(n)$
    - b) $15n + 200 = O(n)$
    - c) $n^3 - 1000 = O(\log n)$
    - d) $2^n = O(n^2)$
    - e) $10 \log n = O(1)$

3. What best describes the relationship between $f(n)$ and $g(n)$ if $f(n) = O(g(n))$?

    - a) as $n$ gets large, $g(n)$ is less than or equal to some multiple of $f(n)$
    - b) as $n$ gets large, $f(n)$ is less than or equal to some multiple of $g(n)$ 
    - c) there is some $n$ that makes $f(n)$ less than $g(n)$ 
    - d) there is some $n$ that makes $g(n)$ less than $f(n)$ 
    - e) the maximum value of $f(n)$ is less than the maximum value of $g(n)$ (for positive $n$)

4. What is the maximum number of elements a properly implemented binary search will need to compare a value against in order to determine its position in a sorted list of 30,000 elements

    - a) 5
    - b) 10
    - c) 15
    - d) 20
    - e) 25

5. What is the worst-case runtime complexity of the following function, as a function of its input list size $N$?

    ```python
    def foo(lst):
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] == lst[j]:
                    return True
        return False
    ```

    - a) $O(1)$
    - b) $O(\log N)$
    - c) $O(N)$
    - d) $O(N \log N)$
    - e) $O(N^2)$

6. What is the worst-case runtime complexity of the following function, as a function of its input list size $N$?

    ```python
    def bar(lst):
        if len(lst) > 10:
            return lst[0]
        else:
            rv = 0
            for x in lst:
                rv *= x
            return rv
    ```

    - a) $O(1)$
    - b) $O(\log N)$
    - c) $O(N)$
    - d) $O(N \log N)$
    - e) $O(N^2)$

7. What is the worst-case runtime complexity of the following function, as a function of its input list size $N$?

    ```python
    def shuf(lst):
        for i in range(len(lst)):
            idx1 = random.randrange(len(lst)) # assume this is O(1)
            idx2 = random.randrange(len(lst)) # assume this is O(1)
            lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    ```

    - a) $O(1)$
    - b) $O(\log N)$
    - c) $O(N)$
    - d) $O(N \log N)$
    - e) $O(N^2)$

8. Which of the following is *not* true of all iterators in Python?

    - a) `next` can be called on them to obtain the next value (when available)
    - b) `iter` can be called on them to obtain an iterator
    - c) they raise a `StopIteration` exception when there are no more values to return
    - d) they can be used as the target of a `for` loop
    - e) they are implemented using the `yield` keyword

9. Which of the following array-backed list methods has the poorest (i.e., fastest growing) runtime complexity?

    - a) `__getitem__`
    - b) `append`
    - c) `__setitem__`
    - d) `__len__`
    - e) `__delitem__`

10. When might you prefer to use a list comprehension instead of a semantically equivalent generator expression to compute a sequence of values??

    - a) when we need to use the sequence as a target of a for loop
    - b) when we need random access (by index) to the values in the sequence
    - c) when the sequence will be iterated over once and then discarded
    - d) when the sequence will only be iterated over partially
    - e) when you plan on creating a tuple from the sequence

## Part 2: Data Structure Application

Each of the questions in this section specifies the behavior for a function you are to implement. Your solution to each question should go into the function `fXX`, where `XX` corresponds to the question number (e.g., your solution to question 1 should go into the function `f01`). All functions have been stubbed out for you in the file `p2_answers.py`. Each question is worth 5 points.

1. Input: a list `l` of strings. Output: a set of strings from `l`. If `l` contains any strings that are the reverse of each other, the returned set should only contain the string that is alphabetically first. E.g., 
   
        Input: ['reed', 'bar', 'deer', 'peels', 'foo', 'sleep']
        Output: {'bar', 'deer', 'foo', 'peels'}

2. Input: a dictionary `d` mapping strings to sets of integers. Output: a dictionary of the same type, where the sets of integers for keys that are lowercase-equivalent are merged together. The result dictionary only contains lowercase keys. E.g.,

        Input: {'tom': {1, 2, 3}, 
                'jack': {4, 6}, 
                'TOM': {2, 3, 4}, 
                'Tom': {3, 4, 5}, 
                'JACK': {5, 7}}

        Output: {'tom': {1, 2, 3, 4, 5}, 
                 'jack': {4, 5, 6, 7}}


3. Input: two integers, $m$ and $n$ (where $m < n$), and a string `c`. Output: a list of strings consisting of $[m, m+1, ..., n-1, n, n-1, ... m+1, m]$ repetitions of `c`. E.g.,

        Input: m=3, n=6, c='*'
        Output: ['***', '****', '*****', '******', '*****', '****', '***']

4. Input: a string `passage` and a dictionary `subs` mapping strings to their substitution strings. Output: a string obtained by replacing all occurrences of keys from `subs` in `passage` with their corresponding values. Tokenization should be based on whitespace. E.g.,

        Input: passage='the cat sat on the mat'
               subs={'cat': 'dog', 'mat': 'rug'}
        Output: 'the dog sat on the rug'

5. Input: two strings `s1` and `s2`, each containing the same number of words after whitespace tokenization. Output: a list, where each entry is a string when the corresponding words in `s1` and `s2` are the same, or a set of the two words otherwise. E.g.,

        Input: s1='the cat sat on the mat'
               s2='the dog sat on the rug'
        Output: ['the', {'cat', 'dog'}, 'sat', 'on', 'the', {'mat', 'rug'}]


## Part 3: Array-Backed List Implementation

Each of the questions in this section specifies the behavior for an `ArrayList` method you are to implement. Your solutions should go into the file `p3_answers.py`, and will involve modifying one or more methods that have been stubbed out for you, according to the question specifications. Each question is worth 10 points.

1. Implement the `iter_in_order` method so that, given a list of valid indexes `idxs`, the method returns an iterator that iterates over the elements in the list in the order specified by `idxs`. E.g.,

        List contents: ['c', 'o', 'm', 'p', 'u', 't', 'e', 'r']
        Operation: iter_in_order([3, 1, 1, 7, 2, 6])
        Output: iterator over ['p', 'o', 'o', 'r', 'm', 'e']

    Note that the iterator should be able to handle repeated elements in `idxs`. Your implementation should not use any other methods of the `ArrayList` class.

2. Implement the `move_range` method so that, given a source index `src`, a destination index `dst`, and a length `n`, the elements in the range `[src, src+n)` are moved to the range `[dst, dst+n)`, with surrounding elements being shifted down/up as necessary to accommodate the move. Assume that there is no overlap between the source and destination indexes. E.g.,

        Starting list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        Operation: move_range(src=1, dst=6, n=3)
        Ending list: [0, 4, 5, 6, 7, 8, 1, 2, 3, 9]

    Note that `src` may be less than or greater than `dst`. Your implementation should operate on the underlying array directly, and should not use any other methods of the `ArrayList` class. If you wish, you may use an intermediate array to help with the move.


## Testing & Submission

Tests are included with this repository that help ensure your solutions return the expected types. Note that the included tests DO NOT check that your solutions are logically correct! I.e., passing the tests does not mean that you will receive any/full credit. If your code fails to run at all (e.g., due to syntax errors), you will receive no credit for the corresponding question(s).

To submit your work, simply commit and push your changes to your repository. You can commit and push as many times as you like; I will only grade the version that was last pushed before the deadline.
