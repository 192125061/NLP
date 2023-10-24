import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Sample text to evaluate coherence
text = """
Natural language processing (NLP) is a subfield of artificial intelligence (AI)
dealing with the interaction between computers and humans through natural language.
NLP is concerned with the development of computer programs that can understand,
interpret, and generate human language in a valuable way. NLP tasks include
translation, language generation, sentiment analysis, and more.
"""

# Tokenize the text into sentences
doc = nlp(text)
sentences = [sent.text for sent in doc.sents]

# Calculate sentence embeddings using CountVectorizer
vectorizer = CountVectorizer().fit_transform(sentences)
vectors = vectorizer.toarray()

# Calculate cosine similarity between sentence vectors
cosine_matrix = cosine_similarity(vectors)

# Calculate the average similarity score as a measure of coherence
coherence_score = cosine_matrix.mean()

# Print the coherence score
print("Coherence Score:", coherence_score)
