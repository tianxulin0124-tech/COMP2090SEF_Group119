# heap_sort_alg.py
# COMP2090SEF Task2 New Algorithm: Heap Sort (O(nlogn))
from heap_structure import MaxHeap

def heap_sort(input_list):
    mh = MaxHeap()
    for num in input_list:
        mh.insert(num)
    desc_list = []
    while mh.show_heap():
        desc_list.append(mh.delete_top())
    return desc_list[::-1]  # Reverse to get ascending order

# Test the heap sort
if __name__ == "__main__":
    test_list = [5, 2, 9, 1, 6]
    print("Original list:", test_list)
    print("After heap sort:", heap_sort(test_list))