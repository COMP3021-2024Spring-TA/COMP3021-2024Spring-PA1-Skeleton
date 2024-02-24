class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        path = queryIP.split('.')
        if len(path) == 4:
            for sub in path:
                if not sub or not sub.isdecimal():
                    return "Neither"
                if sub[0] == '0' and len(sub) != 1:
                    return "Neither"
                if int(sub) > 255:
                    return "Neither"
            return "IPv4"

        path = queryIP.split(':')
        if len(path) == 8:
            valid = "0123456789abcdefABCDEF"
            for sub in path:
                if not sub:
                    return "Neither"
                if len(sub) > 4:
                    return "Neither"
                for digit in sub:
                    if digit not in valid:
                        return "Neither"
            return "IPv6"

        return "Neither"