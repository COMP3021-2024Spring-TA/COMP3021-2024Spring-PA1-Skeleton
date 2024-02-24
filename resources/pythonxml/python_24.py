

def generateBadCharTable(p: str):
    bc_table = dict()
    
    for i in range(len(p)):
        bc_table[p[i]] = i                          
    return bc_table