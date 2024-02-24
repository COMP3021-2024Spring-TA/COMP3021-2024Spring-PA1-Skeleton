class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        a &= MASK
        b &= MASK
        while b:
            carry = ((a & b) << 1) & MASK
            a ^= b
            b = carry
        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)