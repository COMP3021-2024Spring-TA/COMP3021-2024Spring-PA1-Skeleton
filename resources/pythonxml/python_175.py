class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left_1, left_2 = 0, 0

        while left_1 < len(name) and left_2 < len(typed):
            if name[left_1] == typed[left_2]:
                left_1 += 1
                left_2 += 1
            elif left_2 > 0 and typed[left_2 - 1] == typed[left_2]:
                left_2 += 1
            else:
                return False
        while 0 < left_2 < len(typed) and typed[left_2] == typed[left_2 - 1]:
            left_2 += 1

        if left_1 == len(name) and left_2 == len(typed):
            return True
        else:
            return False