from BinaryTree import Any, BinaryNode, BinaryTree
from LinkedList import LinkedList,Node
from typing import List

def all_equal_paths(curr_node:BinaryNode, sum,sum_so_far, path:LinkedList):
 
    if (not curr_node) :
        return

    sum_so_far += curr_node.value
    path.append(curr_node.value)
    i = 0
    if (sum_so_far == sum ) :
        while(i<path.__len__()):
            print(path.node(i), end = " ")
            i+=1
        print()

    if (curr_node.left_child != None) :
        all_equal_paths(curr_node.left_child, sum,sum_so_far, path)

    if (curr_node.right_child != None) :
        all_equal_paths(curr_node.right_child, sum,sum_so_far, path)

    path.remove_last()

def printPaths(root, sum):
    path = LinkedList()
    all_equal_paths(root, sum, 0, path)

tree = BinaryTree(1)
tree.root.add_left_child(2)
tree.root.add_right_child(3)
tree.root.left_child.add_left_child(7)
tree.root.left_child.add_right_child(5)
tree.root.right_child.add_left_child(6)
tree.root.right_child.add_right_child(7)
printPaths(tree.root,10)



