from typing import List

class BinaryHeap:
    def __str__(self):
        return str(self.vals)

    def append(self, val: int):
        self.vals.append(val)

    def pop(self):
        val = self.vals[0]

        self.vals[0] = self.vals[len(self.vals)-1]
        self.vals.pop()

        return val

    def parent(self, i):
        return int((i - 1) / 2) if i > 0 else -1

    def left(self, i):
        l = 2 * i + 1
        return l if l < len(self.vals) else -1
    
    def right(self, i):
        r = 2 * i + 2
        return r if r < len(self.vals) else -1

    def swap(self, x, y):
        t = self.vals[x]
        self.vals[x] = self.vals[y]
        self.vals[y] = t

class MinHeap(BinaryHeap):
    def __init__(self):
        self.vals = []

    def append(self, val: int):
        super().append(val)

        i = len(self.vals)-1
        while i != 0 and self.vals[self.parent(i)] > self.vals[i]:
            parent = self.parent(i)
            self.swap(i, parent)
            i = parent

    def pop(self):
        val = super().pop()

        i = 0
        while True:
            left = self.left(i)
            right = self.right(i)

            if left == -1 and right == -1:
                break

            s = i
            if left != -1 and self.vals[left] < self.vals[i]:
                s = left
            if right != -1 and self.vals[right] < self.vals[s]:
                s = right

            if s != i:
                self.swap(i, s)
                i = s
            else:
                break
            
        return val

class MaxHeap(BinaryHeap):
    def __init__(self):
        self.vals = []

    def append(self, val: int):
        super().append(val)

        i = len(self.vals)-1
        while i != 0 and self.vals[self.parent(i)] < self.vals[i]:
            parent = self.parent(i)
            self.swap(i, parent)
            i = parent

    def pop(self):
        val = super().pop()

        i = 0
        while True:
            left = self.left(i)
            right = self.right(i)

            if left == -1 and right == -1:
                break

            s = i
            if left != -1 and self.vals[left] > self.vals[i]:
                s = left
            if right != -1 and self.vals[right] > self.vals[s]:
                s = right

            if s != i:
                self.swap(i, s)
                i = s
            else:
                break

        return val

def minHeap(heap: List = []):
    min = MinHeap()
    for h in heap:
        min.append(h)
    return min

def maxHeap(heap: List = []):
    max = MaxHeap()
    for h in heap:
        max.append(h)
    return max