import spacy

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Sample text with pronoun references
text = "John went to the store. He bought some groceries."

# Process the text using spaCy
doc = nlp(text)

# Initialize a dictionary to store referents
referents = {}

# Iterate through the processed sentences
for sent in doc.sents:
    # Iterate through tokens in the sentence
    for token in sent:
        # If the token is a pronoun
        if token.pos_ == "PRON":
            # Get the head noun of the pronoun
            head_noun = token._.coref_clusters[0].main.text
            referents[token.text] = head_noun

# Replace pronouns with their referents
resolved_text = text
for pronoun, referent in referents.items():
    resolved_text = resolved_text.replace(pronoun, referent)

# Print the resolved text
print("Original Text:")
print(text)
print("\nResolved Text:")
print(resolved_text)
