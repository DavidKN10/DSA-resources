import random

def is_perfect(n: int) -> bool:
    total = 0
    i = 0
    while total < n:
        i += 1
        total += i
    if total == n:
        return True
    else:
        return False


def integer_right_triangles(p: int) -> int:
    count = 0
    for a in range(1, p // 2):
        for b in range(a, p // 2):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2:
                count += 1
    return count


def two_pair_prob(n_rolls: int, n_trials: int) -> float:
    two_pair_count = 0

    for _ in range(n_trials):
        dice = [random.randint(1, 6) for _ in range(n_rolls)]

        counts = {}
        pair_count = 0

        for roll in dice:
            if roll in counts:
                counts[roll] += 1
                if counts[roll] % 2 == 0:
                    pair_count += 1
            else:
                counts[roll] = 1

        if pair_count >= 2:
            two_pair_count += 1

    return two_pair_count / n_trials