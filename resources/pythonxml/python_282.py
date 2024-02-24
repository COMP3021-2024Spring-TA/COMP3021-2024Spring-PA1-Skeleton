class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        flag = -1
        for key in counter:
            if flag == -1:
                flag = counter[key]
            else:
                if flag != counter[key]:
                    return False
        return True