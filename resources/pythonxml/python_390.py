class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == t:
            return False
        strDict = dict()
        for ch in s:
            if ch in strDict:
                strDict[ch] += 1
            else:
                strDict[ch] = 1
        for ch in t:
            if ch in strDict:
                strDict[ch] -= 1
                if strDict[ch] < 0:
                    return False
            else:
                return False
        return True