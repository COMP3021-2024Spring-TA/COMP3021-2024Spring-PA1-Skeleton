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

        def dfs(index, node) -> bool:
            if index == len(word):
                return node.isEnd

            ch = word[index]
            if ch == '.':
                for child in node.children.values():
                    if child is not None and dfs(index + 1, child):
                        return True
            else:
                if ch not in node.children:
                    return False
                child = node.children[ch]
                if child is not None and dfs(index + 1, child):
                    return True
            return False

        return dfs(0, self)


class WordDictionary:

    def __init__(self):
        self.trie_tree = Trie()


    def addWord(self, word: str) -> None:
        self.trie_tree.insert(word)


    def search(self, word: str) -> bool:
        return self.trie_tree.search(word)