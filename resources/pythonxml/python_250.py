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
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)

        size = len(s)
        bold_left, bold_right = -1, -1
        ans = ""
        for i in range(size):
            cur = trie_tree
            if s[i] in cur.children:
                bold_left = i
                while bold_left < size and s[bold_left] in cur.children:
                    cur = cur.children[s[bold_left]]
                    bold_left += 1
                    if cur.isEnd:
                        if bold_right == -1:
                            ans += "<b>"
                        bold_right = max(bold_left, bold_right)
            if i == bold_right:
                ans += "</b>"
                bold_right = -1
            ans += s[i]
        if bold_right >= 0:
            ans += "</b>"
        return ans