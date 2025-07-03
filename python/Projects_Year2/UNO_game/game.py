from __future__ import annotations
import card
from player import Player
from game_board import GameBoard
from card import CardColor, CardLabel, Card
from random_gen import RandomGen
from config import Config
from data_structures import *


class Game:
    """
    Game class to play the game
    """

    def __init__(self) -> None:
        """
        Constructor for the Game class

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            Both best and worst cases are the same as the variables are only assigned here
        """

        self.current_card = None
        self.temp_nextPlayer = None

        self.players = None
        self.game_board = None

        self.playable_card = None
        self.current_label = None
        self.currentPlayer = None
        self.current_color = None

        self.card_list = None
        self.current_round_Player = None


    def generate_cards(self) -> ArrayList[Card]:
        """
        Method to generate the cards for the game

        Args:
            None

        Returns:
            ArrayList[Card]: The list of Card objects generated
        """

        list_of_cards: ArrayList[Card] = ArrayList(Config.DECK_SIZE)
        idx: int = 0

        # Generate 4 sets of cards from 0 to 9 for each color
        for color in CardColor:
            if color != CardColor.BLACK:
                # Generate 4 sets of cards from 0 to 9 for each color
                for i in range(10):
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1

                # Generate 2 of each special card for each color
                for i in range(2):
                    list_of_cards.insert(idx, Card(color, CardLabel.SKIP))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.REVERSE))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.DRAW_TWO))
                    idx += 1
            else:
                # Generate black crazy and draw 4 cards
                for i in range(4):
                    list_of_cards.insert(idx, Card(CardColor.BLACK, CardLabel.CRAZY))
                    idx += 1
                    list_of_cards.insert(
                        idx, Card(CardColor.BLACK, CardLabel.DRAW_FOUR)
                    )
                    idx += 1

                # Randomly shuffle the cards
                RandomGen.random_shuffle(list_of_cards)

                return list_of_cards



    def initialise_game(self, players: ArrayList[Player]) -> None:
        """
        Method to initialise the game

        Args:
            players (ArrayList[Player]): The list of players

        Returns:
            None

        Complexity:
                Populating the cards to each player happens in both scenarios. Where the outer loop traverses through the number of rounds which is N,
                for each of these rounds the inner loop runs to hand a card to each player which is M.
                The inner loop runs for the number of players and the outer loop runs for the set amount of cards each player must have in the beginning.
                Hence, when n = 1, m = 1 and when n = 1, m = 2 which is O(N*M), which grows much faster than O(NlogN)
                game_board.draw_card() has a best case: O(1) if the draw pile is not empty and worst case: O(NlogN) if the draw pile is empty, it needs to be reshuffled at the expense of O(NlogN)
                when adding the card add_card has the best case of O(log N) and worst case of O(N)

            Best Case Complexity: O(N*M) or O(N^2logN) if the add_card() is in best case → O(logN) and draw_card() in best case → O(1) and if the first card is a number card, then the while loop only has to run once before termination.
            However, the 2 for loops dominate the complexity at O(N*M)

            Worst Case Complexity: O(N) if the first card is not a number card, another card will have to be draw.
            causing the while loop to run a number of times and if the draw pile runs out, the reshuffle() method will need to be called at the expense of O(NlogN). But still O(N*M) dominates O(NlogN)
            In the for loop the worst case for draw_card() → O(NlogN) and add_card() → O(N). This chains to a complexity of O(N^2logN)

            As a result the best case time complexity is O(N*M)
            The worst case is dependent on N and M, such that: Firstly, if M grows faster than NlogN, then O(N*M) is larger. or if M grows slower than N log N, then O(N^2logN) is larger. However, if M = (NlogN), then they are of the same order.
        """

        self.players = players

        self.card_list = self.generate_cards()

        self.game_board = GameBoard(self.card_list)

        for round in range(Config.NUM_CARDS_AT_INIT):
            for initial_player in self.players:
                initial_player.add_card(self.game_board.draw_card())

        start_card = self.game_board.draw_card()

        while True:
            if  (start_card.label <= 9):
                self.current_card = start_card
                self.current_label = self.current_card.label
                self.current_color = self.current_card.color
                break
            else:
                self.game_board.discard_card(start_card)
                start_card = self.game_board.draw_card()


    def next_player(self) -> Player:
        """
        Method to get the next player

        Args:
            None

        Returns:
            Player: The next player

        Complexity:
            Best Case Complexity: O(1) if the current player is None, which occurs at the beginning of the game
            Worst Case Complexity: O(N) if the current player is not None,
                and the current player is the last player, the index to add can be found at an expense of O(N), which would result in iterating over all the other players.
        """

        if self.currentPlayer == None:
            next_player = self.players[0]
            self.current_round_Player = self.players[0]
        else:
            next_player = self.players[((self.players.index(self.currentPlayer) + 1) % len(self.players))]

        return next_player


    def reverse_players(self) -> None:
        """
        Method to reverse the order of the players

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)
            In both Cases the time complexity is O(N/2) due to the division in the for loop which simplifies to O(N), Here N corresponds to the number of players in the player list len(self.players).
                Due that the swapping occurs using temporary variables the time complexity of each iteration is O(1).
        """

        #Reversal of self.players using swapping
        for player in range(len(self.players)//2):
            get_opposite_index = ((len(self.players) - 1) - player)
            self.players[player], self.players[get_opposite_index] = (self.players[get_opposite_index],self.players[player])


    def skip_next_player(self) -> None:
        """
        Method to skip the next player in the game

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            Both the best and Worst cases are the same since it is a general assignment of the current player
        """

        self.currentPlayer = self.next_player()


    def play_draw_two(self) -> None:
        """
        Method to play a draw two card

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(B) Once the temp_nextPlayer receives 2 cards from the for loop which runs at O(1), indicating the number of additional cards to be added
            when .draw_card() is called the best case scenario runs at O(1)
            when .add_card is called the best case scenario runs at O(B)
            Since the dominant time complexity is from .add_card(), the resulting best Case Complexity is O(1)

            Worst Case Complexity: O(NlogN) + O(B) When the player goes into the loop, temp_nextPlayer receives 2 cards from the for loop which runs at O(1), indicating the number of additional cards to be added
            when .draw_card() is called the worst case scenario runs at O(NlogN)
            when adding the card using add_card() has the worst case of O(B)
            As a result the dominant time Case Complexity is O(NlogN) + O(B)

        """

        self.temp_nextPlayer = self.next_player()

        for card_Count in range (2):
            self.temp_nextPlayer.add_card(self.game_board.draw_card())

        self.skip_next_player()


    def play_black(self, card: Card) -> None:
        """
        Method to play a crazy card

        Args:
            card (Card): The card to be played

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1) due to the comparison operators used to validate the color and label of the card.
            If the label is not found as DRAW_FOUR then skip to next player, of which all operations are done in O(1)


            Worst Case Complexity: O(NlogN) + O(B) if the card is a DRAW_FOUR card, 4 additional cards has to be added to the current players hand using the for loop which runs at O(1) indicating the number of cards that needs to be added.
            when draw_card() is called it has 2 scenarios, in which the worst case happens if the draw pile is empty, where it needs to be reshuffled at the expense of O(NlogN). Here N represents the card from the draw pile.
            when adding the card add_card has the best case of O(B) and worst case of O(B). Here B represents the card being added to the current player.
            Once we chain them together we get the resulting time complexity : O(NlogN) + O(B)

        """

        random_colour = CardColor(RandomGen.randint(0,3))
        self.current_color = random_colour

        if card.label == CardLabel.DRAW_FOUR:
            self.temp_nextPlayer = self.next_player()


            #Checks for +4 card
            for card_count in range (4):
                self.temp_nextPlayer.add_card(self.game_board.draw_card())

        self.skip_next_player()


    def draw_card(self, player: Player, playing: bool) -> Card | None:
        """
        Method to draw a card from the deck

        Args:
            player (Player): The player who is drawing the card
            playing (bool): A boolean indicating if the player is able to play the card

        Returns:
            Card - When drawing a playable card, other return None

        Complexity:
            Best Case Complexity: O(1) if the drawn_card is played immediately

            Worst Case Complexity: O(NlogN) + O(B) occurs when the draw pile is empty, causing a reshuffle at a time complexity of O(NlogN), N is the number of cards in the draw_pile.
                 add_card() has a best case time complexity at O(B) and a worst case time complexity at O(B) where the list needs to be resized(). Here the N represents the cards at hand of the player.
                 However, it is important to note that the O(N) from add_card() is different from the N in draw_card(), Hence add_card() N can be considered as B, where B = O(N).
                 Therefore, the overall time complexity is O(NlogN) + B
        """

        drawn_card = self.game_board.draw_card()

        if playing is True:
            if drawn_card.color == CardColor.BLACK or drawn_card.label == self.current_label or drawn_card.color == self.current_color:
                return drawn_card

        player.add_card(drawn_card)
        return None


    def play_game(self) -> Player:
        """
        Method to play the game

        Args:
            None

        Returns:
            Player: The winner of the game
        """

        while len(self.game_board.draw_pile) != 0 :

            self.currentPlayer = self.next_player()

            self.playable_card = self.currentPlayer.play_card(self.current_color, self.current_label)

            #Adds a card if the player does not have any playable cards
            if self.playable_card is None:
                draw_card = self.draw_card(self.currentPlayer, True) #GETS NEW CARD

                if draw_card:
                    self.playable_card = draw_card
                    self.current_card = draw_card
                else:
                    continue

            self.current_card = self.playable_card

            self.game_board.discard_card(self.playable_card)

            self.current_color = self.playable_card.color
            self.current_label = self.playable_card.label


            if self.currentPlayer.hand.is_empty():
                return self.currentPlayer
            else:

                if self.playable_card.color is CardColor.BLACK:
                    self.play_black(self.playable_card)

                if self.playable_card.label == CardLabel.REVERSE:
                    self.reverse_players()

                if self.playable_card.label == CardLabel.SKIP:
                    self.skip_next_player()

                if self.playable_card.label == CardLabel.DRAW_TWO:
                    self.play_draw_two()



