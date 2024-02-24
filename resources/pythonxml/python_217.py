class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line_cnt, last_cnt = 1, 0
        for ch in s:
            width = widths[ord(ch) - ord('a')]
            if last_cnt + width > 100:
                line_cnt += 1
                last_cnt = width
            else:
                last_cnt += width
                
        return [line_cnt, last_cnt]