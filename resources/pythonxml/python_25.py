

def generateBadCharTable(p: str):
    m = len(p)
    bc_table = dict()
    
    for i in range(m - 1):                      
        bc_table[p[i]] = m - 1 - i              
    return bc_table