class MaxHeap:
    def __init__(self):
        self.heap = [None]  

    def heappush(self, n):
        self.heap.append(n)
        i = len(self.heap) - 1
        while i > 1:
            pi = i // 2
            if n <= self.heap[pi]:
                break
            self.heap[i] = self.heap[pi]
            i = pi
        self.heap[i] = n

    def heappop(self):
        size = len(self.heap) - 1
        if size == 0:
            return None
        root = self.heap[1]
        last = self.heap.pop()
        size -= 1
        if size == 0:
            return root

        i = 1
        while i * 2 <= size:
            ci = i * 2
            if ci < size and self.heap[ci] < self.heap[ci + 1]:
                ci += 1
            if last >= self.heap[ci]:
                break
            self.heap[i] = self.heap[ci]
            i = ci
        self.heap[i] = last
        return root

    def __str__(self):
        return str(self.heap[1:])




