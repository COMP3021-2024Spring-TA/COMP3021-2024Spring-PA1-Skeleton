class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray = []
        binary = 0
        while binary < (1 << n):
            gray.append(binary ^ binary >> 1)
            binary += 1
        return gray