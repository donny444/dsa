class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__ (self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = self.head
        self.length = 1
    def push(self, value):
        newNode = Node(value)
        if(not self.head):
            self.head = newNode
            self.tail = newNode 
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self
    def pop(self):
        if(self.length == 0): return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if(self.length == 0):
            self.head = None
            self.tail = None
        return temp
    def unshift(self, value):
        newNode = Node(value)
        if(not self.head):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self
    def shift(self):
        if(self.length == 0): return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if(self.length == 0):
            self.tail = None
        temp.next = None
        return temp
    def get(self, index):
        if(index < 0 or index >= self.length): return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    def set(self, index, value):
        temp = self.get(index)
        if (temp):
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if(index < 0 or index > self.length): return False
        if(index == self.length): return self.push(value)
        if(index == 0): return self.unshift(value)
        newNode = Node(value)
        temp = self.get(index - 1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True
    def remove(self, index):
        if(index < 0 or index >= self.length): return None
        if(index == 0): return self.shift()
        if(index == self.length - 1): return self.pop()
        before = self.get(index - 1)
        temp = before.next
        before.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        next = temp.next
        prev = None
        for i in range(self.length):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        return self
    def showList(self):
        temp = self.head
        print("Nodes in the Linked List: ", end="")
        while(temp):
            print(temp.value, end=" ")
            temp = temp.next

obj = LinkedList(5)
arr = [1, 2, 3, 6, 9, 8]
for i in range(len(arr)): # 5, 1, 2, 3, 6, 9, 8
    obj.push(arr[i])
obj.pop() # 5, 1, 2, 3, 6, 9
obj.unshift(7) # 7, 5, 1, 2, 3, 6, 9
obj.shift()# 5, 1, 2, 3, 6, 9

print("Value at the specfic index: " + str(obj.get(4).value)) # 6
obj.showList()

print("\n")

obj.insert(6, 4)
obj.insert(0, 4)
print(obj.insert(3, 5))
obj.showList()

print("\n")

print(obj.remove(-1))
print(obj.remove(9))
obj.remove(0)
obj.remove(7)
obj.remove(2)
obj.showList()

print("\n")

obj.reverse()
obj.showList()