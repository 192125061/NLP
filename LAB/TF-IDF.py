import math
from collections import Counter

# Sample collection of documents
documents = [
    "This is the first document. It is a simple document.",
    "This document is the second one. It has more words.",
    "And this is the third document. It has even more words."
]

# Sample query
query = "simple document"

# Step 1: Preprocess the documents
stopwords = set(["this", "is", "the", "and", "it", "has"])

tokenized_documents = []
for doc in documents:
    doc = doc.lower()
    doc = doc.split()
    doc = [word for word in doc if word not in stopwords and word.isalpha()]
    tokenized_documents.append(doc)

# Step 2: Calculate TF-IDF scores for each term in each document
N = len(documents)
vocabulary = set(word for doc in tokenized_documents for word in doc)

tfidf_scores = []
for doc in tokenized_documents:
    tfidf_doc = {}
    for term in vocabulary:
        tf = doc.count(term)
        df = sum(1 for d in tokenized_documents if term in d)
        idf = math.log(N / (df + 1))
        tfidf = tf * idf
        tfidf_doc[term] = tfidf
    tfidf_scores.append(tfidf_doc)

# Step 3: Rank the documents based on TF-IDF scores
query = query.lower().split()
query_vector = Counter(query)

ranked_documents = []
for i, doc in enumerate(tfidf_scores):
    dot_product = sum(doc[term] * query_vector[term] for term in query if term in doc)
    doc_length = math.sqrt(sum(score ** 2 for score in doc.values()))
    query_length = math.sqrt(sum(score ** 2 for score in query_vector.values()))
    
    if query_length == 0:
        similarity = 0
    else:
        similarity = dot_product / (doc_length * query_length)

    ranked_documents.append((i, similarity))

ranked_documents.sort(key=lambda x: x[1], reverse=True)

# Display the ranked documents
for i, similarity in ranked_documents:
    print(f"Document {i + 1} - Similarity: {similarity:.4f}")
