class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_dict = dict()
        len1 = len(list1)
        len2 = len(list2)
        for i in range(len1):
            list1_dict[list1[i]] = i

        min_sum = len1 + len2
        res = []
        for i in range(len2):
            if list2[i] in list1_dict:
                sum = i + list1_dict[list2[i]]
                if sum < min_sum:
                    res = [list2[i]]
                    min_sum = sum
                elif sum == min_sum:
                    res.append(list2[i])
        return res