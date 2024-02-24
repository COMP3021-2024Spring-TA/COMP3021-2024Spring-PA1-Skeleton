class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for _ in range(1, n):
            s = ""
            start = 0
            for i in range(len(ans)):
                if ans[i] != ans[start]:
                    s += str(i-start) + ans[start]
                    start = i
            s += str(len(ans)-start) + ans[start]
            ans = s
        return ans