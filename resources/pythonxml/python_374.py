class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []
        """
        Initialize your data structure here.
        """


    def push(self, x: int) -> None:
        self.inStack.append(x)
        """
        Push element x to the back of queue.
        """


    def pop(self) -> int:
        if(len(self.outStack) == 0):
            while(len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        self.outStack.pop()
        return top
        """
        Removes the element from in front of queue and returns that element.
        """


    def peek(self) -> int:
        if (len(self.outStack) == 0):
            while (len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        return top
        """
        Get the front element.
        """


    def empty(self) -> bool:
        return len(self.outStack) == 0 and len(self.inStack) == 0
        """
        Returns whether the queue is empty.
        """