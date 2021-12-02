from BinaryTree import Any, BinaryNode, BinaryTree

b = BinaryNode(10)
b.add_left_child(9)
b.add_right_child(2)
b.left_child.add_left_child(1)
b.left_child.add_right_child(3)
b.right_child.add_left_child(4)
b.right_child.add_right_child(6)

tree = BinaryTree()
print(tree.show(tree))