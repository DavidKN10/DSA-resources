def f01(l: list[str]) -> set[str]:
    unique_strings = set()
    reversed_strings = set()

    for string in l:
        reversed_string = string[::-1]
        if string not in reversed_strings:
            unique_strings.add(string)
            reversed_strings.add(reversed_string)

    return unique_strings


def f02(d: dict[str, set[int]]) -> dict[str, set[int]]:
    result = {}

    for key, value in d.items():
        lowercase_key = key.lower()
        if lowercase_key in result:
            result[lowercase_key] |= value
        else:
            result[lowercase_key] = value

    return result


def f03(m: int, n: int, c: str) -> list[str]:
    result = []

    for i in range(m, n + 1):
        result.append(c * i)

    for i in range(n, m, - 1):
        result.append(c * i)

    return result


def f04(passage: str, subs: dict[str, str]) -> str:
    words = passage.split()
    result = []

    for word in words:
        if word in subs:
            result.append(subs[word])
        else:
            result.append(word)

    return ' '.join(result)


def f05(s1: str, s2: str) -> list[str | set[str]]:
    words1 = s1.split()
    words2 = s2.split()
    result = []

    for word1, word2 in zip(words1, words2):
        if word1 == word2:
            result.append(word1)
        else:
            result.append({word1, word2})

    return result

