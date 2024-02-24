class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.word = ""


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
        cur.word = word


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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)

        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        cols = len(board[0])

        def dfs(cur, row, col):
            ch = board[row][col]
            if ch not in cur.children:
                return

            cur = cur.children[ch]
            if cur.isEnd:
                ans.add(cur.word)

            board[row][col] = "#"
            for direct in directs:
                new_row = row + direct[0]
                new_col = col + direct[1]
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    dfs(cur, new_row, new_col)
            board[row][col] = ch

        ans = set()
        for i in range(rows):
            for j in range(cols):
                dfs(trie_tree, i, j)

        return list(ans)