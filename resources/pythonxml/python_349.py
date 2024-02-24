class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for ch in s:
            if ch == ' ':
                res.append("%20")
            else:
                res.append(ch)
        return "".join(res)