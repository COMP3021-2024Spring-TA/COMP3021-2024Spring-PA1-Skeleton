class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        def generateTrees(start, end):
            if start > end:
                return [None]
            trees = []
            for i in range(start, end+1):
                left_trees = generateTrees(start, i - 1)
                right_trees = generateTrees(i + 1, end)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        curr_tree = TreeNode(i)
                        curr_tree.left = left_tree
                        curr_tree.right = right_tree
                        trees.append(curr_tree)
            return trees
        return generateTrees(1, n)