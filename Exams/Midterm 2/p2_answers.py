# Each function below corresponds to one of questions from part 2 on the exam.
# Your code should RETURN (i.e., not print!) the answer to its corresponding
# question. Do NOT change the names of the functions nor their signatures 
# (i.e., the parameters they take). Type annotations are provided for reference.

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


# Do not change the following line
version = 'sum23mid2dca'
