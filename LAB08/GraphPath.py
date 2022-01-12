from typing import List

from networkx.algorithms.bipartite.basic import color
from Graph import Graph,Vertex
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict
import math
class GraphPath:
    def __init__(self,graph:Graph,source:Vertex,destination:Vertex) -> None:
        self.graph = graph
        self.source = source
        self.destination = destination

    def BFS(self):
        visited = []
        out = ""
        queue = [[self.source]]

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = self.graph.adjacencies[node]
             
                for (neighbour,weight) in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == self.destination:
                        return new_path
                visited.append(node)

    def dijkstra(self):
        cost_array = {}
        visited = []
        path = {}
        path[self.source] = 0
        for (destination,weight) in self.graph.adjacencies[self.source]:
            cost_array[destination] = weight
        cost_array[self.destination] = math.inf
        parent_array = {}
        for (destination,weight) in self.graph.adjacencies[self.source]:
            parent_array[destination] = self.source
        parent_array[self.destination] = None
        v = self.lowest_cost(visited, cost_array)
        while(v is not None):
            c = cost_array.get(v)
            path[v]=c
            for (destination,weight) in self.graph.adjacencies[v]:
                nc = c + weight
                if cost_array[destination] > nc:
                    cost_array[destination] = nc
            visited.append(v)
            v = self.lowest_cost(visited, cost_array)
        return path

    def lowest_cost(self, visited: List[vars], cost_array: Dict[vars, vars]):
        lc = math.inf
        for vertex in cost_array:
            if (cost_array.get(vertex) < lc) and (vertex not in visited):
                lc = cost_array.get(vertex)
        for (vertex,value) in cost_array.items():  
            if value == lc:
                return vertex

    def shortest_path(self):
        out= ""
        for source in self.graph.adjacencies:
            for (destination,weight) in self.graph.adjacencies[source]:
                if(weight==None):
                    out=self.BFS()
                else:
                    out=self.dijkstra()
        return str(out)

    def show(self):
        G = nx.DiGraph()
        tuple = []
        for source in self.graph.adjacencies:
            for (destination,weight) in self.graph.adjacencies[source]:
                if weight==None:
                    tuple.append((source,destination))
                    G.add_edges_from(tuple)
                    SG = G.subgraph(self.BFS())
                else:
                    tuple.append((source,destination,weight))
                    G.add_weighted_edges_from(tuple)
                    SG = G.subgraph(self.dijkstra())
        pos=nx.spring_layout(G)
        nx.draw_networkx(G,pos,arrows=True,node_size=1000) 
        nx.draw_networkx(SG, pos=pos, node_color = 'r',edge_color='r',node_size=1000)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels) 
        plt.show()