import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.tree import Tree
from nltk import word_tokenize, pos_tag

def generate_parse_tree(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tagged_words)
    result.pretty_print()
generate_parse_tree("The quick brown fox jumps over the lazy dog.")