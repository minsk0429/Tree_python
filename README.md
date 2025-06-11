# Tree_Structures_python

Data structures implemented in Python (Binary Tree, Heap Tree)

---

# 🌳 Tree in Data Structures

## 📋 What is a Tree?

A **tree** is a hierarchical data structure consisting of nodes connected by edges. It is used to represent relationships where each item (node) has a parent and potentially many children, except for the root which has no parent.

---

# Binary Tree

## 📋 Binary Tree

A **binary tree** is a type of tree where each node has **at most two children**, usually referred to as the **left** and **right** child.

---

## Characteristics
- Each node has 0, 1, or 2 children  
- The topmost node is called the **root**  
- Nodes with no children are **leaves**  
- Used as the base structure for more complex trees like binary search trees (BSTs), heaps, AVL trees, etc.

---

## Basic Operations

### ✅ Insertion

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
```

### ✅ Tree Traversals
- Inorder (LNR): Left → Node → Right
- Preorder (NLR): Node → Left → Right
- Postorder (LRN): Left → Right → Node

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
```

---

### Use Cases

- Expression trees in compilers
- Hierarchical data representation (e.g., file systems)
- Binary search trees (BSTs) for fast search
- Tree-based algorithms like Huffman coding

---

# Heap Tree

## 📋 Heap Tree

A **heap** is a special type of binary tree used for efficient retrieval of the **minimum** or **maximum** element, depending on the heap type.

- **Min-Heap**: Parent is smaller than or equal to its children
- **Max-Heap**: Parent is larger than or equal to its children
- Implemented as a **complete binary tree** (filled from left to right)

---

### Characteristics

- Always a complete binary tree
- Supports operations like:
  - `insert`
  - `extract_min` / `extract_max`
  - `heapify`
- Commonly implemented using arrays (index-based parent-child relationship)

---

### Example (Min-Heap using heapq)

```python
import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)

print(heapq.heappop(heap))  # Output: 1
```

---

### Use Cases

- Priority queues
- Scheduling systems (e.g., CPU, Dijkstra’s algorithm)
- Heap sort
- Real-time data streaming (to get top-k/largest/smallest elements)

---

## 🚀 Summary

| Structure            | Description                              | Properties                                      | Common Use Cases                             |
|----------------------|------------------------------------------|------------------------------------------------|----------------------------------------------|
| Binary Tree          | Tree with up to two children per node    | Hierarchical, not necessarily ordered          | Expression trees, hierarchical data          |
| Binary Search Tree   | Binary tree with ordered nodes           | Left < Root < Right                            | Fast searching, insertion, deletion          |
| Tree Traversals      | Inorder, Preorder, Postorder             | DFS variants                                   | File systems, syntax trees, serialization    |
| Heap (Min/Max Heap)  | Complete binary tree for priority values | Min: parent ≤ children<br>Max: parent ≥ children | Priority queues, scheduling, heap sort       |

---
The attached codes are sorting and searching implemented in Python including Binary tree (function version), Morse code decision tree creation function (including Morse code encoding algorithm and Morse code decoding), Max-heap (function version), Huffman coding tree creation function.
