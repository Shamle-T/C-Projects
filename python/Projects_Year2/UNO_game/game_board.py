from __future__ import annotations
from card import Card
from random_gen import RandomGen
from config import Config
from data_structures import *



class GameBoard:
    """
    GameBoard class to store cards in draw pile and discard pile
    """

    def __init__(self, cards: ArrayList[Card]):
        """
        Constructor for the GameBoard class

        Args:
            cards (ArrayList[Card]): The list of cards to be used in the game

        Returns:
            None

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)
            Both best and worst case Complexity: O(N) since we are creating a Circular Queue and an ArrayStack of fixed size

        Data Structure Rationale:
        draw pile is implemented using a ArrayStack : This portrays an efficient method of handling the draw process as the card drawn last will be played first according to LIFO principle
             Add card to draw discard using push() → O(1) and Remove card from draw discard using pop() → O(1)

        discard pile is implemented using an ArrayList : The stack shares its properties with the discard pile. Using a list enables the random_shuffle() method to be called since the List is iterable unlike Stack or Queue
            Add card to draw discard using append() → O(1) and Remove card from draw discard using remove() → O(len(self) - index) (However we dont need to call the, remove() function)

        """

        self.draw_pile = ArrayStack(Config.DECK_SIZE)
        self.discard_pile = ArrayList(Config.DECK_SIZE)


        for current_card in range(len(cards)-1,-1,-1):
            self.draw_pile.push(cards[current_card])


    def discard_card(self, card: Card) -> None:
        """
        Discards the specified card from the player's hand.

        Args:
            card (Card): The card to be discarded.

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            Both best and Worst cases are the same as the discard pile
        """

        self.discard_pile.append(card)


    def reshuffle(self) -> None:
        """
        Reshuffles cards from the discard pile and add them back to the draw pile.

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(NlogN)
            Worst Case Complexity: O(NlogN)
            Best and Worst case is same in both cases due to the random_shuffle() method at a cost of O(NlogN), where N is the number of cards in the discard pile.
            Pushing to the stack is performed in constant time complexity at O(1)

        """

        RandomGen.random_shuffle(self.discard_pile)

        for current_card in range (len(self.discard_pile)-1,-1,-1):
            self.draw_pile.push(self.discard_pile[current_card])
        self.discard_pile.clear()


    def draw_card(self) -> Card:
        """
        Draws a card from the draw pile.

        Args:
            None

        Returns:
            Card: The card drawn from the draw pile.

        Complexity:
            Best Case Complexity: O(1) if the draw pile is not empty
            Worst Case Complexity: O(NlogN) if the draw pile is empty, it needs to be reshuffled at the expense of O(NlogN)
        """

        if self.draw_pile.is_empty():
            self.reshuffle()

        return self.draw_pile.pop()



