
def search(self, word: str) -> bool:
    cur = self.root
    for ch in word:                         
        if ch not in cur.children:          
            return False                    
        cur = cur.children[ch]              

    return cur is not None and cur.isEnd    