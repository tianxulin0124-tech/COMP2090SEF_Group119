# Library Management System
A simple OOP-based library management system written in Python, developed for COMP2090SEF / COMP8090SEF/S209W (EECS S&T HKMU).

## Topic
Self-study and implementation of:
- **Object-Oriented Programming (OOP)** core concepts (Abstraction, Encapsulation, Inheritance, Polymorphism)
- A menu-driven command-line Library Management System to simulate real library operations

## Project Files
| File Name | Description |
|-----------|-------------|
| `library_system.py` | Full implementation of the library management system (includes all OOP classes and CLI interactive interface) |
| `README.md` | Project documentation (usage, features, OOP details) |
| `User_Guide.md` | Step-by-step guide to run and test the system (optional) |

## Core Functions
### Library Item Management
- `add_item(item)`: Add new library items (Books/Magazines) to inventory
- `remove_item(item_id)`: Remove existing items from inventory
- `search_item(keyword)`: Search items by title, author, or item ID (fuzzy match)
- `list_all_items()`: Display all items with availability and borrowing details

### User Management
- `add_user(user)`: Register new users (Readers/Librarians)
- `get_user_by_id(user_id)`: Retrieve user information by ID
- `list_all_users()`: Display all registered users and their roles

### Borrow & Return Operations
- `borrow_item(user_id, item_id)`: Allow readers to borrow available items (14-day borrowing period)
- `return_item(item_id)`: Process item returns and update availability status

## OOP Concepts Implemented
### 1. Abstraction
- Abstract Base Classes (ABC): `LibraryItem` (for all library items) and `User` (for all system users)
- Mandatory abstract methods: `get_item_type()` (for items) and `get_user_type()` (for users)

### 2. Encapsulation
- Private attributes (prefixed with `_`): `_item_id`, `_is_available`, `_borrowed_items`
- Controlled access via `@property` decorators and public methods (`borrow()`, `return_item()`)

### 3. Inheritance
| Parent Class | Subclasses | Unique Features |
|--------------|------------|-----------------|
| `LibraryItem` | `Book` | `_isbn`, `_category` |
| `LibraryItem` | `Magazine` | `_issue_number` |
| `User` | `Reader` | `_borrowed_items` list |
| `User` | `Librarian` | `_staff_id` (staff identification) |

### 4. Polymorphism
- `Book.get_item_type()` returns "Book"; `Magazine.get_item_type()` returns "Magazine"
- `Reader.get_user_type()` returns "Regular Reader"; `Librarian.get_user_type()` returns "Librarian"

## How to Run

### Execution Steps
1. Clone or download the project to your local machine
2. Open terminal/command prompt and navigate to the project folder:
   ```bash
   cd /path/to/your/project/folder


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
