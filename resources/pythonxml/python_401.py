class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n_list = list(str(n))
        size = len(n_list)
        start_i = size
        for i in range(size - 1, 0, -1):
            if n_list[i - 1] > n_list[i]:
                start_i = i
                n_list[i - 1] = chr(ord(n_list[i - 1]) - 1)

        for i in range(start_i, size, 1):
            n_list[i] = '9'
        res = int(''.join(n_list))
        return res