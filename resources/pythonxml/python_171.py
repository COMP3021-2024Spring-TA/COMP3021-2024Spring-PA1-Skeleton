class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xyCnt, yxCnt = 0, 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x':
                xyCnt += 1
            else:
                yxCnt += 1

        if (xyCnt + yxCnt) & 1:
            return -1
        return xyCnt // 2 + yxCnt // 2 + (xyCnt % 2 * 2)