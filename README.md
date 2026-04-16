# COMP2090SEF Group 119 - Task 1 Final Submission
# Library Management System
A simple command-line Library Management System developed in Python, based on Object-Oriented Programming (OOP) concepts. This project simulates core library operations including book borrowing, returning, searching, and user management.

---

## Features
- Borrow and return books and magazines
- Search items by title, author, or ID
- View all library items and their availability status
- View all registered users (readers and librarians)
- Automatic 14-day borrowing period calculation
- Menu-driven command-line interface

---

## OOP Concepts Implemented
- Abstraction: Abstract base classes `LibraryItem` and `User`
- Encapsulation: Private attributes with controlled access
- Inheritance: `Book`/`Magazine` from `LibraryItem`; `Reader`/`Librarian` from `User`
- Polymorphism: Method overriding in subclasses

---

## User Guide

### 1. How to Run
1. Save the code as `library_system.py`
2. Open terminal or command prompt
3. Navigate to the project folder
4. Run the program:


### 2. Menu Functions
1. Borrow Item
2. Return Item
3. Search Item
4. View All Items
5. View All Users
6. Exit System

### 3. Test Instructions
The system automatically loads test data on startup.

#### Test Users
- Reader: U001 (Zhang San)
- Reader: U002 (Li Si)
- Librarian: A001 (Cannot borrow items)

#### Test Items
- B001: Python Crash Course
- B002: Core Java
- M001: National Geographic

### 4. Example Operation
1. Choose 1 → Enter U001 → Enter B001 (Borrow book)
2. Choose 4 → Check status is Borrowed
3. Choose 2 → Enter B001 (Return book)
4. Choose 6 → Exit

---

## Update Log

### v0.1.0 (2026-03-25)
- Project initialization and basic structure setup
- Created core abstract classes: LibraryItem and User
- Implemented basic class skeleton for Book, Magazine, Reader, and Librarian
- Added borrowing and returning logic
- Implemented item status control (Available / Borrowed)
- Added encapsulation using private attributes and property methods
- Completed basic inheritance structure for all subclasses

### v0.2.0 (2026-03-30)
- Added search function by title, author, and item ID
- Implemented polymorphism through method overriding
- Added date calculation using datetime module (14-day borrow period)
- Improved system stability and error prompts

### v0.3.0 (2026-04-05)
- Built complete command-line menu interface
- Added view functions for all items and users
- Added built‑in test data for quick demonstration
- Optimized output format and display layout

### v0.4.0 (2026-04-10)
- Fixed bugs in user permission checks
- Enhanced input validation and error handling
- Improved code readability and structure
- Added comments for key functions

### v1.0.0 (2026-04-16)
- Final stable version released
- All OOP concepts fully implemented and tested
- Completed user guide and test cases
- System fully functional for demonstration and submission

---

## References
Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). Design patterns: Elements of reusable object-oriented software. Addison-Wesley.

Kumar, V., & Singh, S. (2020). Design and implementation of a library management system using Python. International Journal of Scientific Research.

Lott, S. F., & Phillips, D. (2021). Python object-oriented programming (4th ed.). Packt Publishing.

Lutz, M. (2013). Learning Python (5th ed.). O’Reilly Media.

Martelli, A., Ravenscroft, A., & Ascher, D. (2010). Python cookbook (3rd ed.). O’Reilly Media.

Martin, R. C. (2008). Clean code: A handbook of agile software craftsmanship. Prentice Hall.

Nwokwu, P. M. (2018). Development of library management system with Python. International Journal of Engineering.

Ramalho, L. (2022). Fluent Python (2nd ed.). O’Reilly Media.

Python Software Foundation. (2024). abc — Abstract base classes. Python Documentation. Retrieved from https://docs.python.org/3/library/abc.html

Python Software Foundation. (2024). datetime — Basic date and time types. Python Documentation. Retrieved from https://docs.python.org/3/library/datetime.html

Zelle, J. M. (2017). Python programming: An introduction to computer science (2nd ed.). Franklin, Beedle & Associates.

Hu, X. C., Tian, J., & Chen, Y. (2021). Research and development of library information management system based on Python. Information Technology and Informatization, (5), 37–40.


# COMP2090SEF Group 119 - Task 2 Final Submission

## Topic
Self-study and implementation of:
- Data Structure: Max Heap
- Algorithm: Heap Sort

## Files
- `heap_structure.py`: Implementation of Max Heap
- `heap_sort_alg.py`: Heap Sort algorithm using Max Heap

## Functions
### MaxHeap
- `insert(value)`
- `delete_top()`
- `heapify_up()`
- `heapify_down()`
- `display_heap()`

### Heap Sort
- `heap_sort(input_list)`: Returns sorted list in ascending order

## How to Run
<<<<<<< Updated upstream
python heap_structure.py
python heap_sort_alg.py
=======
1. Open command line and navigate to the Task2 folder
2. Run MaxHeap test: `python heap_structure.py`
3. Run Heap Sort test: `python heap_sort_alg.py`
>>>>>>> Stashed changes

## Test Results
- MaxHeap: Insertion and deletion work correctly
- HeapSort: Sorts the input list with time complexity O(n log n)
