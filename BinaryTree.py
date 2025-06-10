class CircularQueue:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1) % self.capacity
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else : pass

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else : pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else : pass

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front + 1:self.rear + 1])
        else:
            return str(self.array[self.front + 1:self.capacity] + \
                       self.array[0:self.rear + 1])

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)
    
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)
    
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1
    