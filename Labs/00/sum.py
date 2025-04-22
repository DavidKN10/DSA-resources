def sum_to(k: int) -> int:
    """Returns the sum of integers 0 to k (inclusive)."""
    sum = 0
    for i in range (1, k+1):
        sum += i

    return sum 
