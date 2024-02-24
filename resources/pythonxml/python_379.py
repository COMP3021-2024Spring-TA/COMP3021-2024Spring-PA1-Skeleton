class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(ch, x):
            return chr(ord(ch) + x) 
        
        res = list(s)
        for i in range(1, len(s), 2):
            res[i] = shift(res[i - 1], int(res[i]))
        
        return "".join(res)