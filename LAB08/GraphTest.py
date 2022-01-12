from Graph import Graph
from GraphPath import GraphPath

graph = Graph()
graph.create_vertex(0,"A")
graph.create_vertex(1,"B")
graph.create_vertex(2,"C")
graph.create_vertex(3,"D")
graph.add(1,"0:A","1:B",30)
graph.add(1,"0:A","2:C",10)
graph.add(1,"1:B","3:D",2)
graph.add(1,"2:C","1:B",5)
graph.add(1,"2:C","3:D",9)
path = GraphPath(graph,"0:A","3:D")

graph2 = Graph()
graph2.create_vertex(0,"v0")
graph2.create_vertex(1,"v1")
graph2.create_vertex(2,"v2")
graph2.create_vertex(3,"v3")
graph2.create_vertex(4,"v4")
graph2.create_vertex(5,"v5")
graph2.add(1,"0:v0","1:v1")
graph2.add(1,"0:v0","5:v5")
graph2.add(1,"3:v3","4:v4")
graph2.add(1,"4:v4","1:v1")
graph2.add(1,"4:v4","5:v5")
graph2.add(1,"5:v5","1:v1")
graph2.add(1,"5:v5","2:v2")
path2 = GraphPath(graph2,"0:v0","2:v2")
path2.show()