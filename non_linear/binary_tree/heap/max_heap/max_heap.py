class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        largest = i

        if l < len(self.heap) and self.heap[l] > self.heap[largest]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)
    
    def insert(self, data):
        self.heap.append(data)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
        
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        heap_max = self.heap.pop()
        self.heapify(0)

        return heap_max
    
    def delete(self, data):
        if len(self.heap) == 0:
            return None
        
        i = self.heap.index(data)
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        self.heap.pop()
        self.heapify(i)

    
    def __str__(self):
        return str(self.heap)

if __name__ == "__main__":
    print("\n\nMAX HEAP\n")

    heap = MaxHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    heap.insert(2)
    heap.insert(1)
    heap.insert(9)
    heap.insert(4)
    heap.insert(6)
    heap.insert(8)
    
    print("[Heap]:", heap)
    heap.delete(3)
    print("[Heap]:", heap)
    
    print("[Extract Max]:", heap.extract_max())
    print("[Heap]:", heap)
    print("[Extract Max]:", heap.extract_max())
    print("[Heap]:", heap)
