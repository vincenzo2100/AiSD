from typing import Any, Callable, List , Union
from Queue import Queue
import treelib as tr


class TreeNode:
    value: Any
    children: List['TreeNode']

    def is_leaf(self)->bool:
        if(len(self.children)==0):
            return True
        else:
            return False
    
    def add(self,child:'TreeNode')->None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for i in self.children:
            i.for_each_deep_first(visit)
            
    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        queue = Queue()

        for i in self.children:
            queue.enqueue(i)

        while len(queue) != 0:
            x = queue.dequeue()
            visit(x)
            for i in x.children:
                queue.enqueue(i)
            

    def search(self, value: Any) -> Union['TreeNode', List['TreeNode'], None]:
        result: List[TreeNode] = []

        def search_foo(node: 'TreeNode'):
            if node.value == value:
                result.append(node)

        self.for_each_level_order(search_foo)

        if len(result) == 0:
            return None
        elif len(result) == 1:
            return result[0]


    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)

class Tree:
    root: TreeNode

    def add(self, value: Any, parent_name: 'TreeNode') -> None:

        is_present: List[bool] = [False]

        def search_nodes(node: 'TreeNode') -> None:
            if node == parent_name:
                is_present[0] = True

        self.root.for_each_level_order(search_nodes)

        if is_present[0]:
            parent_name.add(value)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self) -> None:
        G = tr.Tree()

        G.create_node(str(self.root.value), str(self.root.value))

        def add_edge(node: 'TreeNode') -> None:
            for i in node.children:
                G.create_node(str(i.value), str(i.value), parent=str(node.value))

        self.for_each_level_order(add_edge)
        G.show()

    def __init__(self, value=None):
        self.root = TreeNode(value)

    def __len__(self):
        count: List[int] = [0]

        def counter() -> None:
            count[0] += 1

        self.for_each_level_order(counter)

        return counter
