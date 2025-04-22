def f01(s: str) -> dict[int, set[str]]:
    words = s.split()
    result = {}

    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}

    return dict(sorted(result.items()))


def f02(docs: dict[str,str]) -> dict[str, set[tuple[int,str]]]:
    index = {}

    for doc_name, doc_body in docs.items():
        words = doc_body.split()
        for index_pos, word in enumerate(words):
            if word in index:
                index[word].add((index_pos, doc_name))
            else:
                index[word] = {(index_pos, doc_name)}
    return index

"""
input_string = 'i really like python and like cake'
output_dict = f01(input_string)
print(output_dict)
"""

docs = {'a': 'the cat chased the mouse', 'b': 'the dog chased the cat'}
index = f02(docs)
print(index)
