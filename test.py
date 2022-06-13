def anagrams(word: str, words: list):
    return [w for w in words if sorted(w) == sorted(word)]
