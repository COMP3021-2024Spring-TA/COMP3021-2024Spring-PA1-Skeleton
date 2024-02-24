class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for i in range(1, target // 2 + 1):
            cur_sum = 0
            for j in range(i, target):
                cur_sum += j
                if cur_sum > target:
                    break
                if cur_sum == target:
                    cur_res = []
                    for k in range(i, j + 1):
                        cur_res.append(k)
                    res.append(cur_res)
                    break
        return res