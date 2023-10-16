import random
from collections import defaultdict

# Sample text corpus
corpus = "The quick brown fox jumps over the lazy dog"

def generate_bigram_model(text):
    words = text.split()
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    model = defaultdict(list)

    for prev_word, next_word in bigrams:
        model[prev_word].append(next_word)

    return model

def generate_text(model, start_word, num_words):
    current_word = start_word
    generated_text = [current_word]

    for _ in range(num_words):
        next_word_options = model[current_word]
        if next_word_options:
            current_word = random.choice(next_word_options)
            generated_text.append(current_word)
        else:
            break

    return ' '.join(generated_text)

def main():
    bigram_model = generate_bigram_model(corpus)
    start_word = random.choice(list(bigram_model.keys()))
    generated_text = generate_text(bigram_model, start_word, num_words=10)
    
    print(f"Generated text starting with '{start_word}':")
    print(generated_text)

if __name__ == "__main__":
    main()