class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_counts = dict()


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for number in self.num_counts.keys():
            number2 = value - number
            if number == number2:
                if self.num_counts[number] > 1:
                    return True
            else:
                if number2 in self.num_counts:
                    return True
        return False