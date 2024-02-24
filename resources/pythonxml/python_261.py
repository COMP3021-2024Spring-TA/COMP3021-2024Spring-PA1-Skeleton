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
            if ch not in cur.children or not cur.children[ch].isEnd:
                return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd

class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)

        ans = ""
        for word in words:
            if trie_tree.search(word):
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word
        return ans