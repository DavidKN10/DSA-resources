# Lab 01: Python Basics

## Overview

This assignment is designed to give you practice with Python's built-in numeric types and control structures. You will also learn to use the `random` module, which allows you to generate random numbers.

## Implementation Details

All the exercises in this assignment will have you making edits to `basics.py`.

## Exercise 1: Perfect Numbers (5 points)

Complete the `is_perfect` function, which takes an integer $i$, so that it returns `True` if $i$ is a "perfect" number, and `False` otherwise.

A perfect number is a positive integer whose value is equal to the sum of its proper divisors (i.e., its factors excluding the number itself). 6 is the first perfect number, as its divisors 1, 2, and 3 add up to 6.

## Exercise 2: Integer Right Triangles (5 points)

Given a perimeter of 60, we can find two right triangles with integral length sides: [(10, 24, 26), (15, 20, 25)]. Complete the function `integer_right_triangles`, which takes an integer $p$ and returns the number of unique integer right triangles with perimeter $p$.

For full credit, your implementation must complete in under 1 minute for all tests. Note that this means you should think about the efficiency of your implementation!

## Exercise 3: Monte Carlo Simulation (5 points)

A Monte Carlo simulation is a method of approximating an unknown value --- often a probability or statistic --- by performing a large number of random trials. For instance, instead of using [combinatorics](https://en.wikipedia.org/wiki/Combinatorics) to directly calculate the probability of rolling a 7 with two dice, we can simulate rolling two dice a large number of times and calculate the fraction of times that the sum of the dice is 7. To do this, we need to be able to generate random numbers, which we can do with the `random` module. The following code shows how we might compute the probability of rolling a 7 with two dice:

```python
import random

def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def estimate_seven_prob(trials):
    count = 0
    for i in range(trials):
        if roll_two_dice() == 7:
            count += 1
    return count / n
```

Here are some results of running `estimate_seven_prob` with varying numbers of trials:

    estimate_seven_prob(100)
    > 0.22

    estimate_seven_prob(1_000)
    > 0.179

    estimate_seven_prob(10_000)
    > 0.1712

    estimate_seven_prob(1_000_000)
    > 0.166804

Note that there are six different ways of rolling a 7 with two dice (1+6, 2+5, 3+4, 4+3, 5+2, 6+1), out of a total of thirty-six possible outcomes. So the probability of rolling a 7 is 6/36 = 1/6 = 0.1666... . As we increase the number of trials, our estimate of the probability gets closer to the true value.

---

For this exercise, you are to complete the function `two_pair_prob`, which estimates the probability of rolling two pairs with $n\_rolls$ independent dice rolls, over $n\_trials$ trials. A "pair" is two dice with the same value, and "two pairs" is two distinct pairs of dice with the same value. For example, the following sequences contain two pairs over 5 rolls: (2, 1, 1, 3, 2), (3, 4, 3, 6, 4). Note that we are not interested in the probability of rolling *exactly* two pairs, but rather the probability of rolling two pairs or more. For example, the following also count as two pairs over 5 rolls: (1, 1, 1, 2, 2), (1, 1, 1, 1, 2), (1, 1, 1, 1, 1). The following do *not* count as two pairs over 5 rolls: (1, 1, 2, 3, 1), (3, 4, 6, 5, 3), (2, 3, 4, 5, 6).

**Note**: we will be checking that you are computing your result via random trials. Using combinatorics (or hard-coding results) will earn you no credit!
