class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.words = list()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
            if len(cur.words) < 3:
                cur.words.append(word)
        cur.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        res = []
        flag = False
        for ch in word:
            if flag or ch not in cur.children:
                res.append([])
                flag = True
            else:
                cur = cur.children[ch]
                res.append(cur.words)

        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie_tree = Trie()
        for product in products:
            trie_tree.insert(product)

        return trie_tree.search(searchWord)