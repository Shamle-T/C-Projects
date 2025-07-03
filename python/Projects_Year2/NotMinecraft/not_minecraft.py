from __future__ import annotations
from cave_system import CaveSystem, CaveNode
from data_structures import *
from data_structures.array_stack import ArrayStack
from minecraft_block import MinecraftBlock, MinecraftItem
from minecraft_checklist import MinecraftChecklist
from miner import Miner
from random_gen import RandomGen


class NotMinecraft:
    """
    A class representing a NotMinecraft game.
    """

    def __init__(self, cave_system: CaveSystem, checklist: MinecraftChecklist) -> None:
        """
        Initializes the NotMinecraft game.
        Args:
            cave_system (CaveSystem): The cave system for the game.
        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            -) Initializes the cave_system and checklist and creates a Miner instance.
        """
        self.miner = Miner("Steve")
        self.cave_system = cave_system
        self.checklist = checklist

    def dfs_explore_cave(self) -> ArrayList[MinecraftBlock]:
        """
        Performs a depth-first search (DFS) to explore the cave system and collect blocks.
        Returns:
            ArrayList[MinecraftBlock]: A list of collected blocks.
        Complexity:
            Not required
        """
        visited_cave_nodes = ArrayList[CaveNode]()
        stack_of_nodes = LinkedStack()
        explored_result = ArrayList[MinecraftBlock]()

        visited_cave_nodes.append(self.cave_system.entrance)
        stack_of_nodes.push(self.cave_system.entrance)

        while not stack_of_nodes.is_empty():
            node = stack_of_nodes.pop()

            for current_cave_node in range(len(node.blocks)):
                explored_result.append(node.blocks[current_cave_node])

            for current_node in range((len(node.neighbours)-1),-1,-1):
                neighbor = node.neighbours[current_node]


                already_visited_node = False
                for current_node_chk_visit in range(len(visited_cave_nodes)):
                    if visited_cave_nodes[current_node_chk_visit] == neighbor:
                        already_visited_node = True
                        break

                if not already_visited_node:
                    visited_cave_nodes.append(neighbor)
                    stack_of_nodes.push(neighbor)

        return explored_result

    def objective_mining_filter(self, blocks: ArrayList[MinecraftBlock], block1: MinecraftBlock,
                                block2: MinecraftBlock) -> ArrayList:
        """
        Given a list of blocks, filter the blocks that should be considered according to scenario 1.
        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.
            block1 (MinecraftBlock): Filtered blocks should have a ratio of value to mining time > block1.
            block2 (MinecraftBlock): Filtered blocks should have a ratio of value to mining time < block2.
        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N logC)

            -) N is the number of blocks in the ArrayList of blocks
            -) C is the number of elements in self.checklist

        Justification:
            -) Due to the iteration of all blocks the cost of objective_mining_filter is O(N)
            -) For each block the ratio is calculated at O(1)
            -) Best case occurs when item to be searched in the checklist is the first item in the checklist. Hence O(N)
            -) __contains__ magic method is used to check if the block is present in the checklist of blocks, this will result in O(C) in the worst case and O(log C) in the best case (since we assume the BST is always sorted)
        """

        obj_result = ArrayList[MinecraftBlock]()

        block1_ratio = block1.item.value / block1.hardness
        block2_ratio = block2.item.value / block2.hardness

        maximum = max(block1_ratio, block2_ratio)
        minimum = min(block1_ratio, block2_ratio)

        for current_block in range(len(blocks)):
            block = blocks[current_block]
            ratio = block.item.value / block.hardness
            if block in self.checklist:
                if minimum < ratio < maximum:
                    obj_result.append(block)

        return obj_result

    def objective_mining(self, blocks: ArrayList[MinecraftBlock]) -> None:
        """
        Mines the cave system to achieve the objective of collecting blocks.
        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N log N)

            -) Where N is the number of blocks in the ArrayList of blocks

        Justification:
            -) Heapify occurs in O(N) at both the best and the worst cases
            -) Best case and Worst case of get_max() occurs in: O(1) and O(log N) respectively
            -) mine() costs O(log N)
            -) get_max() best case and worst case respectively is O(1) and O(logn)
            -) Each call to get_max() removes the max element from the heap and at the same time performs a sink operation at O(logN)
            -) get_max() and mine() is repeated for N number of blocks , as a result the total number of get_max operations will result in O(N logN)

        """
        ratio_block_pairs = ArrayList()

        for current_block in range(len(blocks)):
            block = blocks[current_block]
            ratio = block.item.value / block.hardness
            ratio_block_pairs.append((ratio, block))

        mining_max_heap = MaxHeap.heapify(ratio_block_pairs)

        while len(mining_max_heap):
            ratio, block_to_mine = mining_max_heap.get_max()

            self.miner.mine(block_to_mine)


    def objective_mining_summary(self, blocks: ArrayList[MinecraftBlock], block1: MinecraftBlock,
                                 block2: MinecraftBlock) -> None:
        """
        Returns the summary of the objective mining.
        This is to explain how objective mining will be called and tested.
        Complexity:
            Not Required
        """
        filtered_blocks = self.objective_mining_filter(blocks, block1, block2)

        self.chicken_jockey_attack(filtered_blocks)

        self.objective_mining(filtered_blocks)

    def profit_mining(self, blocks: ArrayList[MinecraftBlock], time_in_seconds: int) -> None:
        """
        Mines the cave system casually.
        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.
            time_in_seconds (int): The time in seconds to mine.

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N + K logN)

            -) Where N is the number of blocks in the ArrayList of blocks
            -) Where K is the number of blocks which have been mined


        Justification:
            -) Building the ArrayList requires O(N) time complexity, to insert the tuples into 'ratio_block_pairs'
            -) Heapify occurs at a time complexity cost of O(N)
            -) Mining of blocks upto K blocks requires O(log N) per blocks = O(K logN)
            -) get_max() and mine() is repeated for N number of blocks , as a result the total number of get_max operations will result in O(N logN)
        """

        time_taken = 0.0
        ratio_block_pairs = ArrayList()

        for current_block in range(len(blocks)):
            block = blocks[current_block]
            ratio = block.item.value / block.hardness
            ratio_block_pairs.append((ratio, block))

        mining_max_heap = MaxHeap.heapify(ratio_block_pairs)

        while len(mining_max_heap):
            ratio, high_block = mining_max_heap.get_max()

            if time_taken + high_block.hardness <= time_in_seconds:
                time_taken += high_block.hardness
                self.miner.mine(high_block)

    def chicken_jockey_attack(self, blocks: ArrayList[MinecraftBlock]) -> None:
        """
        Chicken Jockey Attack
        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.
        Complexity:
            Not required
        """
        RandomGen.random_shuffle(blocks)

    def main(self, scenario: int, **criteriaArgs) -> None:
        """
        Main function to run the NotMinecraft game.
        Args:
            scenario (int): The scenario number to run.
            criteriaArgs (dict): Additional arguments for the scenario.
        Complexity:
            Not required
        Sample Usage:
            not_minecraft = NotMinecraft(cave_system, checklist)
            not_minecraft.main(1, block1=block1, block2=block2)
            not_minecraft.main(2, time_in_seconds=60)
        """
        if scenario == 1:
            blocks = self.dfs_explore_cave()
            self.objective_mining_summary(blocks, **criteriaArgs)
        elif scenario == 2:
            blocks = self.dfs_explore_cave()
            self.profit_mining(blocks, **criteriaArgs)
