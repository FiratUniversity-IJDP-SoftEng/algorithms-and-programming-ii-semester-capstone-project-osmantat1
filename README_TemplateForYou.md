# Binary Search Tree (BST) - Interactive Visualization

## Project Overview

This project is an interactive command-line application that implements and visualizes the Binary Search Tree (BST) operations. It was developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

### Problem Definition

The Binary Search Tree (BST) is a data structure used to store ordered data that allows fast lookup, addition, and removal of items. This project aims to simulate and visualize these BST operations interactively.

### Mathematical Background

- A Binary Search Tree is a binary tree where each node follows this property:  
  Left subtree keys < Node key < Right subtree keys

### Algorithm Steps

1. Insertion – Place a node in the correct position based on value.
2. Search – Traverse left or right recursively to find a node.
3. Deletion – Remove a node and restructure the tree accordingly:
   - No child → remove node.
   - One child → replace node with child.
   - Two children → replace with inorder successor.
4. Traversal – Visit nodes in inorder, preorder, or postorder order.

### Pseudocode

```
function insert(node, key):
    if node is null:
        return new Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
```

## Complexity Analysis

### Time Complexity

- Best Case: O(log n) – when the tree is balanced  
- Average Case: O(log n)  
- Worst Case: O(n) – when the tree becomes a linked list

### Space Complexity

- O(n) – for storing n nodes and recursion stack

## Features

- Insert, delete, and search operations  
- Inorder, preorder, and postorder traversals  
- Random input generation  
- Unit test support  
- Modular code structure  
- Clear CLI-based menu system

## Installation

### Prerequisites

- Python 3.8 or higher  
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/osmantat/bst-visualizer.git
   cd bst-visualizer
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Launch the application with `streamlit run app.py`.  
2. Use the sidebar or CLI options to:  
   - Insert new elements into the BST  
   - Delete nodes from the BST  
   - Search for elements  
   - Visualize tree traversals (inorder, preorder, postorder)  
3. (Optional) Generate random numbers for automated testing and tree creation.

### Example Inputs

- Insert: `30`, `15`, `50`, `40`, `70`  
  - Expected Inorder Output: `15 30 40 50 70`
- Delete: `40`  
  - Inorder after deletion: `15 30 50 70`
- Search: `70` → Output: `"Found"`
- Traversal types:
  - Preorder: `30 15 50 70`
  - Postorder: `15 70 50 30`

## Implementation Details

### Key Components

- `algorithm.py`: Contains the core Binary Search Tree logic (insert, delete, search, traversals)  
- `app.py`: Main application entry point (Streamlit or CLI-based)  
- `utils.py`: Utility functions for timing, random input generation, etc.  
- `test-algorithm.py`: Unit tests for validating algorithm correctness  
- *(optional)* `visualizer.py`: Visual representation logic (future improvement)

### Code Highlights

```python
def insert(self, key):
    """
    Inserts a key into the BST.
    """
    def _insert(node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = _insert(node.left, key)
        else:
            node.right = _insert(node.right, key)
        return node
    self.root = _insert(self.root, key)
```

## Testing

This project includes a test suite to verify the correctness of the algorithm implementation:

```bash
python -m unittest test-algorithm.py
```

### Test Cases

- Insertion: Validate BST structure and inorder traversal  
- Deletion: Handle leaf, one-child, and two-child deletion cases  
- Search: Verify existing and non-existing key search  
- Traversals: Ensure outputs match expected sequences

## Live Demo

A live demo of this application is available at:  
**(Optional)** https://bst-osmantat.streamlit.app  
*(This can be deployed later using Streamlit Cloud)*

## Limitations and Future Improvements

### Current Limitations

- No graphical tree visualization (just text-based traversals)  
- Tree is not auto-balanced (no AVL or Red-Black balancing)  
- CLI/Streamlit interface only; no persistent storage

### Planned Improvements

- Integrate AVL Tree support for balanced tree comparison  
- Add `graphviz` or `networkx` for graphical visualization  
- Deploy a full web version using Streamlit Cloud

## References and Resources

### Academic References

1. Data Structures and Algorithms, Cormen et al.  
2. Binary Search Tree Lecture Notes - Fırat University  
3. AVL Trees - CLRS (Introduction to Algorithms)

### Online Resources

- https://www.geeksforgeeks.org/binary-search-tree-data-structure/  
- https://en.wikipedia.org/wiki/Binary_search_tree  
- https://docs.python.org/3/

## Author

- **Name:** Osman Tat  
- **Student ID:** 230543002  
- **GitHub:** https://github.com/osmantat1

## Acknowledgements

I would like to thank **Assoc. Prof. Ferhat UÇAR** for guidance throughout this project and my classmates for their feedback and support.

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*
