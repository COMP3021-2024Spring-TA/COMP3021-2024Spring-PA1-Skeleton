class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        if numerator ^ denominator < 0:
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        numerator %= denominator
        if numerator == 0:
            return ''.join(res)
        res.append('.')

        record = dict()
        while numerator:
            if numerator not in record:
                record[numerator] = len(res)
                numerator *= 10
                res.append(str(numerator // denominator))
                numerator %= denominator
            else:
                res.insert(record[numerator], '(')
                res.append(')')
                break
        return ''.join(res)