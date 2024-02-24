class Solution:
    def build(self, s: str):
        stack = []
        for ch in s:
            if ch != '#':
                stack.append(ch)
            elif stack:
                stack.pop()
        return stack
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.build(s) == self.build(t)