class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        self.shuffle_nums = self.nums.copy()
        for i in range(len(self.shuffle_nums)):
            swap_index = random.randrange(i, len(self.shuffle_nums))
            self.shuffle_nums[i], self.shuffle_nums[swap_index] = self.shuffle_nums[swap_index], self.shuffle_nums[i]
        return self.shuffle_nums