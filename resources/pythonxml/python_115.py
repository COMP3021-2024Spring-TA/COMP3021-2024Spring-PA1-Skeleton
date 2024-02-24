def find(self, x):                              
    while self.fa[x] != x:                      
        self.fa[x] = self.fa[self.fa[x]]        
        x = self.fa[x]
    return x                                    