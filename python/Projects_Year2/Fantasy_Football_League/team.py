from __future__ import annotations

from typing import Collection, TypeVar

from data_structures import HashTableSeparateChaining, LinkedList, ArrayList, LinkedQueue
from data_structures.referential_array import ArrayR
from enums import TeamGameResult, PlayerPosition
from hashy_date_table import HashyDateTable
from player import Player

T = TypeVar("T")


class Team:



    position_list = tuple(PlayerPosition)

    def __init__(self, team_name: str, initial_players: ArrayR[Player], history_length: int) -> None:
        """
        Constructor for the Team class

        Args:
            team_name (str): The name of the team
            initial_players (ArrayR[Player]): The players the team starts with initially
            history_length (int): The number of `GameResult`s to store in the history

        Returns:
            None

        Complexity:
            Best Case Complexity:  O(N * K)
                Occurs when players in the initial player list are added to the Linked List O(N).
                When they are added we need to perform a hash which requires O(K)

            Worst Case Complexity: O(N * K)
                Same as the best case

        Justification:
            initial_players -> Implemented with HashTable, using LinkedLists this is due that each player has a position which it needs to be mapped to in the hash table, making lookups, appending, deletion much easier at O(1)
            history_length -> Implemented with circular queue


        Let N be the number of players in the original team list (initial_players).
        Let P represent the current total number of players on the team.
        Let H be the current number of entries in the history log, with a maximum of history_length.
        Let M be the number of blog posts that have already been created.
        Let K be the average character length of any string key (like player positions or blog post dates).
        """
        self.name = team_name

        self.players = HashTableSeparateChaining()
        self.post = HashyDateTable()
        self.history = LinkedQueue()

        self.initial_players = initial_players
        self.history_length = history_length
        self.points = 0


        #Sets all the players to the hashtable using linkedLists
        for current_player in self.initial_players:
            self.add_player(current_player)



    def add_player(self, player: Player) -> None:
        """
        Adds a player to the team.

        Args:
            player (Player): The player to add

        Returns:
            None

        Complexity:
            Best Case Complexity: O(K)
                Occurs if the player Position is valid, and a LinkedList for the player has already been created.
                Appending occurs at the end which add the player object to the end of the list.

            Worst Case Complexity: O(K + P)
                Occurs when a LinkedList does not exist for the player position and a new one has to be created for the position.

                Once created the player has to be added to the Linked List
        """
        #for position_types in PlayerPosition:
        position_key = player.position.value

        if position_key not in PlayerPosition:
            raise ValueError(f"Invalid position {player.position}")

        if position_key not in self.players:
            self.players[position_key] = LinkedList()

        self.players[position_key].append(player)



    def remove_player(self, player: Player) -> None:
        """
        Removes a player from the team.

        Args:
            player (Player): The player to remove

        Returns:
            None

        Complexity:
            Best Case Complexity: O(K)
                Occurs when the hash finds the correct list using the spot O(K).
                Deletion is always O(1)

            Worst Case Complexity: O(K+P)
                Occurs when we traverse through items using the table using the hash to find a match O(K)
                Once found we need to delete the item at the index O(P)

        """

        player_key = player.position.value
        if player_key not in self.players:
            raise ValueError(f"Invalid position of player {player.position}")

        current_position_slot = self.players[player_key]
        for current_player in range(len(current_position_slot)):
            if current_position_slot[current_player] == player:
                current_position_slot.delete_at_index(current_player)


        # raise ValueError(f"Invalid position of player: {player.position}")

    def get_players(self, position: PlayerPosition | None = None) -> Collection[Player]:
        """
        Returns the players of the team that play in the specified position.
        If position is None, it should return ALL players in the team.
        You may assume the position will always be valid.
        Args:
            position (PlayerPosition or None): The position of the players to return

        Returns:
            Collection[Player]: The players that play in the specified position
            held in a valid data structure provided to you within
            the data_structures folder.
            
            This includes the ArrayR, which was previously prohibited.

        Complexity:
            Best Case Complexity: O(K)
                Occurs when we pass a correct/specific position , and using the hash lookup, we receive the existing list O(1)

            Worst Case Complexity: O(P)
                Occurs when the position = None , which will require you to visit every player.
        """

        if position is None:
            result = ArrayList()
            for current_position in PlayerPosition:
                for player in self.players[current_position.value]:
                    result.append(player)
            return result

        else:
            return self.players[position.value]


    def add_result(self, result: TeamGameResult) -> None:
        """
        Add the `result` to this `Team`'s history

        Args:
            result (GameResult): The result to add
            
        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

            Length check  using len() and appending the result
            Adds an integer value to the individual points of the teams points using the ENUM class
        """

        if len(self.history) < self.history_length:
            self.history.append(result)
            self.points += result.value


    def get_history(self) -> Collection[TeamGameResult] | None:
        """
        Returns the `GameResult` history of the team.
        If the team has played less than this team's `history_length`,
        return all the result of all the games played so far.

        For example:
        If a team has only played 4 games and they have:
        Won the first, lost the second and third, and drawn the last,
        the result should be a container with 4 objects in this order:
        [GameResult.WIN, GameResult.LOSS, GameResult.LOSS, GameResult.DRAW]

        If this method is called before the team has played any games,
        return None the reason for this is explained in the specification.

        Returns:
            Collection[GameResult]: The most recent `GameResult`s for this team
            or
            None if the team has not played any games.

        Complexity:
            Best Case Complexity: O(1)
                Occurs when there are no games played.
                Hence no history to retrieve

            Worst Case Complexity: O(H)
                This occurs when all games are served and appended back again to build the resulting list.
        """
        queue_length = len(self.history)
        if queue_length == 0:
            return None

        result_game_order = LinkedList()

        for current_game in range(queue_length):
            old_game = self.history.serve()
            result_game_order.append(old_game)
            self.history.append(old_game)
        return result_game_order



    def make_post(self, post_date: str, post_content: str) -> None:
        """
        Publish a team blog `post` for a particular `post_date`.
       
        A `Team` can have one published post per day. Any duplicate
        posts should overwrite the original post for that day.
        
        Args:
            `post_date` (`str`) - The date of the post
            `post_content` (`str`) - The content of the post
        
        Returns:
            None

        Complexity:
            Best Case Complexity:O(K)
                stores each post content at the specific post date, with double hashing

            Worst Case Complexity: O(M^2 * K )
                Occurs when the HashyDateTable is triggered (and its worst case)
                This occurs at the cost of reinserting to the existing positions O(M*M*K)
        """
        self.post[post_date] = post_content


    def __len__(self) -> int:
        """
        Returns the number of players in the team.

        Complexity:
            Best Case Complexity: O(1) Occurs when there is 1 player or no players in self.players
            Worst Case Complexity: O(P) Occurs when there are multiple player in self.players

        P : number of players in self.players
        """
        total = 0
        for current_slot in self.players.values():
            total += len(current_slot)
        return total

    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the team object.

        Complexity analysis not required.
        """
        return f"T.Name {self.name}, Players: {self.players}"

    def __repr__(self) -> str:
        """Returns a string representation of the Team object.
        Useful for debugging or when the Team is held in another data structure.
        """
        return str(self)

    #__gt__() greater than operator is not required since the arraySorted list only compares using < and <=

    """
    Best case - O(1)
    Worst case - O(1)
    """
    def __lt__(self, other: Team) -> bool:
        return self.points < other.points

    """
    Best case - O(1)
    Worst case - O(1)
    """
    def __eq__(self, other: Team) -> bool:
        if self.points == other.points:
            return self.name < other.name

