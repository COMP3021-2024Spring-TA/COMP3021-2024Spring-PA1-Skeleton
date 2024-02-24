class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber:
            columnNumber -= 1
            s = chr(65 + columnNumber % 26) + s
            columnNumber //= 26
        return s