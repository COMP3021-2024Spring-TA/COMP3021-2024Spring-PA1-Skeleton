class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = dict()
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1

        for ch in s:
            if ch in dic and dic[ch] == 1:
                return ch
        return ' '