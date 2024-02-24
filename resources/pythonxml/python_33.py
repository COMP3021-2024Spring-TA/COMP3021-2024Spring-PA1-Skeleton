
def insert(self, word: str) -> None:
    cur = self.root
    for ch in word:                         
        if ch not in cur.children:          
            cur.children[ch] = Node()       
        cur = cur.children[ch]              
    cur.isEnd = True                        