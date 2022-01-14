from collections import defaultdict
from enum import Enum
from typing import Any,Optional,Dict,List
from Queue import Queue
import networkx as nx
import matplotlib.pyplot as plt



class EdgeType(Enum):
    directed = 1
    undirected = 0 
        
class Vertex:
    data:Any
    index: int
    def __init__(self,index:int,data:Any) -> None:
        self.data = data
        self.index = index

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]
    def __init__(self,source:Vertex,destination:Vertex,weight: Optional[float]) -> None:
        self.source=source
        self.destination=destination
        self.weight = weight

class Graph:
    adjacencies: Dict[Vertex,List[Edge]]
   

    def __init__(self,adjacencies=None) -> None:
        if(adjacencies == None):
            adjacencies={}
        self.adjacencies = adjacencies

    def create_vertex(self,index:int,data: Any) -> Vertex:
        vertex = Vertex(index,data)
        self.adjacencies[str(vertex.index)+":"+str(vertex.data)]=[]
        
    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge = Edge(source,destination,weight)
        self.adjacencies[edge.source].append((edge.destination,edge.weight))
         
    
    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
            edge = Edge(source,destination,weight)
            self.adjacencies[edge.source].append((edge.destination,edge.weight))
            self.adjacencies[edge.destination].append((edge.source,edge.weight))
           
            

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if(edge==1):
            self.add_directed_edge(source,destination,weight)
        elif(edge==2):
            self.add_undirected_edge(source,destination,weight)

    def BFT(self,vertex: Vertex):
        visited = []
        queue = Queue()
        visited.append(vertex)
        queue.enqueue(vertex)
        while queue:
            v = queue.dequeue()
            print(v,end=' ')
            for (neighbour,weight) in self.adjacencies[v]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.enqueue(neighbour)



    def dft_util(self,v, visited):
        visited.add(v)
        print(v, end=' ')
        for (neighbour,weight) in self.adjacencies[v]:
            if(neighbour not in visited):
                self.dft_util(neighbour,visited)

    def DFT(self,v: Vertex):
        visited = set()
        self.dft_util(v,visited)
    
    

    def show(self):
        G = nx.DiGraph()
        tuple = []
        for source in self.adjacencies:
            for (destination,weight) in self.adjacencies[source]:
                if weight==None:
                    tuple.append((source,destination))
                    G.add_edges_from(tuple)
                else:
                    tuple.append((source,destination,weight))
                    G.add_weighted_edges_from(tuple)
        pos=nx.spring_layout(G)
        nx.draw_networkx(G,pos,arrows=True,node_size=1000) 
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels) 
        plt.show()
        
      
    def __str__(self):
        dict = defaultdict(list)
        out = ""
        dict2 = {}
        for source in self.adjacencies:
            for(destination,weight) in self.adjacencies[source]:
                dict[source].append((destination,weight))
                dict[destination].append((source,weight))

        for key,value in dict.items():
                dict2[key]=set(value)
                
        
        for key in sorted(dict2.keys()) :
           out+=str(key)+"---->"+str(dict2[key])+"\n"
        return out
                
        
        