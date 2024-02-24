class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.count = 0


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
        cur.count += 1


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        if cur and cur.isEnd:
            return cur.count
        return 0

class WordsFrequency:

    def __init__(self, book: List[str]):
        self.tire_tree = Trie()
        for word in book:
            self.tire_tree.insert(word)


    def get(self, word: str) -> int:
        return self.tire_tree.search(word)