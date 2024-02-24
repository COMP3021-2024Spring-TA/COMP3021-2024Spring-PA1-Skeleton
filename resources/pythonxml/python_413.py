class Solution:
    def getNext(self, n: int):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum


    def isHappy(self, n: int) -> bool:
        num_set = set()
        while n != 1 and n not in num_set:
            num_set.add(n)
            n = self.getNext(n)
        return n == 1