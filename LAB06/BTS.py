from typing import Any,List,Optional,Callable
from BinaryTree import BinaryNode
import treelib as tr

class BinarySearchTree:
    root: BinaryNode
    def __init__(self, value = None, root: BinaryNode = None)->None:
        if root is None:
            self.root = BinaryNode(value)
        else:
            self.root = root
    
    def _insert(self, node: BinaryNode, value: Any) -> 'BinaryNode':
        if value < node.value:
            if node.left_child is not None:
                self._insert(node.left_child, value)
            else:
                node.add_left_child(value)
                return node.left_child

        if value >= node.value:
            if node.right_child is not None:
                self._insert(node.right_child, value)
            else:
                node.add_right_child(value)
                return node.right_child

    def insert(self, value):
        self._insert(self.root, value)

    def insertlist(self, list: List[Any]) -> None:
         for i in list:
            self.insert(i)

    def contains(self, value) -> bool:
        res: List[bool] = [False]

        def compare(node: BinaryNode) -> None:
            if node.value == value:
                res[0] = True

        self.root.traverse_pre_order(compare)
        return res[0]

    def remove(self,node: BinaryNode, value):
        if node is None:
            return node
        if value < node.value:
            node.left_child = self.remove(node.left_child,value)
        elif(value > node.value):
            node.right_child = self.remove(node.right_child,value)
        else:
            if node.left_child is None:
                temp = node.right_child
                node = None
                return temp
 
            elif node.right_child is None:
                temp = node.left_child
                node = None
                return temp
            temp = BinaryNode.min(node.right_child)
            node.value = temp.value
 
            node.right_child = self.remove(node.right_child, temp.value)
 
        return node
 


    def show(self) -> None:
        g = tr.Tree()

        g.create_node(str(self.root.value), str(self.root.value))

        def add_edge(node: 'BinaryNode') -> None:
            if node.left_child is not None:
                g.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))
            if node.right_child is not None:
                g.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))

        self.root.traverse_pre_order(add_edge)
        g.show()