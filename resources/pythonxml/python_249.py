class Solution:
    def strToInt(self, str: str) -> int:
        num_str = ""
        positive = True
        start = 0

        s = str.lstrip()
        if not s:
            return 0

        if s[0] == '-':
            positive = False
            start = 1
        elif s[0] == '+':
            positive = True
            start = 1
        elif not s[0].isdigit():
            return 0

        for i in range(start, len(s)):
            if s[i].isdigit():
                num_str += s[i]
            else:
                break
        if not num_str:
            return 0
        num = int(num_str)
        if not positive:
            num = -num
            return max(num, -2 ** 31)
        else:
            return min(num, 2 ** 31 - 1)