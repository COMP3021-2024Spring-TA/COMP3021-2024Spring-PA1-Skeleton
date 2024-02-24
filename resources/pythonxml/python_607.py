class Solution:
    def totalMoney(self, n: int) -> int:
        week_cnt = n // 7
        weak_first_money = (1 + 7) * 7 // 2
        weak_last_money = weak_first_money + 7 * (week_cnt - 1)
        week_ans =  (weak_first_money + weak_last_money) * week_cnt // 2

        day_cnt = n % 7
        day_first_money = 1 + week_cnt
        day_last_money = day_first_money + day_cnt - 1
        day_ans = (day_first_money + day_last_money) * day_cnt // 2
        
        return week_ans + day_ans