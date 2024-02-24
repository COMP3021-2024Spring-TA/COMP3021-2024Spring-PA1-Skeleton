class CQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []


    def appendTail(self, value: int) -> None:
        self.inStack.append(value)


    def deleteHead(self) -> int:
        if len(self.outStack) == 0 and len(self.inStack) == 0:
            return -1
        if (len(self.outStack) == 0):
            while (len(self.inStack) != 0):
                self.outStack.append(self.inStack[-1])
                self.inStack.pop()
        top = self.outStack[-1]
        self.outStack.pop()
        return top