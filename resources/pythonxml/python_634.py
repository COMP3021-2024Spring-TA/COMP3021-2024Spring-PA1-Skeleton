class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if (len(self.outStack) == 0):
            while (len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        self.outStack.pop()
        return top


    def peek(self) -> int:
        """
        Get the front element.
        """
        if (len(self.outStack) == 0):
            while (len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        return top


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.outStack) == 0 and len(self.inStack) == 0