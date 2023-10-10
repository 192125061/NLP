import nltk
from nltk.parse.generate import generate
from nltk import CFG
grammer = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
PP -> P NP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'""")
parser = nltk.ChartParser(grammer)
sentence = "the cat chased a dog"
tokens = sentence.split()
for tree in parser.parse(tokens):
    tree.pretty_print()
parser = list(parser.parse(tokens))
