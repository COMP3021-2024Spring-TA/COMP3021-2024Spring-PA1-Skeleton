





class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nums1 = self.inorderTraversal(root1)
        nums2 = self.inorderTraversal(root2)
        nums = []
        index1, index2 = 0, 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                nums.append(nums1[index1])
                index1 += 1
            else:
                nums.append(nums2[index2])
                index2 += 1
        
        while index1 < len(nums1):
            nums.append(nums1[index1])
            index1 += 1
    
        while index2 < len(nums2):
            nums.append(nums2[index2])
            index2 += 1
        
        return nums