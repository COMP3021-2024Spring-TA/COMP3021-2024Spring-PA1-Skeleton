class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_map = dict()
        for i in range(len(s)):
            letter_map[s[i]] = i
        res = []
        start, end = 0, 0
        for i in range(len(s)):
            end = max(end, letter_map[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res