class EdgeNode:                                 
    def __init__(self, vi, vj, val):
        self.vi = vi                            
        self.vj = vj                            
        self.val = val                          
        
class Graph:                                    
    def __init__(self):
        self.edges = []                         
        
    
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)
            
    
    def add_edge(self, vi, vj, val):
        edge = EdgeNode(vi, vj, val)            
        self.edges.append(edge)                 
        
    
    def get_edge(self, vi, vj):
        for edge in self.edges:
            if vi == edge.vi and vj == edge.vj:
                val = edge.val
                return val
        return None
    
    
    def printGraph(self):
        for edge in self.edges:
            print(str(edge.vi) + ' - ' + str(edge.vj) + ' : ' + str(edge.val))
            
graph = Graph()
edges = [[1, 2, 5],[1, 5, 6],[2, 4, 7],[4, 3, 9],[3, 1, 2],[5, 6, 8],[6, 4, 3]]
graph.creatGraph(edges)
print(graph.get_edge(3, 4))
graph.printGraph()