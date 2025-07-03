from __future__ import annotations

from data_structures import HashTableSeparateChaining
from enums import PlayerPosition

# Do not change the import statement below
# If you need more modules and classes from datetime, do not use
# separate import statements. Use them from datetime like this:
# datetime.datetime, or datetime.date, etc.
import datetime


class Player:

    def __init__(self, name: str, position: PlayerPosition, age: int) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (PlayerPosition): The position of the player
            age (int): The age of the player

        Complexity:
            Best Case Complexity: O(1)
                Constructor sets up the attributes and assigns them. self.statistics is assigned by creating a HashTableSeparateChaining using a fixed default of 17 spots.
                Which is required by its constructor in HashTableSeparateChaining class

            Worst Case Complexity: O(1) Same as best case with a deafult size of 17 spots.

        Justification:
            I have not used the lazy double table due to its complexity in double hashing which is not required to map a simple statistic, and is unnecessary for our current requirements
        """
        self.name = name
        self.position = position
        self.goals = 0
        self.statistics = HashTableSeparateChaining()   #using linked lists

        CURRENT_YEAR = datetime.datetime.now().year
        self.age = CURRENT_YEAR - age


    def reset_stats(self) -> None:
        """
        Reset the stats of the player.
        
        This doesn't delete the existing stats, but resets them to 0.
        I.e. all stats that were previously set should still be available, with a value of 0.

        Complexity:
            Best Case Complexity: O(C+T)
                In the for loop, using keys will return the complexity of (C+T)
                At each set item instance to set it to 0 we need to call __setitem__ which finds the bucket and set the value with a complexity of O(T)

            Worst Case Complexity: O(C + T^2 + T·L)
                Occurs when all entries are hashed into one spot of the hash table.
                Use of .keys() to collect all the keys from the player statistics using (C+T)
                Each of the multiple stats need to be reset to 0.
                Complexity = T · O(T + L)

        C = number of spots in the hash table (TABLE SIZE)
        T = total number of statistics stored
        L = length of a STRING key of the statistic
        """
        for stat_keys in self.statistics.keys():
            self.statistics[stat_keys] = 0

    def __setitem__(self, statistic: str, value: int) -> None:
        """
        Set the given value for the given statistic for the player.

        Args:
            statistic (string): The key of the stat
            value (int): The value of the stat

        Complexity:
            Best Case Complexity: O(L)
                Instantly assigns each value in the statistic to the value passed in the parameter

            Worst Case Complexity: O(T+L) Same for both sceanrios
                Occurs when all entries are hashed into one spot of the hash table.
                Before appending or updating, the algorithm scans the chains beforehand

            O(L) refers to the resulting hash value
        """
        self.statistics[statistic] = value

    def __getitem__(self, statistic: str) -> int:
        """
        Get the value of the player's stat based on the passed key.

        Args:
            statistic (str): The key of the stat

        Returns:
            int: The value of the stat

        Complexity:
            Best Case Complexity: O(L) Returns the current players statistics

            Worst Case Complexity: O(T+L) Same for both sceanrios
                Occurs when traversing through the items in the chain, until the desired key is found.
        """
        return self.statistics[statistic]

    def get_age(self) -> int:
        """
        Get the age of the player

        Returns:
            int: The age of the player

        Complexity:
            Best Case Complexity: O(1) returns the age of the player based on the current year
            Worst Case Complexity: O(1) Same as best case

        Import statement's complexity is assumed to be O(1)
        """

        CURRENT_YEAR = datetime.datetime.now().year
        return CURRENT_YEAR - self.age


    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the player object.

        Complexity Analysis not required.
        """
        return f"Player name: {self.name}, age: {self.age}, play position: {self.position}, goals: {self.goals}, statistics: {self.statistics}"

    def __repr__(self) -> str:
        """ String representation of the Player object.
        Useful for debugging or when the Player is held in another data structure.
        """
        return str(self)
