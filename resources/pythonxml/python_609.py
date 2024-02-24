class Solution:
    def shellSort(self, arr):
        size = len(arr)
        gap = size // 2

        while gap > 0:
            for i in range(gap, size):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] < temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap = gap // 2
        return arr

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        nums = score.copy()
        nums = self.shellSort(nums)
        score_map = dict()
        for i in range(len(nums)):
            score_map[nums[i]] = i + 1

        res = []
        for i in range(len(score)):
            if score[i] == nums[0]:
                res.append("Gold Medal")
            elif score[i] == nums[1]:
                res.append("Silver Medal")
            elif score[i] == nums[2]:
                res.append("Bronze Medal")
            else:
                res.append(str(score_map[score[i]]))
        return res