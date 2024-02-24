class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        ans = 0
        for i in range(1, n + 1):
            flag = False
            num = i
            while num:
                digit = num % 10
                num //= 10
                if check[digit] == 1:
                    flag = True
                elif check[digit] == -1:
                    flag = False
                    break
            if flag:
                ans += 1
            	
        return ans