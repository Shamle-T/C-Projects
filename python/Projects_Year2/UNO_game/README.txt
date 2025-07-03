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
  
  How It Works
    Players take turns playing a card that matches the color or value of the top card on the discard pile
    Special black cards can reverse play order or skip players
    The first player to run out of cards wins the game
