class VertexNode:                               
    def __init__(self, vi):
        self.vi = vi                            
        self.adj_edges = dict()                 
        
class Graph:
    def __init__(self):
        self.vertices = dict()                   
    
    
    def creatGraph(self, edges=[]):
        for vi, vj, val in edges:
            self.add_edge(vi, vj, val)
    
    
    def add_vertex(self, vi):
        vertex = VertexNode(vi)
        self.vertices[vi] = vertex
    
    
    def add_edge(self, vi, vj, val):        
        if vi not in self.vertices:
            self.add_vertex(vi)
        if vj not in self.vertices:
            self.add_vertex(vj)
        
        self.vertices[vi].adj_edges[vj] = val
        
    
    def get_edge(self, vi, vj):
        if vi in self.vertices and vj in self.vertices[vi].adj_edges:
            return self.vertices[vi].adj_edges[vj]
        return None
    
    
    def printGraph(self):
        for vi in self.vertices:
            for vj in self.vertices[vi].adj_edges:
                print(str(vi) + ' - ' + str(vj) + ' : ' + str(self.vertices[vi].adj_edges[vj]))


graph = Graph()
edges = [[1, 2, 5],[1, 5, 6],[2, 4, 7],[4, 3, 9],[3, 1, 2],[5, 6, 8],[6, 4, 3]]
graph.creatGraph(edges)
print(graph.get_edge(3, 4))
graph.printGraph()