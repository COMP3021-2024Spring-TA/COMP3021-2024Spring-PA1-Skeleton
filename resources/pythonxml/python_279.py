class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)
        i, j = 0, 0
        while i < size_s and j < size_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == size_s