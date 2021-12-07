from enum import Enum
from typing import Any,Optional,Dict,List,Callable
from Queue import Queue

class EdgeType(Enum):
    directed = 1
    undirected = 0 
        
class Vertex:
    data:Any
    index: int

    def __init__(self,data:Any,index: int) -> None:
        self.data = data
        self.index = index
        
class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

class Graph:
    adjacencies: Dict[Vertex,List[Edge]]

    def __init__(self,adjacencies=None) -> None:
        if(adjacencies == None):
            adjacencies={}
        self.adjacencies = adjacencies

    def create_vertex(self,index:int, data: Any) -> Vertex:
        vertex = Vertex(data,index)
        self.adjacencies[str(index)+": "+str(data)]=[]

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(destination)
        if(weight is not None):
            self.adjacencies[source].append(weight)
    
    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(destination)
        self.adjacencies[destination].append(source)
        if(weight is not None):
            self.adjacencies[source].append(weight)
            self.adjacencies[destination].append(weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if(edge==1):
            self.add_directed_edge(source,destination,weight)
        elif(edge==2):
            self.add_undirected_edge(source,destination,weight)

    def BTS(self,vertex: Vertex):
        visited = []
        queue = Queue()
        visited.append(vertex)
        queue.enqueue(vertex)
        while queue:
            v = queue.dequeue()
            print(v,end=' ')
            for neighbour in self.adjacencies[v]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.enqueue(neighbour)

    def dfs_util(self,v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.adjacencies[v]:
            if(neighbour not in visited):
                self.dfs_util(neighbour,visited)

    def DFS(self,v: Vertex):
        visited = set()
        self.dfs_util(v,visited)
   
    def show(self):
        for key, value in self.adjacencies.items():
            print(key, '---->', value)


    def __generate_edges(self):
        edges = []
        for vertex in self.adjacencies:
            for neighbour in self.adjacencies[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self)->str:
        res = "vertices: "
        for k in self.adjacencies:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " \n"
        return res
        

            
       
graph = Graph()
graph.create_vertex(0,"v0")
graph.create_vertex(1,"v1")
graph.create_vertex(2,"v2")
graph.create_vertex(3,"v3")
graph.create_vertex(4,"v4")
graph.create_vertex(5,"v5")
graph.add(1,"0: v0","1: v1")
graph.add(1,"0: v0","5: v5")
graph.add(1,"2: v2","3: v3")
graph.add(1,"2: v2","1: v1")
graph.add(1,"3: v3","4: v4")
graph.add(1,"4: v4","1: v1")
graph.add(1,"4: v4","5: v5")
graph.add(1,"5: v5","1: v1")
graph.add(1,"5: v5","2: v2")
print(graph)



