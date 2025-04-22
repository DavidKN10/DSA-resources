import math
import string

def tokenize(docs: dict[str,str], sw: set[str] = set()) -> dict[str,list[str]]:
    """Tokenizes documents and removes stopwords.
    
    Tokenizes the text using whitespace, lowercases all tokens, and
    removes the provided stopwords."""
    
    tokenized_documents = {}
    stop_words = set(['the', 'are', 'and']) | sw

    for doc_name, doc_content in docs.items():
        # remove punctuation marks
        doc_content = doc_content.translate(str.maketrans('', '', string.punctuation))

        tokens = doc_content.lower().split()

        tokens = [token for token in tokens if token not in stop_words]

        tokenized_documents[doc_name] = tokens

    return tokenized_documents


def build_index(docs: dict[str,list[str]]) -> dict[str,dict[str,int]]:
    """Builds an inverted index from the provided documents.

    The inverted index is a dictionary mapping each token to a dictionary
    of document names and their frequencies."""
    
    inverted_index = {}

    # count the frequency of each token within the document
    for doc_name , tokens in docs.items():
        token_freq = {}
        for token in tokens:
            if token in token_freq:
                token_freq[token] += 1
            else:
                token_freq[token] = 1

    # updating the inverted_index dictionary with the token frequencies for each document
        for token, freq in token_freq.items():
            if token in inverted_index:
                inverted_index[token][doc_name] = freq
            else:
                inverted_index[token] = {doc_name: freq}

    return inverted_index               


def build_tfidf_index(index: dict[str,dict[str,int]], 
                      n_docs: int) -> dict[str,dict[str,float]]:
    """Builds a TF-IDF index from the provided inverted index."""
    tfidf_index = {}

    # Calculate IDF for each token
    idf_scores = {}
    for token, doc_freq in index.items():
        idf_scores[token] = math.log10(n_docs /len(doc_freq))

    # Calculate TF=IDF weights for each token in each document
    for token, doc_freq in index.items():
        tfidf_index[token] = {}
        for doc_name, tf_score in doc_freq.items():
            tfidf_index[token][doc_name] = tf_score * idf_scores[token]

    return tfidf_index


def run_query(index: dict[str,dict[str,float]], 
              query: str) -> list[(str,float)]:
    """Runs a query against the provided index."""

    query_tokens = query.split()
    scores = {}

    for token in query_tokens:
        if token in index:
            for doc, weight in index[token].items():
                if doc in scores:
                    scores[doc] += weight
                else:
                    scores[doc] = weight
    
    sorted_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_results
