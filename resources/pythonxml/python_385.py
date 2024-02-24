class Solution:
    def longestPalindrome(self, s: str) -> int:
        word_dict = dict()
        for ch in s:
            if ch in word_dict:
                word_dict[ch] += 1
            else:
                word_dict[ch] = 1

        ans = 0
        flag = False
        for value in word_dict.values():
            ans += value // 2 * 2
            if value % 2 == 1:
                flag = True

        if flag:
            ans += 1

        return ans