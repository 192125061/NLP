import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')  # Download necessary NLTK data

def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

def main():
    words = ["running", "cats", "geese", "friendships", "jumps"]

    print("Original Words:", words)

    stemmed_words = stem_words(words)

    print("Stemmed Words:", stemmed_words)

if __name__ == "__main__":
    main()