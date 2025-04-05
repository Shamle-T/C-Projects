from __future__ import annotations
from card import Card, CardColor, CardLabel
from config import Config
from data_structures import *



class Player:
    """
    Player class to store the player details
    """

    def __init__(self, name: str) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player

        Returns:
            None

        Complexity:
            Best Case Complexity: is O(N) where N is the length of ArraySortedList at initialization.
            Initializing the ArraySortedList calls ArrayR(size) to create a list of size specified in the Config file.
            Creation of hand sorted array involves using a for loop in referential_array.py, causing the complexity to be O(max_capacity).
            As a result Player __init__ method attains a Complexity of O(N).

            Worst Case Complexity: is the same at O(N) since initializing the Player class requires to create a list of fixed size .

        Using ArraySortedList Rationale:
            self.hand is declared as a SortedArray: due that when player, plays the card, the first card that matches the same color or label as the gameboard current card can be chosen easily, making it easier to obtain the playable card from each player.
        """

        self.playable_card = None
        self.name = name
        self.hand = ArraySortedList(Config.NUM_CARDS_AT_INIT)


    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Finding the position to add the card is O(logN) which occurs in both best and worst case scenarios

            Best Case Complexity: O(N) when resizing of the SortedList does not occur, still the card is checked of the middle value

            Worst Case Complexity: O(N) When the size of SortedList is not sufficient for adding a card, hence resizing must be done O(N)

            Hence both the best and worst cases are of O(N)
        """

        self.hand.add(card)


    def is_empty(self) -> bool:
        """
        Method to check if the player's hand is empty

        Args:
            None

        Returns:
            bool: True if the player's hand is empty, False otherwise

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

            Both best and worst cases are the same since the equality comparison operator is of constant time complexity.
        """

        if self.hand == []:
            return True
        else:
            return False


    def cards_in_hand(self) -> int:
        """
        Method to check the number of cards left in the player's hand

        Args:
            None

        Returns:
            int: The number of cards left in the player's hand

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

            Both best and worst cases are the same since using len() is of constant time complexity
        """

        return len(self.hand)


    def play_card(self, current_color: CardColor, current_label: CardLabel) -> Card | None:
        """
        Method to play a card from the player's hand

        Args:
            current_color (CardColor): The current color of the game
            current_label (CardLabel): The current label of the game

        Returns:
            Card: The first card that is playable from the player's hand, None otherwise

        Complexity:
            Best Case Complexity: O(1) if the playable card is the first card in the players hand
            Worst Case Complexity: O(N) if the playable card is the last card in the players hand. Here N is the last card in the hand
        """

        if not self.is_empty():

            self.playable_card= None

            for index in range (len(self.hand)):

                current_card = self.hand[index]
                if self.hand[index] is not None:
                    if current_card.get_playable_card(current_color, current_label):
                        self.hand.remove(current_card)
                        return current_card

                else:
                     return self.playable_card


    def __str__(self) -> str:

        """
        Return a string representation of the player.

        Optional method for debugging.

        Complexity : O(1) Best Case and Worst case are the same
            Constant time complexity for returning the string representation of the players name and hand.

        """

        return f"Player {self.name}, {self.hand}"


    def __repr__(self) -> str:
        """
        Method to return the string representation of the player

        Args:
            None


        Returns:
        str: The string representation of the player

        Complexity: O(1) as Best Case and Worst case are the same
            Constant time complexity for returning String player representation

        """

        return str(self)
