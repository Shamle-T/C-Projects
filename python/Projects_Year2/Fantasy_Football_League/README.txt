🔍 Overview
  The Fantasy Football League (FFL) project involved designing a full-fledged football season simulator using advanced data structures and algorithmic techniques. We built a modular system that tracks players, teams, match statistics, and league standings across multiple weeks, while strictly avoiding Python built-in types (list, dict, set) and libraries (except enum, dataclasses, and datetime).
    This assignment enforced conceptual depth by requiring students to apply custom implementations of:
    Hash Tables with custom probing methods
    Lazy deletion and Double Hashing
    Array-based dynamic/resizable lists
    Recursion, Iterators, and Simulations
    Enumerations and constrained input formats

🎯 Learning Objectives
  Apply data abstraction and encapsulation in a sports simulation context.
  Implement efficient hash table strategies (linear probing, double hashing).
  Manage dynamic collections using custom-built list and array structures.
  Simulate real-world scheduling scenarios (match delays, weekly games).
  Analyze and maintain time complexity efficiency across operations.
  Use iterators and magic methods to simulate iterable objects and operator overloading.

⚽ How the Fantasy Football League (FFL) Game Works
The Fantasy Football League (FFL) simulates a realistic football season involving multiple teams and players. Each season is composed of weekly fixtures (game weeks), during which teams face off in simulated matches. The system automatically generates schedules, simulates matches, tracks team performance, and maintains a dynamic leaderboard.

🧠 Game Simulation Flow
Season Setup:
  The season begins with a set of registered teams, each containing multiple players grouped by position (e.g., goalkeeper, striker).
  A match schedule is generated using a round-robin-like approach where each team plays others in home and away matches across multiple game weeks.

Weekly Games:
  Every WeekOfGames contains a fixed number of Game objects.
  Each Game has a home_team and an away_team.

Simulating a Match:
  Matches are simulated using the provided GameSimulator.simulate(home_team, away_team) method.
  This simulation returns a GameSimulationOutcome object, which includes:
    home_goals and away_goals
    A list of goal_scorers (player names)

After the Match:
  Player Stats:
    For every goal scored, the respective player’s goals attribute is incremented.

  Team Points:
    Teams earn points based on the result:
      Win: 3 points
      Draw: 1 point
      Loss: 0 points
      These are tracked using the TeamGameResult enum.

  Match History:
    Each team's recent match results are stored in a history log with a fixed length, using a queue-like structure.

Leaderboard Update:
  After every game, the leaderboard is updated.
  Teams are sorted first by total points (descending) and then by name (ascending) in the case of a tie.

Game Delays (Optional):
  Weeks of games can be rescheduled using the delay_week_of_games() method to simulate real-world disruptions (e.g., weather, events).
  The delayed week can either push other weeks forward or be moved to the season's end.

Components
  Player: Tracks goals and customizable stats.
  Team: Maintains roster, points, result history, and updates.
  Game: Holds match fixtures.
  WeekOfGames: Bundles matches per week with iterable behavior.
  Season: Controls the full season, scheduling, simulating matches, and managing the leaderboard.


🧩 Task-by-Task Summary
  🔹 Task 1 – Hashy Date Table
  Goal: Build a specialized hash table for date strings in multiple formats (YYYY-MM-DD, DD/MM/YYYY, etc.)
  Work Done:
  Implemented a hash function optimized to distribute days of the year uniformly across the table.
  Ensured minimal collisions by tailoring the hash to a 366-slot-per-year layout.
  
  Complexity: Hash function runs in O(1) due to fixed-length string parsing.
  
  🔹 Task 2 – Lazy Double Table
  Goal: Implement a hash table that uses double hashing and lazy deletion.
  Work Done:
  Developed hash2() to produce step sizes co-prime with table size.
  Rewrote probing logic using hash2 and incorporated sentinel-based deletion.
  Implemented full support for insertion, deletion, and rehashing with lazy deletion in mind.
  
  Complexity:
  Insertion and deletion in amortized O(1) (low load factor of 2/3).
  rehash() loops through and reinserts valid keys only.
  
  🔹 Task 3 – The Player Class
  Goal: Create a player system that tracks statistics and supports indexing via keys.
  Work Done:
  Stored name, position (using PlayerPosition enum), and birth year instead of age.
  Allowed stats tracking via __getitem__ and __setitem__ (e.g. player["ASSISTS"] = 5).
  Implemented stat resets and dynamic age calculation from current year.
  
  Complexity:
  Stat reset and stat access are O(n) and O(1) depending on internal structure (assumed constant due to constraints).
  
  🔹 Task 4 – The Team Class
  Goal: Design a class to manage team-level data: players, game history, posts.
  Work Done:
  Grouped players by position using enum-based partitioning.
  Preserved insertion order within position groups.
  Maintained match history with a fixed-length structure.
  Implemented blog-style updates using date-based posts.
  
  Complexity:
  Player insertion/removal: O(1) to O(n) depending on group structure.
  History management with circular buffer-like logic: O(1).
  
  🔹 Task 5 – Setup Season
  Goal: Implement a class to organize teams and generate match schedules.
  Work Done:
  Stored teams, leaderboard, and the match schedule using appropriate containers.
  Created custom iterators for weekly games (WeekOfGames class).
  Implemented delay_week_of_games to reschedule match weeks flexibly.
  
  Complexity:
  Delay handling with reordering: O(n) for cascading shifts.
  Iterators and len: O(1).
  
  🔹 Task 6 – Simulate Season
  Goal: Use the game simulator to simulate all matches and update all relevant data.
  Work Done:
  Iterated through each WeekOfGames and used GameSimulator.simulate() for match results.
  Updated:
  Team points and history
  Player goal counts
  Leaderboard rankings
  
  Complexity:
  Each week: O(m log m) (if leaderboard is re-sorted after each game), where m = number of teams.
  Goal updates and match result handling: O(GS) where GS is cost of game simulation (assumed constant or linear in goal count).
