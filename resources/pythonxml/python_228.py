class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False


    def insert(self, num: int, max_bit: int) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for i in range(max_bit, -1, -1):
            bit = num >> i & 1
            if bit not in cur.children:
                cur.children[bit] = Trie()
            cur = cur.children[bit]
        cur.isEnd = True

    def search(self, num: int, max_bit: int) -> int:
        """
        Returns if the word is in the trie.
        """
        cur = self
        res = 0
        for i in range(max_bit, -1, -1):
            bit = num >> i & 1
            if 1 - bit not in cur.children:
                res = res * 2
                cur = cur.children[bit]
            else:
                res = res * 2 + 1
                cur = cur.children[1 - bit]
        return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie_tree = Trie()
        max_bit = len(format(max(nums), 'b')) - 1
        ans = 0
        for num in nums:
            trie_tree.insert(num, max_bit)
            ans = max(ans, trie_tree.search(num, max_bit))
            
        return ans