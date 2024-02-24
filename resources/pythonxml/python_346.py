class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ord(ch) > 96:
                if ch not in cur.children:
                    continue
            else:
                if ch not in cur.children:
                    return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie_tree = Trie()
        trie_tree.insert(pattern)
        res = []
        for query in queries:
            res.append(trie_tree.search(query))
        return res