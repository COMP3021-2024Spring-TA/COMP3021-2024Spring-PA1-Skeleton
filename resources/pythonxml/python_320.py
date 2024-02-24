class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = dict()
        word_dict = dict()
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            p = pattern[i]
            word = words[i]
            if p in pattern_dict and pattern_dict[p] != word:
                return False
            if word in word_dict and word_dict[word] != p:
                return False
            pattern_dict[p] = word
            word_dict[word] = p
        return True