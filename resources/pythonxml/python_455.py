class Solution:
    def createBinaryTree(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left >= right:
            return None
        max_value_index = left
        for i in range(left + 1, right):
            if nums[i] > nums[max_value_index]:
                max_value_index = i

        root = TreeNode(nums[max_value_index])
        root.left = self.createBinaryTree(nums, left, max_value_index)
        root.right = self.createBinaryTree(nums, max_value_index + 1, right)

        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.createBinaryTree(nums, 0, len(nums))