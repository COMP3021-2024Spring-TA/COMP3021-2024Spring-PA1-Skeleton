class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    class Node:
        def __init__(self, x):
            self.val = x
            self.min = x

    def push(self, val: int) -> None:
        node = self.Node(val)
        if len(self.stack) == 0:
            self.stack.append(node)
        else:
            topNode = self.stack[-1]
            if node.min > topNode.min:
                node.min = topNode.min

            self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min