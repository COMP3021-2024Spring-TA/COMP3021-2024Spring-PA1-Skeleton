class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = size
        self.sum = 0


    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.queue.append(val)
        else:
            if self.queue:
                self.sum -= self.queue[0]
                self.queue.pop(0)
            self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)