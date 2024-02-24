class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        table = dict()
        for word in s1.split(' '):
            if word not in table:
                table[word] = 1
            else:
                table[word] += 1
        
        for word in s2.split(' '):
            if word not in table:
                table[word] = 1
            else:
                table[word] += 1
       
        res = []
        for word in table:
            if table[word] == 1:
                res.append(word)
        
        return res