import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
nltk.download('movie_reviews')
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:2000]
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features
featuresets = [(find_features(rev), category) for (rev, category) in documents]
training_set = featuresets[:1500]
testing_set = featuresets[1500:]
classifier = SklearnClassifier(MultinomialNB())
classifier.train(training_set)
accuracy = nltk.classify.accuracy(classifier, testing_set)
print("Accuracy:", accuracy)
custom_text = "This movie is Worst!"
features = find_features(custom_text.split())
classification = classifier.classify(features)
print("Classification:", classification)
