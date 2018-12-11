"""
Write a function, which returns top 10 words from the "Pan Tadeusz" text.

[(word, number_of_occurrences),
]

Normalize word before counting:
- remove punctuation characters
- lowercase word

Example: 'gdzie?' and 'Gdzie' are the same words.
Text is available in data/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt
"""
from collections import Counter
import re


def get_top_words(file_path, how_many, min_word_length=1, max_word_length=100):
    word_pattern = re.compile("(\w+)")
    counter = Counter()
    with open(file_path) as f:
        for line in f:
            for word in line.split():
                m = word_pattern.search(word)
                if m:
                    word = m.group(1).lower()
                    if min_word_length <= len(word) <= max_word_length:
                        counter[word] += 1

    return [item for item in counter.most_common(how_many)]


print(get_top_words("../data/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt", 10, 5))
