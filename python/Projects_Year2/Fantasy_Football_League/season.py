from __future__ import annotations

from data_structures import ArraySortedList, LinkedList
from data_structures.array_set import ArraySet
from data_structures.referential_array import ArrayR
from data_structures.array_list import ArrayList
from enums import TeamGameResult, PlayerPosition
from game_simulator import GameSimulator, GameSimulationOutcome
from dataclasses import dataclass

from player import Player
from team import Team


#Each game is an instance of the class
@dataclass
class Game:
    """
    Simple container for a game between two teams.
    Both teams must be team objects, there cannot be a game without two teams.

    Note: Python will automatically generate the init for you.
    Use Game(home_team: Team, away_team: Team) to use this class.
    See: https://docs.python.org/3/library/dataclasses.html

    Do not make any changes to this class.
    """
    home_team: Team = None
    away_team: Team = None

# game week is a collection of games that will be played that week
class WeekOfGames:
    """
    Simple container for a week of games.

    A fixture must have at least one game.
    """

    def __init__(self, week: int, games: ArrayR[Game] | ArrayList[Game]) -> None:
        """
        Container for a week of games.

        Args:
            week (int): The week number.
            games (ArrayR[Game]): The games for this week.
        
        No complexity analysis is required for this function.
        Do not make any changes to this function.
        """
        self.games = games
        self.week: int = week

    def __iter__(self):
        """
        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

            Requires only 1 assignment of self.current_pointer
        """
        self.current_pointer = 0
        return self

    def __next__(self):
        """
        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

            Required by the iteration dunder method to go to the next iteration.
            Increments self.current_pointer by 1.
        """
        if self.current_pointer >= len(self.games):
            raise StopIteration
        else:
            current_game = self.games[self.current_pointer]
            self.current_pointer += 1
            return current_game

# season consists of several game weeks - each season will have a leaderboard and a schedule.
class Season:

    def __init__(self, teams: ArrayR[Team] | ArrayList[Team]) -> None:
        """
        Initializes the season with a schedule.

        Args:
            teams (ArrayR[Team]): The teams played in this season.

        Complexity:
            Best Case Complexity: O(N^2)
            Worst Case Complexity: O(N^2)

            main complexity increase due to the assignment of self.schedule by calling generate_schedule which is O(N^2)
        """

        self.teams = teams
        self.leaderboard = ArraySortedList()
        self.schedule  = self._generate_schedule()

    def _generate_schedule(self) -> ArrayList[ArrayList[Game]]:
        """
        Generates a schedule by generating all possible games between the teams.

        Return:
            ArrayList[ArrayList[Game]]: The schedule of the season.
                The outer array is the weeks in the season.
                The inner array is the games for that given week.

        Complexity:
            Best Case Complexity: O(N^2) where N is the number of teams in the season.
            Worst Case Complexity: O(N^2) where N is the number of teams in the season.
        
        Do not make any changes to this function.
        """
        num_teams: int = len(self.teams)
        weekly_games: ArrayList[ArrayList[Game]] = ArrayList()
        flipped_weeks: ArrayList[ArrayList[Game]] = ArrayList()
        games: ArrayList[Game] = ArrayList()

        # Generate all possible matchups (team1 vs team2, team2 vs team1, etc.)
        for i in range(num_teams):
            for j in range(i + 1, num_teams):
                games.append(Game(self.teams[i], self.teams[j]))

        # Allocate games into each week ensuring no team plays more than once in a week
        week: int = 0
        while games:
            current_week: ArrayList[Game] = ArrayList()
            flipped_week: ArrayList[Game] = ArrayList()
            used_teams: ArraySet = ArraySet(len(self.teams))

            week_game_no: int = 0
            for game in games:
                if game.home_team.name not in used_teams and game.away_team.name not in used_teams:
                    current_week.append(game)
                    used_teams.add(game.home_team.name)
                    used_teams.add(game.away_team.name)

                    flipped_week.append(Game(game.away_team, game.home_team))
                    games.remove(game)
                    week_game_no += 1

            weekly_games.append(current_week)
            flipped_weeks.append(flipped_week)
            week += 1

        for flipped_week in flipped_weeks:
            weekly_games.append(flipped_week)

        return weekly_games

    def simulate_season(self) -> None:
        """
        Simulates the season.

        Complexity:
            Assume GameSimulator.simulate() is O(1)
            Remember to define your variables in your complexity.

            Best Case Complexity: O(G ( G * P) + O(T.logT))
                Occurs when we iterate over all the games in the season. O(G)
                Creation of teams using Teams class  O(G*P)
                Supose there are no goal counts
                Updating the leaderboard O(T.logT) this is derived from the wayarray sorted List sorts the elements


            Worst Case Complexity: =  O(G * G * P) + O(T.log T)
                Occurs when all the previous actions take place in the best case scenario except in the worst case we need to update the goal count
                For each player compare between teams


        T: number of teams (have been changed from N to T)
        G: total number of games both home & away
        W: number of weeks
        P: number of players per team
        """

        for current_week in self.schedule:
            for current_game in current_week:
                home_team = Team(current_game.home_team.name, current_game.home_team.get_players(), current_game.home_team.history_length)
                away_team = Team(current_game.away_team.name, current_game.away_team.get_players(),current_game.home_team.history_length)

                # print("Home team:",current_game.home_team.name, "| Away:team:", current_game.away_team.name)
                result = GameSimulator.simulate(home_team, away_team)
                # print(f"Away goals: {result.away_goals},Home goals: {result.home_goals},Goal scorers: {result.goal_scorers}")

                for current_scorer in result.goal_scorers:
                    for player in home_team.get_players():
                        if player.name == current_scorer:
                            player.goals +=1
                    for player in away_team.get_players():
                        if player.name == current_scorer:
                            player.goals +=1


                if result.home_goals > result.away_goals:
                    home_team.add_result(TeamGameResult.WIN)
                    away_team.add_result(TeamGameResult.LOSS)
                elif result.home_goals < result.away_goals:
                    home_team.add_result(TeamGameResult.LOSS)
                    away_team.add_result(TeamGameResult.WIN)
                elif result.home_goals == result.away_goals:
                    home_team.add_result(TeamGameResult.DRAW)
                    away_team.add_result(TeamGameResult.DRAW)

                self.leaderboard.clear()
                current_team_index = 0
                while current_team_index <= (len(self.teams)-1):
                    self.leaderboard.add(self.teams[current_team_index])
                    current_team_index += 1
                # print(self.leaderboard)


    def delay_week_of_games(self, orig_week: int, new_week: int | None = None) -> None:
        """
        Delay a week of games from one week to another.

        Args:
            orig_week (int): The original week to move the games from.
            new_week (int or None): The new week to move the games to. If this is None, it moves the games to the end of the season.

        Complexity:
            Best Case Complexity: O(1)
                Occurs when , given that next week is provided
                Such that original week and the next week are in the same index , as a result only one shift occurs
                Since both remove() and insert result in a complexity of O(1)

            Worst Case Complexity: O(T + W)
                Occurs when next week is not provided O(T)
                Remove occurs at the start of the list, hence this requires shifting
                inserting occurs at the end of the list, no shifting required

        """
        #Algo to get the last week when the next week is none when delaying to the end of season
        self.new_week = new_week
        if self.new_week is None:
            team_count = len(self.teams)
            games_count = team_count * (team_count - 1)

            games_per_week = team_count // 2
            game_weeks = games_count / games_per_week

            self.new_week = game_weeks - 1

        #imeplement algo for setting the week to another week by delaying
        # self.schedule[orig_week], self.schedule[new_week] = self.schedule[new_week], self.schedule[orig_week]
        temp_week = self.schedule[orig_week-1]
        self.schedule.remove(self.schedule[orig_week-1])
        self.schedule.insert(self.new_week-1, temp_week)




    def __len__(self) -> int:
        """
        Returns the number of teams in the season.

        Complexity:
            Best Case Complexity: O(1)
                Occurs when there is only one team in the season.
            Worst Case Complexity: O(N)
                Occurs when there is more than one team in the season.
        """
        team_count = 0
        for _ in self.teams:
            team_count += 1
        return team_count

    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the season object.

        Complexity:
            Analysis not required.
        """
        return f"Schedule: {self.schedule}"

    def __repr__(self) -> str:
        """Returns a string representation of the Season object.
        Useful for debugging or when the Season is held in another data structure."""
        return str(self)
