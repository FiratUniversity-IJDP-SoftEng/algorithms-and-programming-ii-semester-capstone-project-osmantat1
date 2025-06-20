# app.py
# Main application file to interact with the Binary Search Tree (BST).
# Allows users to insert, delete, search, and view traversals of the BST.

from algorithm import BinarySearchTree
from utils import generate_random_numbers, print_list
import sys

def print_menu():
    """
    Print the main menu options for interacting with the BST.
    """
    print("\n==== Binary Search Tree Operations ====")
    print("1. Insert a number")
    print("2. Delete a number")
    print("3. Search for a number")
    print("4. Print traversals (Inorder / Preorder / Postorder)")
    print("5. Generate random numbers and build tree")
    print("6. Exit")

def main():
    bst = BinarySearchTree()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                val = int(input("Enter number to insert: "))
                bst.insert(val)
                print(f"> {val} inserted into the tree.")
            except ValueError:
                print("[!] Invalid input. Please enter an integer.")

        elif choice == '2':
            try:
                val = int(input("Enter number to delete: "))
                bst.delete(val)
                print(f"> {val} deleted from the tree (if it existed).")
            except ValueError:
                print("[!] Invalid input. Please enter an integer.")

        elif choice == '3':
            try:
                val = int(input("Enter number to search: "))
                found = bst.search(val)
                print(f"> {val} {'found' if found else 'not found'} in the tree.")
            except ValueError:
                print("[!] Invalid input. Please enter an integer.")

        elif choice == '4':
            print_list("Inorder", bst.inorder())
            print_list("Preorder", bst.preorder())
            print_list("Postorder", bst.postorder())

        elif choice == '5':
            try:
                count = int(input("How many random numbers? "))
                numbers = generate_random_numbers(count)
                for num in numbers:
                    bst.insert(num)
                print_list("Inserted random numbers", numbers)
            except ValueError:
                print("[!] Invalid input. Please enter a valid number.")

        elif choice == '6':
            print("Exiting program.")
            sys.exit()

        else:
            print("[!] Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()

