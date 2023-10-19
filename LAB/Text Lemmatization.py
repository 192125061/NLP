import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
lemmatizer = WordNetLemmatizer()
text = "I love BMW cars over Audi Cars and RE bikes than others"
words = nltk.word_tokenize(text)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
lemmatized_text = ' '.join(lemmatized_words)
print(lemmatized_text)
