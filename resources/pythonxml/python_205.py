class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = collections.defaultdict(int)
        dp[p[0]] = 1
        max_len = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                max_len += 1
            else:
                max_len = 1
            dp[p[i]] = max(dp[p[i]], max_len)

        ans = 0
        for key, value in dp.items():
            ans += value
        return ans