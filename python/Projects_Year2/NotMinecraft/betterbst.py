from __future__ import annotations
from collections.abc import Callable

from typing import Tuple, TypeVar

from algorithms.mergesort import mergesort
from data_structures import *

K = TypeVar('K')
I = TypeVar('I')


class BetterBST(BinarySearchTree[K, I]):
    def __init__(self, elements: ArrayList[Tuple[K, I]]) -> None:
        """
        Initialiser for the BetterBST class.
        We assume that the all the elements that will be inserted
        into the tree are contained within the elements ArrayList.

        As such you can assume the length of elements to be non-zero.
        The elements ArrayList will contain tuples of key, item pairs.

        First sort the elements ArrayList and then build a balanced tree from the sorted elements
        using the corresponding methods below.

        Args:
            elements(ArrayList[tuple[K, I]]): The elements to be inserted into the tree.

        Complexity:
            Best Case Complexity: O(N logN)
            Worst Case Complexity: O(N logN)

            -) Where n is the number of elements in the input list (elements)

        Justification:
            -) Sorting elements using __sort_elements() -> O(N logN)
            -) Building balanced tree using __build_balanced_tree() -> O(N log N )
            -) Sorting N elements via merge sort and building the tree using the sorted list of numbers

        """
        super().__init__()
        new_elements: ArrayList[Tuple[K, I]] = self.__sort_elements(elements)
        self.__build_balanced_tree(new_elements)

    def __sort_elements(self, elements: ArrayList[Tuple[K, I]]) -> ArrayList[Tuple[K, I]]:
        """
        Recall one of the drawbacks to using a binary search tree is that it can become unbalanced.
        If we know the elements ahead of time, we can sort them and then build a balanced tree.
        This will help us maintain the O(log n) complexity for searching, inserting, and deleting elements.

        Args:
            elements (ArrayList[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            ArrayList(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            Best Case Complexity: O(N logN) where N is the length of the list and comp is the cost of comparison for the object type T (the elements in the list).
            Worst Case Complexity:  O(N logN) where N is the length of the list and comp is the cost of comparison for the object type T (the elements in the list).

        Justification:
            -) Complexity depends on mergesort
            -) Depending on the type of comparisons the complexity will change, therefore we receive comp(T) complexity for comparison complexity, this is multiplied by the number of the number of elements in teh list

        """
        return mergesort(elements)

    def __build_balanced_tree(self, elements: ArrayList[Tuple[K, I]]) -> None:
        """
        This method will build a balanced binary search tree from the sorted elements.

        Args:
            elements (ArrayList[Tuple[K, I]]): The elements we wish to use to build our balanced tree.

        Returns:
            None

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)


            Best Case Complexity: O(N log N ) - Occurs when the tree remains balanced, and the complexity of the comparison are simple
            Worst Case Complexity: O(N log N ) - Occurs when the tree remains balanced, but the complexity of the comparisons are complex depending on the data type
                -) where R refers to the number of insertions into the BST, depending on the number of elements in the input list
                -) log N, where N refers to the height of the tree


        Justification:
            -) Best and worst case occurs when the tree is balanced. In this case the tree always remains balanced, due that we are passing a sorted arrayList
            -) As a result we add the midpoint of the sorted arrayList to bst using the insert_aux (using the __setitem__ method).
            -) In insert_aux, the midpoint of the sorted arrayList is inserted at the root.
            -) Therefore when building the tree we cannot build an unbalanced BST since we pass a sorted arrayList. Which allows both the complexities to be similar

            -) Initial N refers to the number of insertions . When building the left and right subtrees.
                Where log N refers to its depth, which is required when traversing through the bst to find the location to insert the new node.
                Compk refers to the complexity of the comparison types

            Complexities of magic methods in respective data types:
                __getitem__ complexities from array_list.py:
                    Best and Worst Case Complexity :  complexity: O(1) / (raises IndexError: if index is out of bounds)

                __setitem__ complexities from bst.py: (insert_aux)
                    Best case complexity: O(CompK) inserts the item at the root.
                    Worst case complexity: O(CompK * N) where N is the number of elements in the tree and the tree is unbalanced

            -) Complexity of the setter method is as defined above from insert_aux in bst.py and, Complexity of the getter method is O(1) in elements (for ArrayList)

        """

        def build_tree(start, end):

        #     Obtain the midpoint of the sorted array and create the first node using that, as the root node
            if start  > end:
                return

            midpoint = (start + end) // 2

            key, item = elements[midpoint]  #Makes use of __getitem__

            # Action statement where the bst is built using the setter method
            self[key] = item        #Makes use of __setitem__

            # Building the left and right subtree - Recursion occurs here
            build_tree(start, midpoint-1)
            build_tree(midpoint+1, end)


        build_tree(0,len(elements)-1)


    def filter_keys(self, filter_func1: Callable[[K], bool], filter_func2: Callable[[K], bool]) -> ArrayList[Tuple[K, I]]:
        """
        Filters the keys in the tree based on two criteria.

        Args:
            filter_func1 (callable): A function that takes a value and returns True if the key is more than criteria1.
            filter_func2 (callable): A function that takes a value and returns True if the key is less than criteria2.
        Returns:
            ArrayList[Tuple[K, I]]: An ArrayList of tuples containing Key,Item pairs that match the filter.

        Complexity:
            Best Case Complexity: O(log N * (filter_func1 + filter_func2)) ( During best case not all nodes are traversed, only the large parts of the tree are pruned based on the filter functions, in a balanced tree)
            Worst Case Complexity: O(N * filter_func1 + filter_func2))  (All nodes are visited since the filter accommodates to match all the nodes, in an unbalanced tree)

            -) Where N is the number of nodes in the tree.

        Justification:
            -) Append complexity (using insert in ArrayList)
                Best case complexity: O(len(self)) : O(1)
                Worst case complexity: O(N), for list of length N.


        """

        filter_key_result = ArrayList[Tuple[K, I]]()

        def inorder(node):
            if node is None:
                return

            if filter_func1(node.key):
                inorder(node.left)

            if filter_func1(node.key) and filter_func2(node.key):
                filter_key_result.append((node.key, node.item))

            if filter_func2(node.key):
                inorder(node.right)

        inorder(self.root)
        return filter_key_result
