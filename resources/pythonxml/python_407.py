class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increments = []
        self.size = 0


    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.stack.append(x)
            self.increments.append(0)
            self.size += 1


    def pop(self) -> int:
        if self.size == 0:
            return -1
        if self.size >= 2:
            self.increments[-2] += self.increments[-1]
        self.size -= 1
        
        val = self.stack.pop() + self.increments.pop()
        return val


    def increment(self, k: int, val: int) -> None:
        if self.increments:
            self.increments[min(k, self.size) - 1] += val







