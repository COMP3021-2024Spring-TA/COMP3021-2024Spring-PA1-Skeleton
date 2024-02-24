
def startsWith(self, prefix: str) -> bool:
    cur = self.root
    for ch in prefix:                       
        if ch not in cur.children:          
            return False                    
        cur = cur.children[ch]              
    return cur is not None                  