class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        tree_dict = dict()
        res = []
        def preorder(node):
            if not node:
                return '#'
            sub_tree = str(node.val) + ',' + preorder(node.left) + ',' + preorder(node.right)
            if sub_tree in tree_dict:
                tree_dict[sub_tree] += 1
            else:
                tree_dict[sub_tree] = 1
            if tree_dict[sub_tree] == 2:
                res.append(node)
            return sub_tree
        preorder(root)
        return res