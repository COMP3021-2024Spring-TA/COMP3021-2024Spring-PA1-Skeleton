class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        ans = ""

        idx = 0
        for i in range(len(s) - 1, -1, -1):
            ans += s[i]
            idx += 1
            if idx % 3 == 0 and i != 0:
                ans += "."

        return ''.join(reversed(ans))