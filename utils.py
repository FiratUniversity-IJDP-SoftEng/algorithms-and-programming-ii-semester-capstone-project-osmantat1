# utils.py
# This file contains utility functions used for generating sample data,
# measuring execution time, and formatting output for the BST visualizer.

import random
import time

def generate_random_numbers(count=10, min_val=1, max_val=100):
    """
    Generate a list of random integers.

    Args:
        count (int): Number of integers to generate.
        min_val (int): Minimum possible value.
        max_val (int): Maximum possible value.

    Returns:
        list: A list of random integers.
    """
    return random.sample(range(min_val, max_val), count)


def measure_time(func):
    """
    Decorator to measure the execution time of a function.

    Args:
        func (function): Function to be measured.

    Returns:
        function: Wrapped function with timing.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[Timer] Function '{func.__name__}' executed in {end - start:.6f} seconds.")
        return result
    return wrapper


def print_list(label, items):
    """
    Print a labeled list of items.

    Args:
        label (str): A label for the list.
        items (list): Items to print.
    """
    print(f"{label}: {' '.join(map(str, items))}")

