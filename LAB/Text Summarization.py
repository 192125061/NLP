import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
def extractive_summarization(text, num_sentences=3):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    word_frequencies = {}
    for word in words:
        if word.lower() not in stop_words:
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += word_frequencies[word]
                else:
                    sentence_scores[sentence] = word_frequencies[word]
    summary = ' '.join([sentence for sentence, score in sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]])
    return summary
text = """
Natural language processing (NLP) is a field of computer science that focuses on the interaction between computers and humans through natural language. The ultimate objective of NLP is to read, decipher, understand, and make sense of human language in a way that is valuable. Text summarization is a subfield of NLP, which aims to shorten long texts while preserving their most important information. There are two main types of text summarization: extractive and abstractive. Extractive summarization involves selecting sentences or phrases directly from the source text, while abstractive summarization aims to generate new sentences that capture the key information. In this program, we will perform extractive text summarization using NLTK.
"""
summary = extractive_summarization(text, num_sentences=3)
print("Summary:")
print(summary)
