# heap_sort_alg.py
# COMP2090SEF Task2 New Algorithm: Heap Sort (O(nlogn))
from heap_structure import MaxHeap

def heap_sort(input_list):
    max_heap = MaxHeap()
    for item in input_list:
        max_heap.insert(item)
    
    descending_list = []
    while max_heap.display_heap():
        descending_list.append(max_heap.delete_top())
    
    return descending_list[::-1]

if __name__ == "__main__":
    original_list = [5, 2, 9, 1, 6]
    print("Original list:", original_list)
    print("After heap sort:", heap_sort(original_list))