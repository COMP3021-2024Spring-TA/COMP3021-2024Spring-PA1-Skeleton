class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def verify(left, right):
            if left >= right:
                return True
            index = left
            while postorder[index] < postorder[right]:
                index += 1
            mid = index
            while postorder[index] > postorder[right]:
                index += 1

            return index == right and verify(left, mid - 1) and verify(mid, right - 1)
        if len(postorder) <= 2:
            return True
        return verify(0, len(postorder) - 1)