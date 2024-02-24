class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(parenthesis, symbol, index):
            if n * 2 == index:
                if symbol == 0:
                    parentheses.append(parenthesis)
            else:
                if symbol < n:
                    backtrack(parenthesis + '(', symbol + 1, index + 1)
                if symbol > 0:
                    backtrack(parenthesis + ')', symbol - 1, index + 1)

        parentheses = list()
        backtrack("", 0, 0)
        return parentheses