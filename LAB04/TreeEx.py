from Tree import Tree,TreeNode

tree = Tree('F')
tree.root.add(TreeNode('B'))
tree.root.add(TreeNode('G'))
tree.root.children[0].add(TreeNode('A'))
tree.root.children[0].add(TreeNode('D'))
tree.root.children[0].children[1].add(TreeNode('C'))
tree.root.children[0].children[1].add(TreeNode('E'))
tree.root.children[1].add(TreeNode('I'))
tree.root.children[1].children[0].add(TreeNode('H'))
tree.show()
