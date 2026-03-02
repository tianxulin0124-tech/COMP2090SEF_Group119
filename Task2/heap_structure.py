# heap_structure.py
# COMP2090SEF Task2 New Data Structure: Max Heap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def get_parent_idx(self, child_idx):
        return (child_idx - 1) // 2

    def swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def heapify_up(self, idx):
        while idx > 0 and self.heap[idx] > self.heap[self.get_parent_idx(idx)]:
            p_idx = self.get_parent_idx(idx)
            self.swap(idx, p_idx)
            idx = p_idx

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_down(self, idx):
        max_idx = idx
        length = len(self.heap)
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < length and self.heap[left] > self.heap[max_idx]:
            max_idx = left
        if right < length and self.heap[right] > self.heap[max_idx]:
            max_idx = right

        if max_idx != idx:
            self.swap(idx, max_idx)
            self.heapify_down(max_idx)

    def delete_top(self):
        if not self.heap:
            return "Error: Heap is empty!"
        if len(self.heap) == 1:
            return self.heap.pop()
        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return top

    def show_heap(self):
        return self.heap

# Test the heap
if __name__ == "__main__":
    h = MaxHeap()
    for val in [5, 3, 8, 10]:
        h.insert(val)
    print("Heap content:", h.show_heap())
    print("Deleted top element:", h.delete_top())