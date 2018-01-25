def find_anagrams(words):
    by_sorted = {}
    for w in words:
        letters = [l for l in w]
        letters.sort()
        letters = ''.join(letters)
        if letters not in by_sorted:
            by_sorted[letters] = []
        by_sorted[letters].append(w)
    return by_sorted.values()

