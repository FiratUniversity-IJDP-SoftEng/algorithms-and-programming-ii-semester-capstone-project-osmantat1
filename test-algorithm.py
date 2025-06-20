# test-algorithm.py
# Unit tests for the BinarySearchTree class using Python's unittest module.

import unittest
from algorithm import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        """
        Runs before each test. Creates a new BST and inserts some values.
        """
        self.bst = BinarySearchTree()
        for value in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(value)

    def test_inorder(self):
        """
        Test inorder traversal returns sorted values.
        """
        expected = [20, 30, 40, 50, 60, 70, 80]
        self.assertEqual(self.bst.inorder(), expected)

    def test_preorder(self):
        """
        Test preorder traversal.
        """
        expected = [50, 30, 20, 40, 70, 60, 80]
        self.assertEqual(self.bst.preorder(), expected)

    def test_postorder(self):
        """
        Test postorder traversal.
        """
        expected = [20, 40, 30, 60, 80, 70, 50]
        self.assertEqual(self.bst.postorder(), expected)

    def test_search_existing(self):
        """
        Test searching for a key that exists.
        """
        self.assertTrue(self.bst.search(40))
        self.assertTrue(self.bst.search(70))

    def test_search_non_existing(self):
        """
        Test searching for a key that does not exist.
        """
        self.assertFalse(self.bst.search(999))
        self.assertFalse(self.bst.search(-10))

    def test_delete_leaf(self):
        """
        Test deleting a leaf node (no children).
        """
        self.bst.delete(20)
        self.assertFalse(self.bst.search(20))
        self.assertEqual(self.bst.inorder(), [30, 40, 50, 60, 70, 80])

    def test_delete_node_with_one_child(self):
        """
        Test deleting a node with one child.
        """
        self.bst.delete(30)  # 30 has one child: 40
        self.assertFalse(self.bst.search(30))
        self.assertEqual(self.bst.inorder(), [20, 40, 50, 60, 70, 80])

    def test_delete_node_with_two_children(self):
        """
        Test deleting a node with two children.
        """
        self.bst.delete(50)  # root node with 2 children
        self.assertFalse(self.bst.search(50))
        self.assertEqual(self.bst.inorder(), [20, 30, 40, 60, 70, 80])

if __name__ == '__main__':
    unittest.main()

