from __future__ import annotations

from betterbst import BetterBST
from data_structures import *
from minecraft_block import MinecraftBlock


class MinecraftChecklist:
    def __init__(self, blocks: ArrayR[MinecraftBlock]) -> None:
        """
        Initializes the MinecraftChecklist instance with a list of blocks.

        Complexity:
            Best Case Complexity: O(N logN)
            Worst Case Complexity: O(N logN)

            Where n is the number of blocks in the given array

        Justification:
            -) Firstly a key_value_pairs ArrayList is being created to store tuples of key(float) - value(MinecraftBlock) pairs. Next we create a better BST and insert the ArrayList of tuples to its __init__()
        """

        key_value_pairs = ArrayList(len(blocks))

        for block in blocks:
            ratio = block.item.value / block.hardness
            key_value_pairs.append((ratio, block))


        self.checklist = BetterBST(key_value_pairs)



    def __contains__(self, item: MinecraftBlock) -> bool:
        """
        Checks if the item is in the checklist.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(N)

            -) Where n is the number of blocks in the checklist

        Justification:
            Using in-order traversal find the required node using its name
            Best case occurs when the item in search is the first item in the checklist.
            Worst case occurs when the item in search is the last item in the checklist or not in the checklist at all.
        """
        for node in self.checklist:
            if node.item.name == item.name:
                return True
        return False

    def __len__(self) -> int:
        """
        Returns the number of blocks in the checklist.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            -) Retrieves the length of the bst using the __len__() method of BetterBST
            -) Constant-time access.
        """
        return len(self.checklist)

    def add_block(self, block: MinecraftBlock) -> None:
        """
        Adds a block to the checklist.

        Complexity:
            Best Case Complexity: O(log N)
            Worst Case Complexity: O(log N)

            Where n is the number of blocks in the checklist.

        Justification:

            -) Inserts one block at a time into BetterBST
            -) O(log N) time per insertion due that the tree is balanced


        """
        item_ratio = block.item.value // block.hardness
        self.checklist[item_ratio] = block

    def remove_block(self, block: MinecraftBlock) -> None:
        """
        Removes a block from the checklist.

        Complexity:
            Best Case Complexity: O(log N)
            Worst Case Complexity: O(log N)

            -) Where n is the number of blocks in the checklist.

        Justification:
            -) Deletion occurs via the value-hardness ratio as the key.
            -) In a balanced BST (Assume BST is always balanced) the key is found at O(log N) time due to the traversal cost
            -) Best/Worst case occurs when you need to traverse the BST to find the node to delete, and requires finding the successor
        """
        item_ratio = block.item.value // block.hardness
        del self.checklist[item_ratio]

    def get_sorted_blocks(self) -> ArrayR[MinecraftBlock]:
        """
        Returns the sorted blocks in the checklist.
        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity:  O(N)

            -) Where n is the number of blocks in the checklist

        Justification:
            -) Best and Worst case are both O(N). Cost of O(N) if due to the inorder traversal of the balanced BST
            -) Both appending items to the Arraylist and copying items to an ArrayR comes at a cost of O(N), here N also represents the length of the ArrayR to be constructed
        """
        sorted_block = ArrayList[MinecraftBlock]()

        for node in self.checklist:
            sorted_block.append(node.item)

        sorted_block_result = ArrayR[MinecraftBlock](len(sorted_block))

        for item in range(len(sorted_block)):
            sorted_block_result[item] = sorted_block[item]

        return sorted_block_result

    def get_optimal_blocks(self, block1: MinecraftBlock, block2: MinecraftBlock) -> ArrayR[MinecraftBlock]:
        """
        Returns the optimal blocks between two given blocks.
        Criteria 1:
            - Optimal blocks have a ratio of value to mining time more than the same ratio for block1.
        Criteria 2:
            - Optimal blocks have a ratio of value to mining time less than the same ratio for block2.
        Args:
            block1 (MinecraftBlock): The first block.
            block2 (MinecraftBlock): The second block.
        Returns:
            ArrayR: An array of optimal blocks between the two given blocks.
        Complexity:
            Best Case Complexity: O(log N)
            Worst Case Complexity: O(N)

            -) Where n is the number of total blocks.

        Justification:
            -) Best case complexity: is derived form the best case of filter_keys in betterbst.py at O(log N * (filter_func1 + filter_func2))
            -) Worst case complexity: is derived form teh worst case of filter_keys in betterbst.py at O(N * filter_func1 + filter_func2))

            -) All the items in ArrayList of 'optimal_keys' are copied back into ArrayR at a cost of O(K).
            -) Here K = the number of blocks that satisfy the filter.
            -) Therefore constructing the ArrayR occurs in O(K)
            -) However K <= N due that N is the total number of blocks. Hence O(N) dominates O(K) as a result the complexity becomes O(N)


        """
        block_1_ratio = block1.item.value / block1.hardness
        block_2_ratio = block2.item.value / block2.hardness

        maximum = max(block_1_ratio, block_2_ratio)
        minimum = min(block_1_ratio, block_2_ratio)

        optimal_keys = self.checklist.filter_keys(lambda ratio: ratio > minimum, lambda ratio: ratio < maximum)
        optimal_blocks = ArrayR[MinecraftBlock](len(optimal_keys))

        for item in range(len(optimal_keys)):
            optimal_blocks[item] = optimal_keys[item][1]

        return optimal_blocks
