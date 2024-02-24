class Solution:
    def inOrder(self, root, nums):
        if not root:
            return
        self.inOrder(root.left, nums)
        nums.append(root.val)
        self.inOrder(root.right, nums)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        self.inOrder(root, nums)
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                return True
            elif sum < k:
                left += 1
            else:
                right -= 1
        return False