class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []

        index, num = 0, 0
        pre_level, cur_level = 0, 0

        size = len(traversal)
        while index < size and traversal[index] != '-':
            num = num * 10 + ord(traversal[index]) - ord('0')
            index += 1

        root = TreeNode(num)
        stack.append(root)

        while index < size:
            if traversal[index] == '-':
                cur_level += 1
                index += 1
            else:
                num = 0
                while index < size and traversal[index] != '-':
                    num = num * 10 + ord(traversal[index]) - ord('0')
                    index += 1

                if cur_level > pre_level:
                    node = stack.pop()
                    node.left = TreeNode(num)
                    stack.append(node)
                    stack.append(node.left)
                    pre_level = cur_level
                    cur_level = 0
                else:
                    while len(stack) > cur_level:
                        stack.pop()
                    node = stack.pop()
                    node.right = TreeNode(num)
                    stack.append(node)
                    stack.append(node.right)
                    pre_level = cur_level
                    cur_level = 0
        return root