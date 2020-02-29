import sys

sys.path.append("../queue_and_stack")
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # current = self
        # # to create a new tree when we find a place to insert
        # new = None
        # # if there is no root, the newly inserted value is the root
        # while True:
        #     # if there is a root, check if the value is < or > the root
        #     # if smaller, look left
        #     # if no node, add node
        #     # if great, look right
        #     # repeat steps
        #     if value <= current.value and current.left is not None:
        #         current = current.left
        #     elif value >= current.value and current.right is not None:
        #         current = current.right
        #     elif value <= current.value and current.left is None:
        #         # create new node
        #         current.left = BinarySearchTree(value)
        #         # assign to left node tree
        #         new = current.left
        #         break
        #     elif value >= current.value and current.right is None:
        #         current.right = BinarySearchTree(value)
        #         new = current.right
        #         break
        # return new
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
        # if no root, return false
        # else: compare to root
        # if smaller, go left. if greater or ==, right
        # repeat steps until found
        # return True if found, False if doesn't exist
        while True:
            if current.value == None:
                return False
            elif target < current.value and current.left is not None:
                current = current.left
            elif target > current.value and current.right is not None:
                current = current.right
            elif target < current.value and current.left is None:
                return False
            elif target > current.value and current.right is None:
                return False
            elif target == current.value:
                return current.value

    # Return the maximum value found in the tree
    def get_max(self):
        # while you can go right, go right
        # return highest

        # current = self
        # while current.right is not None:
        #     current = current.right

        # return current.value

        # RECURSIVE
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if you can go left, go left
        # if you can't, go right
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # uses queue
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # stack?
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
