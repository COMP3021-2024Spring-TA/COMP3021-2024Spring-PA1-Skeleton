

def generateBadCharTable(p: str):
    m = len(p)
    bc_table = dict()
    
    for i in range(m):                      
        bc_table[p[i]] = m - i              
    return bc_table