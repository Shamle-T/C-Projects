from __future__ import annotations
from enum import auto, IntEnum
from config import Config
from data_structures import *

class CardColor(IntEnum):
    """
    Enum class for the color of the card
    """

    RED = 0
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    BLACK = auto()


    def __str__(self) -> str:
        """
        Method to return the string representation of the CardColor

        Args:
            None

        Returns:
            str: The string representation of the CardColor

        Complexity:
            O(1) → Constant time complexity for returning the name of CardColor

        """

        return(self.name)


class CardLabel(IntEnum):
    """
    Enum class for the value of the card
    """

    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    SKIP = auto()
    REVERSE = auto()
    DRAW_TWO = auto()
    CRAZY = auto()
    DRAW_FOUR = auto()


    def __str__(self) -> str:
        """
        Method to return the string representation of the CardLabel

        Args:
            None

        Returns:
            str: The string representation of the CardLabel

        Complexity:
            O(1) → Constant time complexity for returning the name of CardLabel

        """

        return(self.name)


class Card:
    def __init__(self, color: CardColor, label: CardLabel) -> None:
        """
        Initialize the card with the given color and value.

        Args:
            color (CardColor): The color of the card.
            value (CardValue): The value of the card.

        Returns:
            None

        Complexity:
            Best Case: O(1)
            Worst Case: O(1)

        Rationale:
        Assigning the class attributes: self.color and self.label is O(1). Hence, both best and Worst Cases are the same at O(1)

        """

        self.color = color
        self.label = label


    def __str__(self) -> str:
        """
        Return a string representation of the card.

        Optional method for debugging.

        Complexity:
            Best Case and Worst case are the same
            O(1) → Constant time complexity for returning the string representation of the card.
        """

        return(f"{self.color}, {self.label}")


    def __repr__(self) -> str:
        """
        Method to return the string representation of the Card

        Args:
            None

        Returns:
            str: The string representation of the Card

        Complexity:
            Best Case and Worst case are the same
            O(1) → Constant time complexity for returning String card representation
        """

        return str(self)


    def __eq__(self, other: Card) -> bool:
        """
        Check if this card is equal to another card.

        Args:
            other (Card): The other card to compare to.

        Returns:
            bool: True if this card is equal to the other card, False otherwise.

        Complexity:
            Best Case and Worst case are the same
            O(1) → Constant time complexity for returning the self.name Comparisons with the enum class values are of constant time complexity

        """

        if other is None:
            return False
        else:
            return self.color == other.color and self.label == other.label


    #New less than magic method
    def __lt__(self, other: Card) -> bool:
        """
       Check if this card is less than another card.

       Args:
           other (Card): The other card to compare to.

       Returns:
           bool: True if this card is less than the other card, False otherwise.

       Complexity:
            Best Case and Worst case are the same
            O(1) → Constant time complexity for returning the card with the lowest enum value depending on color or label

       """

        if other is None:
            return False

        if self.color == other.color:
            return self.label < other.label
        return self.color < other.color


    # New less than or equal to magic method
    def __le__(self, other: Card) -> bool:
        """
       Check if this card is less than or equal to another card.

       Args:
           other (Card): The other card to compare to.

       Returns:
           bool: True if this card is less than or equal to the other card, False otherwise.

       Complexity:
            O(1) → Constant time complexity for returning the card with the lowest or equal enum value depending on card

       """

        return self < other or self == other


    def get_playable_card(self, current_color: CardColor , current_label: CardLabel) -> bool:
        """
        Method to identify if the current card is playable

        Args:
            current_color (CardColor): The current card color on the gameboard.
            current_label (CardLabel): The current card label on the gameboard.

        Returns:
            bool: True if this card is playable, False otherwise.

        Complexity:
            Best case: O(1)  Both best and worst case scenarios are the same at O(1), since we ignore the cost of primitive type comparisons
            With the help of OR operator, if one of the comparisons, result True the rest of the operations in the line wont take place,
                thereby if the color of the first card is the current color,results to the fastest execution.
                Otherwise if the color is black this would result in processing through 2 OR conditions to receive the playable card, given that current card is playable.

            Worst case: O(1) the time complexity remains the same, given that everytime the playable card is black, for the if condition to capture this it would have to wait for 2 OR operations to finish

        """

        if self.color == current_color or self.label == current_label or self.color == CardColor.BLACK:
            return True
        else:
            return False
