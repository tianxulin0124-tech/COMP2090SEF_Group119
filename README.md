# COMP2090SEF Group 119 - Task 2 Final Submission
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
| `Project_Report.pdf` | Formal project report (covers core functions, OOP usage, self-reflection) |

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
- Purpose: Define unified interface for subclasses, hide unnecessary implementation details

### 2. Encapsulation
- Private attributes (prefixed with `_`): `_item_id`, `_is_available`, `_borrowed_items`, `_user_id`
- Controlled access via `@property` decorators (e.g., `item_id`, `user_id`)
- Public business methods: `borrow()`, `return_item()`, `add_borrowed_item()`
- Purpose: Ensure data integrity, prevent invalid modification of core attributes

### 3. Inheritance
| Parent Class | Subclasses | Inherited Attributes | Unique Features |
|--------------|------------|----------------------|-----------------|
| `LibraryItem` | `Book` | `_item_id`, `_title`, `_author`, `_is_available` | `_isbn`, `_category` |
| `LibraryItem` | `Magazine` | `_item_id`, `_title`, `_author`, `_is_available` | `_issue_number` |
| `User` | `Reader` | `_user_id`, `_name`, `_contact` | `_borrowed_items` list, borrow/return permissions |
| `User` | `Librarian` | `_user_id`, `_name`, `_contact` | `_staff_id`, no borrowing permissions |
- Purpose: Reuse core code, reduce redundancy, extend functionality for specific types

### 4. Polymorphism
- Method overriding in subclasses:
  - `Book.get_item_type()` → returns "Book"
  - `Magazine.get_item_type()` → returns "Magazine"
  - `Reader.get_user_type()` → returns "Regular Reader"
  - `Librarian.get_user_type()` → returns "Librarian"
- Purpose: Uniform handling of different subclasses, flexible extension (e.g., add `DVD` type without changing core logic)

## External Resources Declaration
- No external third-party libraries are used in this project
- All functions rely on Python's built-in standard libraries:
  - `abc`: Implement abstract base classes (core for OOP abstraction)
  - `datetime`: Calculate borrowing periods (14-day limit) and due dates
- All code is original, no external code (from GitHub/other programmers) is used

## Self-Reflection
### Potential Weaknesses
1. **No data persistence**: All data (items/users/borrowing records) is stored in memory and lost when the program closes
2. **Basic CLI only**: No graphical user interface (GUI), low usability for non-technical users
3. **Limited security**: No password authentication, any user with a valid ID can borrow items
4. **Simple permission control**: Only basic differentiation between readers and librarians

### Future Improvements
1. Add data persistence using `json`/`csv` files or SQLite database
2. Implement a GUI with Python's built-in `tkinter` library
3. Add password hashing and role-based permission control (e.g., only librarians can add/remove items)
4. Extend features: item reservation, overdue fine calculation, borrowing statistics reports
5. Add input validation (e.g., check ID format, prevent empty input)

## How to Run

### Execution Steps
1. Clone or download the project to your local machine:
   ```bash
   git clone [your-github-repository-url]


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
