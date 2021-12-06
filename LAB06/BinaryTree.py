from typing import Any,Callable,Optional
import treelib as tr

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value) -> None:
        self.value = value
        self.right_child = None
        self.left_child = None   

    def min(node):
        current = node
        while(current.left_child is not None):
            current = current.left_child
 
        return current

    def is_leaf(self):
        if((self.left_child is None) and (self.right_child is None)):
            return True
        else:
            return False

    def add_left_child(self,value:Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self,value:Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]): 
        if(self.left_child is not None):
            self.left_child.traverse_in_order(visit)
        visit(self)
        if(self.right_child is not None):
            self.right_child.traverse_in_order(visit)
    
    def traverse_post_order(self, visit: Callable[[Any], None]):

        if(self.left_child is not None):
            self.left_child.traverse_post_order(visit)
        if(self.right_child is not None):
            self.right_child.traverse_post_order(visit)
        visit(self)
    
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if(self.left_child is not None):
            self.left_child.traverse_pre_order(visit)
        if(self.right_child is not None):
            self.right_child.traverse_pre_order(visit)

    def __str__(self):
        return str(self.value)

    def show(self,level=0):
        if(self.right_child!=None):
           self.right_child.show(level+1)
        if(level>0):
            print("    "*level,'->',self.value)
        else:
            print("    "*level,self.value)
        if(self.left_child!=None):
           self.left_child.show(level+1)

class BinaryTree:
    root: BinaryNode

    def __init__(self, value = None, root: BinaryNode = None)->None:
        if root is None:
            self.root = BinaryNode(value)
        else:
            self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)
    
    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    

    




