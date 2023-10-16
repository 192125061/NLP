import nltk
nltk.download('get_wordnet_pos')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

text = "Hello my self sathish from saveetha university"
word = word_tokenize(text)
Lemmatizer = WordNetLemmatizer()
def get_wordnet(tag):
    tag = tag[0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag,wordnet.NOUN)
lemmatized_word = [Lemmatizer.lemmatize(word, get_wordnet_pos(pos_tag)) 
                   for word,pos_tag in nltk.pos_tag(word)]

for word,lemma in zip(word,lemmatized_word):
    print(f"original: {word}, lemma: {lemma}")
    