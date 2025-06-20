# algorithm.py
# This module implements a basic Binary Search Tree (BST).
# It includes insertion, deletion, searching, and tree traversals.

class Node:
    """
    A node in the Binary Search Tree.

    Attributes:
        key (int): The value stored in the node.
        left (Node): The left child node.
        right (Node): The right child node.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A Binary Search Tree (BST) implementation.

    Methods:
        insert(key): Inserts a key into the BST.
        delete(key): Deletes a key from the BST.
        search(key): Searches for a key in the BST.
        inorder(): Returns keys in inorder traversal.
        preorder(): Returns keys in preorder traversal.
        postorder(): Returns keys in postorder traversal.
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Insert a new key into the BST.

        Args:
            key (int): The key to insert.
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

    def search(self, key):
        """
        Search for a key in the BST.

        Args:
            key (int): The key to search for.

        Returns:
            bool: True if found, False otherwise.
        """
        def _search(node, key):
            if not node:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.root, key)

    def delete(self, key):
        """
        Delete a key from the BST.

        Args:
            key (int): The key to delete.
        """
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, key):
            if not node:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Node with only one child or no child
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # Node with two children: Get the inorder successor
                temp = _min_value_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            return node

        self.root = _delete(self.root, key)

    def inorder(self):
        """
        Inorder traversal (Left, Root, Right).

        Returns:
            list: Keys in ascending order.
        """
        def _inorder(node):
            return _inorder(node.left) + [node.key] + _inorder(node.right) if node else []
        return _inorder(self.root)

    def preorder(self):
        """
        Preorder traversal (Root, Left, Right).

        Returns:
            list: Keys in preorder.
        """
        def _preorder(node):
            return [node.key] + _preorder(node.left) + _preorder(node.right) if node else []
        return _preorder(self.root)

    def postorder(self):
        """
        Postorder traversal (Left, Right, Root).

        Returns:
            list: Keys in postorder.
        """
        def _postorder(node):
            return _postorder(node.left) + _postorder(node.right) + [node.key] if node else []
        return _postorder(self.root)

