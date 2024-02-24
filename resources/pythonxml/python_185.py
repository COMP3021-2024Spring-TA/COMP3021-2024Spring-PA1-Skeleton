class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.value = 0


    def insert(self, word: str, value: int) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True
        cur.value = value


    def search(self, word: str) -> int:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return self.dfs(cur)

    def dfs(self, root) -> int:
        if not root:
            return 0
        res = root.value
        for node in root.children.values():
            res += self.dfs(node)
        return res



class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_tree = Trie()


    def insert(self, key: str, val: int) -> None:
        self.trie_tree.insert(key, val)


    def sum(self, prefix: str) -> int:
        return self.trie_tree.search(prefix)