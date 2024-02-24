class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            top = self.stack.pop()
            span += top[1]
        self.stack.append([price, span])
        return span