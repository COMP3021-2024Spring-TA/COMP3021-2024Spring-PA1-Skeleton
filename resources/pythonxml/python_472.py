class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushQueue = collections.deque()
        self.popQueue = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.pushQueue.append(x)
        while self.popQueue:
           self.pushQueue.append(self.popQueue.popleft())
        self.pushQueue, self.popQueue = self.popQueue, self.pushQueue

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.popQueue.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.popQueue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.popQueue







