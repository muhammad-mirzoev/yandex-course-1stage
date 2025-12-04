class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence: str):
        words_in_sentence = sentence.split()
        self.words.extend(words_in_sentence)

    def shortest_words(self):
        if not self.words:
            return []

        min_length = min(len(word) for word in self.words)
        shortest = [word for word in self.words if len(word) == min_length]
        shortest.sort()
        return shortest

    def longest_words(self):
        if not self.words:
            return []

        max_length = max(len(word) for word in self.words)
        longest = {word for word in self.words if len(word) == max_length}
        longest = sorted(longest)
        return longest