# Lab: Vector Space Model

## Overview

The [Vector Space Model (VSM)](https://en.wikipedia.org/wiki/Vector_space_model) is used in [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval) to represent documents and queries as vectors in a high-dimensional space, where each dimension corresponds to a token appearing in the entire document collection. In this assignment, you will implement a simple VSM and use it to retrieve and rank documents based on their relevance to a given query.

Consider the following document collection (each document is a single string):

    {
        'doc1': 'the cakes are everywhere',
        'doc2': 'all I want are all the cakes cakes cakes',
        'doc3': 'pies are what I want',
        'doc4': 'cakes and pies are everywhere'
    }

The first thing to do is to [*tokenize*](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization) each document, i.e., split it into a list of tokens (words), typically along whitespace. While doing this, it is also common to remove ["stopwords"](https://en.wikipedia.org/wiki/Stop_word), which are tokens that are so common they are unlikely to be useful for retrieval. Below are the tokenized documents, with the stopwords `{'the', 'are', 'and'}` removed:

    {
        'doc1': ['cakes', 'everywhere'],
        'doc2': ['all', 'i', 'want', 'all', 'cakes', 'cakes', 'cakes'],
        'doc3': ['pies', 'what', 'i', 'want'],
        'doc4': ['cakes', 'pies', 'everywhere']
    }

A central structure in a VSM implementation is the [*inverted index*](https://en.wikipedia.org/wiki/Inverted_index), which maps each token to the documents it appears in, along with the frequency of the token in each document. The following is the inverted index for the above collection:

    {
        'cakes': {'doc1': 1, 'doc2': 3, 'doc4': 1},
        'everywhere': {'doc1': 1, 'doc4': 1},
        'all': {'doc2': 2},
        'i': {'doc2': 1, 'doc3': 1},
        'want': {'doc2': 1, 'doc3': 1},
        'pies': {'doc3': 1, 'doc4': 1},
        'what': {'doc3': 1}
    }

Instead of just using raw token frequency (TF) values, it is common to weight them using each token's *inverse document frequency* (IDF), which is a measure of how much information a token provides, i.e., whether the token is common or rare across all documents. The IDF of a token $t$ is computed as follows:

$$
\hbox{IDF}(t) = \log \frac{\hbox{total num documents}}{\hbox{num documents containing } t}
$$

E.g., the token `'cakes'` appears in 3 out of 4 documents, so its IDF is $\log \frac{4}{3} \approx 0.125$. 

The IDF of a token is used to weight its frequency in a document. E.g., since `'cakes'` appears 3 times in document `'doc2'`, its weighted frequency (known as [TF&middot;IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)) is $3 \times \log \frac{4}{3} \approx 0.375$. Below is the inverted index updated with TF&middot;IDF measures:

    {
        'cakes': {'doc1': 0.125, 'doc2': 0.375, 'doc4': 0.125},
        'everywhere': {'doc1': 0.301, 'doc4': 0.301},
        'all': {'doc2': 1.204},
        'i': {'doc2': 0.301, 'doc3': 0.301},
        'want': {'doc2': 0.301, 'doc3': 0.301},
        'pies': {'doc3': 0.301, 'doc4': 0.301},
        'what': {'doc3': 0.602}
    }

Using this updated inverted index, we can now rank documents based on their similarity to a query. To compute the similarity score between a query and a document, we simply sum up the TF&middot;IDF weights of tokens in the query that also appear in the document (there are more sophisticated approaches, but we'll keep it simple). 

E.g., consider the query `'I want yummy pies'`. After tokenizing the query, we go through the entries in the inverted index and collect the documents that contain any of these tokens, summing together the corresponding TF&middot;IDF weights (`'yummy'` isn't in any document, so contributes nothing). Here are the results, ranked by score:

    [
        ('doc3', 0.903), 
        ('doc2', 0.602), 
        ('doc4', 0.301)
    ]

Note that `'doc1'` is not included in the results, as it does not contain any of the query tokens.

## Implementation Details

Your VSM implementation will go in the `vsm.py` file. You will implement the following four functions (worth 8 points each):

- `tokenize`: Tokenizes documents and removes stopwords. Returns a dictionary mapping document names to lists of tokens.
- `build_index`: Builds an inverted index from the provided tokenized documents. Returns a dictionary mapping tokens to dictionaries of document names and their frequencies.
- `build_tfidf_index`: Builds a TF&middot;IDF-weighted inverted index from the provided TF inverted index. Returns a dictionary mapping tokens to dictionaries of document names and their TF&middot;IDF weights.
- `run_query`: Ranks the documents in the provided TF&middot;IDF-weighted inverted index based on their similarity to the provided query. Returns a list of `(doc_name, score)` tuples, sorted by score in descending order.

Stubs for these functions are provided in `vsm.py`, and they include docstrings and type annotations that should help you understand what each function is supposed to do. You are free to add additional helper functions as needed. Do *not* modify the provided function signatures!

Some implementation notes/hints:

- Use the string [`split`](https://docs.python.org/3/library/stdtypes.html#str.split) method to tokenize documents, and [`lower`](https://docs.python.org/3/library/stdtypes.html#str.lower) to convert tokens to lowercase.
- Use the [`math.log10`](https://docs.python.org/3/library/math.html#math.log10) function to compute logarithms needed for IDF measures.
- The type annotations we include are descriptive but potentially a bit cryptic. It's important that you understand [how to decipher them](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html). E.g., the type annotation `dict[str,dict[str,int]]` describes a dictionary that maps `str`s to dictionaries, where each inner dictionary maps `str`s to `int`s. 
