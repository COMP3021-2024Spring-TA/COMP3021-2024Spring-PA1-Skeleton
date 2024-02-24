class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        left_1, left_2 = len(s) - 1, len(t) - 1
        sign_1, sign_2 = 0, 0
        while left_1 >= 0 or left_2 >= 0:
            while left_1 >= 0:
                if s[left_1] == '#':
                    sign_1 += 1
                    left_1 -= 1
                elif sign_1 > 0:
                    sign_1 -= 1
                    left_1 -= 1
                else:
                    break

            while left_2 >= 0:
                if t[left_2] == '#':
                    sign_2 += 1
                    left_2 -= 1
                elif sign_2 > 0:
                    sign_2 -= 1
                    left_2 -= 1
                else:
                    break

            if left_1 < 0 and left_2 < 0:
                return True
            if left_1 >= 0 and left_2 < 0:
                return False
            if left_1 < 0 and left_2 >= 0:
                return False
            if s[left_1] != t[left_2]:
                return False

            left_1 -= 1
            left_2 -= 1

        return True