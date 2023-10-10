import re
text = "Regular expression are a powerful tool for text processing"

word_pattern = r'\w+'
words = re.findall(word_pattern,text)
print(words)