Card Clash: Color Chaos
  Overview
    Card Clash: Color Chaos is a Python-based multiplayer card game where players compete to be the first to discard all their cards. Each card has a color and a value, with special black cards introducing unique gameplay effects.
  
  This project was built to explore core algorithm design, manual data structure usage, and object-oriented programming in a game-based context. The game runs entirely on custom logic and avoids all built-in Python data structures and sorting functions.
  
  Key Concepts Demonstrated
    Manual game logic implementation without built-in list, dict, tuple, or set
    Use of provided custom data structures (like LinkedList, Stack, etc.)
    Turn-based game loop and card matching algorithms
    Modular object-oriented structure and separation of concerns
        
  Provided Components
    Some components were given as part of the project scaffold:
    Custom Data Structures – Classes like Stack, Queue, and others used throughout the game
    Test Cases – A suite of predefined tests to validate gameplay and logic correctness
    Config File – Contains constants such as card types, player limits, and rules
    
  These were used as-is, and the main focus was on building the game logic within strict constraints.
  
  Constraints
    This project was intentionally developed with the following limitations:
    No use of Python built-in collections (list, dict, tuple, set, etc.
    No built-in or library sorting functions
    No external libraries or frameworks
    All gameplay logic and sorting built manually
    Constants sourced from a single config module

  Game rules
    The game is played with a 112-card deck:
    4 colors (Red, Blue, Green, Yellow), each with:
    20 number cards (0–9, two of each)
    2 Skip cards
    2 Reverse cards
    2 Draw Two cards
    8 special Black cards:
    4 Black Draw Four cards
    4 Black Crazy cards (wild cards)
    
    Players take turns playing cards that match the color or label of the top card on the discard pile.
    Special card effects include:
    Skip: Skips the next player.
    Reverse: Reverses player turn order.
    Draw Two: Next player draws two cards and misses a turn.
    Black Crazy: Wild card that changes the current color randomly.
    Black Draw Four: Same as Black Crazy, but the next player draws four cards and skips a turn.

  Project Tasks
    Task 1 – Card and Player Classes
      Created a Card class with color and label enums.
      Built a Player class with a custom card hand, and implemented:
      add_card, play_card, is_empty, cards_in_hand
      Play priority rules based on color, then label enum order.

  Task 2 – GameBoard Class
    Built a GameBoard to manage draw_pile and discard_pile
    Implemented discard_card, draw_card, and reshuffle methods
    Ensured reshuffle uses a deterministic shuffle with RandomGen

  Task 3 – Game Class
    Implemented the full game state with players, current card, and turn management
    Created methods to handle:
    Player order (reverse_players, next_player)
    Special effects (skip_next_player, play_draw_two, play_black)
    Drawing logic with intelligent playability handling

  Task 4 – Game Flow (play_game)
    Implemented a full game loop until a player wins
    Handled reshuffling, Black card color switching, special card logic, and all edge cases
    Matched exact behavior with provided test case logs (test4_1.md, test4_2.md) using random seeds


  How It Works
    Players take turns playing a card that matches the color or value of the top card on the discard pile
    Special black cards can reverse play order or skip players
    The first player to run out of cards wins the game



