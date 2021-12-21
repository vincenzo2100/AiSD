from collections import defaultdict
from enum import Enum
from typing import Any,Optional,Dict,List,Callable

from networkx.algorithms.shortest_paths import weighted
from Queue import Queue
import networkx as nx
import matplotlib.pyplot as plt

class EdgeType(Enum):
    directed = 1
    undirected = 0 
        
class Vertex:
    data:Any
    index: int
    def __init__(self,data:Any) -> None:
        self.data = data

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

class Graph:
    adjacencies: Dict[Vertex,List[Edge]]
    draw_directed: List = []
    draw_undirected: List = []

    def __init__(self,adjacencies=None) -> None:
        if(adjacencies == None):
            adjacencies={}
        self.adjacencies = adjacencies

    def create_vertex(self,data: Any) -> Vertex:
        vertex = Vertex(data)
        self.adjacencies[vertex.data]=[]
        
    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(destination)
        if(weight is not None):
            self.adjacencies[source].append(weight)
        self.draw_directed.append((source,destination,weight))
    
    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
            self.adjacencies[source].append(destination)
            self.adjacencies[destination].append(source)
            if(weight is not None):
                self.adjacencies[source].append(weight)
                self.adjacencies[destination].append(weight)
            self.draw_undirected.append((source,destination,weight))
            self.draw_undirected.append((destination,source,weight))

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
        if(self.draw_directed):
            G = nx.DiGraph()
            G.add_weighted_edges_from(self.draw_directed)
            pos=nx.spring_layout(G)
            nx.draw_networkx(G,pos,arrows=True)
            labels = nx.get_edge_attributes(G,'weight')
            nx.draw_networkx_edge_labels(G,pos,edge_labels=labels) 
            plt.show()
        if(self.draw_undirected):
            G = nx.Graph()
            G.add_weighted_edges_from(self.draw_undirected)
            pos=nx.spring_layout(G)
            nx.draw_networkx(G,pos)
            labels = nx.get_edge_attributes(G,'weight')
            nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
            plt.show()   
        
    
    def __str__(self):
        edges = []
        for vertex in self.adjacencies:
            for neighbour in self.adjacencies[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append((vertex, neighbour))
        dictionary = defaultdict(list)
        dictionary2 = {}
        for k, v in edges:
            dictionary[k].append(v)

        for key,value in dictionary.items():
            dictionary2[key] = set(value)
        out = ""
        for key, value in dictionary2.items():
            out+=str(key)+'---->'+str(value)+"\n"
        return out
        
        