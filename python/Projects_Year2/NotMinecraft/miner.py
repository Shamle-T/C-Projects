from __future__ import annotations
from typing import Iterable

from data_structures import *
from minecraft_block import MinecraftBlock, MinecraftItem


class Miner:
    """
    A class representing a miner in a mining simulation.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the miner with a name and an empty inventory.
        Args:
            name (str): The name of the miner.
        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        Justification:
            -) Creating a string : O(1)
            -) Creating an ArrayList of MinecraftItem objects : O(1)
            -) Both occur at constant time : O(1)
        """
        self.name = name
        self.inventory = ArrayList[MinecraftItem]()


    def mine(self, block: MinecraftBlock) -> None:
        """
        Mines a block and adds the item to the miner's bag.

        Args:
            block (MinecraftBlock): The block to be mined.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(N)

            -) Where N is the size of the current inventory

        Justification:
            -) Both the best case and worst case can be amortized to O(1)
            -) If no resizing is needed appending to the ArrayList is O(1)
            -) However in the worst case, the complexity is O(N) due to expanding the arrayList


            """
        self.inventory.append(block.item)

    def clear_inventory(self) -> Iterable:
        """
        Clears the miner's inventory and returns what he had in the inventory before the clear.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            -) Replaces the previous inventory with the new inventory, and a reference of the previous inventory is stored in 'previous_inventory'
        """
        self.previous_inventory = self.inventory
        self.inventory = ArrayList[MinecraftItem]()

        return self.previous_inventory

    def __str__(self) -> str:
        return f"Miner: {self.name}"
