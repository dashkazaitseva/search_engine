from collections import Counter
from typing import List
from parser_file import read_phrases, get_best_adds
import copy


PHRASES = read_phrases()
WORDS = Counter([word for phrase in PHRASES for word in phrase.split()])
BEST_ADDS = get_best_adds(PHRASES)


def probability_of_word(word, number=sum(WORDS.values())):
    return WORDS[word] / number


def correction(word):
    return max(candidates(word), key=probability_of_word)


def candidates(word):
    return known([word]) or known(edits(word)) or known(double_edits(word)) or [word]


def known(words):
    return set(w for w in words if w in WORDS)


def edits(word):
    letters = 'abcdefghijklmnopqrstuvwxyz' if 'a' <= list(WORDS.keys())[0][0] <= 'z' \
        else 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def double_edits(word):
    return (e2 for e1 in edits(word) for e2 in edits(e1))


def get_next_word(s: List[List[str]], number_to_get: int) -> List[List[str]]:
    if not number_to_get:
        return []
    new_queries = []
    for query in s:
        for addition in BEST_ADDS[query[-1]]:
            new_queries.append(copy.deepcopy(query) + [addition])
    return s + get_next_word(new_queries, number_to_get - 1)


def query_significant(query: str) -> float:
    """order will be: long from base, short from base, short not from base, long not from base"""
    q_helper = query.split()
    if query in PHRASES:
        return 1 / len(q_helper) / len(q_helper[-1])
    return 100 * len(q_helper) / len(q_helper[-1])


def sort_queries(queries: List[str]) -> List[str]:
    queries = [" ".join(query) for query in queries]
    queries.sort(key=query_significant)

    return queries


def get_best_queries(s: str, number_of_queries: int) -> List[str]:
    queries = get_next_word([[s]], 5)
    queries = sort_queries(queries)

    return queries[:number_of_queries]


def main():
    while True:
        s = correction(input())
        suggest = get_best_queries(s, 5)
        print("\n".join(suggest))
    pass


if __name__ == '__main__':
    main()
