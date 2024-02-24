class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        size = len(nestedList)
        for i in range(size - 1, -1, -1):
            self.stack.append(nestedList[i])
        
    
    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()
        
    
    def hasNext(self) -> bool:
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])
        return False