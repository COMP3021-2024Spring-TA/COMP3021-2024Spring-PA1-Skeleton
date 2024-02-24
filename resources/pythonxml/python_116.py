def find(self, x):                              
    if self.fa[x] != x:                         
        self.fa[x] = self.find(self.fa[x])      
    return self.fa[x]