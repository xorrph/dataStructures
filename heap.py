import math


class heap:
    def __init__(self,array):
        self.size = len(array) -1
        self.heap = self.buildHeap(array)

    def __repr__(self):
        return str([x.data for x in array])

    def buildHeap(self,array):
        self.heap = array
        print([x.data for x in array])
        for i in range(self.size//2,-1,-1):
            self.heapify(i)
        return self.heap


    def heapify(self,i):
        l = self.heap[i].left() - 1
        r = self.heap[i].right() - 1
        if l <= self.size and self.heap[l].data > self.heap[i].data:
            largest = l
        else: largest = i
        if r <= self.size and self.heap[r].data > self.heap[largest].data:
            largest = r
        if largest != i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.heap[i].i, self.heap[largest].i = self.heap[largest].i, self.heap[i].i
            self.heapify(largest)

    def heapsort(self):
        for i in range(self.size,0,-1):
            self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
            self.heap[0].i, self.heap[i].i = self.heap[i].i, self.heap[0].i
            self.size -= 1
            self.heapify(0)


class node:
    def __init__(self,data,i):
        self.data = data
        self.i = i

    def parent(self):
        return math.floor(self.i/2)

    def left(self):
        return 2 * self.i

    def right(self):
        return 2 * self.i + 1

    def setIndex(self,i):
        self.i = i

array = [node(i,i+1) for i in range(10)]
h = heap(array)
print(h)
h.heapsort()
print(h)

