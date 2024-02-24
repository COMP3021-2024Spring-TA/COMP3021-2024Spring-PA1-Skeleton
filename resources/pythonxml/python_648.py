class Solution:
    def decodeString(self, s: str) -> str:
        stack1 = []
        stack2 = []
        num = 0
        res = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack1.append(res)
                stack2.append(num)
                res = ""
                num = 0
            elif ch == ']':
                cur_res = stack1.pop()
                cur_num = stack2.pop()
                res = cur_res + res * cur_num
            else:
                res += ch
        return res