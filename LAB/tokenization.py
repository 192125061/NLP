from nltk.tokenize import RegexpTokenizer 
tokenizer = RegexpTokenizer("[\w']+") 
text = "all the very best for your exam!!"
print(tokenizer.tokenize(text))