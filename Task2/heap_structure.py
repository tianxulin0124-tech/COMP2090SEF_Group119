# heap_structure.py
# COMP2090SEF Task2 New Data Structure: Max Heap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def swap_nodes(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self.get_parent_index(index)]:
            parent_index = self.get_parent_index(index)
            self.swap_nodes(index, parent_index)
            index = parent_index

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_down(self, index):
        max_index = index
        length = len(self.heap)
        left = 2 * index + 1
        right = 2 * index + 2

        if left < length and self.heap[left] > self.heap[max_index]:
            max_index = left
        if right < length and self.heap[right] > self.heap[max_index]:
            max_index = right

        if max_index != index:
            self.swap_nodes(index, max_index)
            self.heapify_down(max_index)

    def delete_top(self):
        if not self.heap:
            return None 
        
        top_value = self.heap[0]
        
        if len(self.heap) == 1:
            self.heap.pop()
            return top_value
        
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        
        return top_value

    def display_heap(self):
        return self.heap

# Test code
if __name__ == "__main__":
    heap = MaxHeap()
    test_data = [10, 8, 5, 3]
    for num in test_data:
        heap.insert(num)
    print("Heap content:", heap.display_heap())
    print("Deleted top element:", heap.delete_top())
    print("Heap after deletion:", heap.display_heap())