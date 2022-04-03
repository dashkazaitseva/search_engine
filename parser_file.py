from collections import defaultdict
from collections import Counter


def read_phrases():
    phrases = []
    with open("phrases.txt", encoding="UTF8") as input_phrases:
        for line in input_phrases:
            phrases.append(line.strip().lower())
    return phrases


def get_best_adds(phrases) -> dict:
    word_after = defaultdict(list)
    for phrase in phrases:
        phrase = phrase.split()
        for i in range(len(phrase) - 1):
            word_after[phrase[i]].append(phrase[i + 1])
    for word in word_after:
        word_after[word] = Counter(word_after[word])
        word_after[word] = word_after[word].most_common(3)
        word_after[word] = [addition[0] for addition in word_after[word]]

    return word_after
