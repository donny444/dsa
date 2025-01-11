class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        temp = self.root
        while True:
            if newNode.value is temp.value:
                return None
            if(newNode.value < temp.value):
                if temp.left is None:
                    temp.left = newNode
                    return self
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return self
                temp = temp.right
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if(value < temp.value):
                temp = temp.left
            elif(value > temp.value):
                temp = temp.right
            else:
                return True
        return False
    def minimumNode(currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode