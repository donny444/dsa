class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = newNode
                return
            elif not node.right:
                node.right = newNode
                return
            else:
                queue.append(node.left)
                queue.append(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    def removeallnodes(self, node):
        if node is not None:
            self.removeallnodes(node.left)
            self.removeallnodes(node.right)
            node = None

#Usage Example
tree = BinaryTree()
values = [1, 2, 3, 4, 5, 6, 7]

for value in values:
    tree.insert(value)

tree.inorder(tree.root)
tree.preorder(tree.root)
tree.postorder(tree.root)