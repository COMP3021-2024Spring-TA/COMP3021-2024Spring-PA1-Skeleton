class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        cnts = Counter()

        word = ""
        for ch in paragraph:
            if ch.isalpha():
                word += ch.lower()
            else:
                if word and word not in banned_set:
                    cnts[word] += 1
                word = ""
        if word and word not in banned_set:
            cnts[word] += 1

        max_cnt, ans = 0, ""
        for word, cnt in cnts.items():
            if cnt > max_cnt:
                max_cnt = cnt
                ans = word
        
        return ans