There exists 2 projects in this repo, which were made for the assignemnts:
  1. Bootcamps - FarmGame - https://git.infotech.monash.edu/fit2099/fit2099-s1-2025/bootcamps/wthi0003.git
  2. 2 Main projects - Elden Thing 
    Basis of the game, part 1 (Assignment 1) - https://git.infotech.monash.edu/fit2099/fit2099-s1-2025/assignments/wthi0003.git
    Advancements of the game, part 2 (Assignemnt 2 and 3 combined) - https://git.infotech.monash.edu/fit2099/fit2099-s1-2025/assignment-group/MA_Applied08_GroupA/project.git

Both of them can be cloned to intellij via respective links using HTTPS

The first project consists of a weekly development of a farm game, a step by step introduction to implementing system design using OOP principles
The second project has 2 parts, where the first part is done individually, whereas the second part is done groupwise. Below is a detailed description about the 2 parts of the main project

Part 1 
⚔️ ELDEN THING: The Valley of the Inheritree
🧱 Object-Oriented Game Design & Development (Java)
This project is a text-based, rogue-like adventure game inspired by Elden Ring. It was built using object-oriented principles to model a dynamic world featuring player actions, non-playable characters (NPCs), game state changes, and environmental effects.

The game is designed to evolve over multiple iterations. This initial phase focuses on building core mechanics like combat, terrain interaction, healing, and rot effects while maintaining a clean, extensible architecture following SOLID design principles.

🧩 Key Concepts Applied
Object-Oriented Principles: Abstraction, inheritance, encapsulation, polymorphism
Design Thinking: Iterative development, scenario mapping, and modular extensibility
UML Design: Class diagrams for proposed extensions (tools: PlantUML / diagrams.net)
Team Tools: Git for version control, IDE-driven development (IntelliJ / Eclipse)

🎮 Gameplay Features (Implemented in Assignment 1)
🧙‍♂️ REQ1 – The Graceless Farmer
Introduced the Farmer as the main character with health and stamina tracking.
Designed and implemented friendly NPCs: Spirit Goat and Omen Sheep, with differing HP and behaviors.
Built combat mechanics using probabilistic hit logic (50% chance, 25 dmg).
Displayed player stats and game state dynamically at each tick.

🌱 REQ2 – The Valley of the Inheritree
Developed a planting system where seeds bloom instantly into Inheritree (t) or Bloodrose (w).
Created tile-based terrain effects: only soil (.) supports planting; blight (x) is unplantable.
Inheritree purifies nearby tiles and heals adjacent actors every turn.
Bloodrose saps player health once and damages nearby actors each turn.
Implemented inventory logic, seed usage via action handling (not just dropping).

🧪 REQ3 – Crimson Rot
All actor actions now consume stamina (configurable per action).
Rot effects trigger auto-despawn of goats (10 turns) and sheep (15 turns).
Introduced the Talisman (o):
Cures rot from blight tiles at stamina cost.
Resets countdown for spirit goats.
Causes sheep to sprout Inheritrees in surrounding tiles.
Built rot-timer tracking and tile transformation mechanics.

⚙️ Design Strategy
Employed clean class hierarchies for Actor, Item, Ground, and Action abstractions.
Encapsulated rot logic and planting mechanics using polymorphism for future extensibility.
Separated responsibilities across factories, action classes, and effect classes to ensure maintainability.
Designed code to support future behaviors (e.g., hostile NPCs, growing crops over time, AI pathfinding).

💡 Highlights
Built on a scaffolded Java game engine
Used UML class diagrams for planning and refactoring
Carefully adhered to SOLID principles to allow modular growth
Emphasized code readability, testability, and gameplay clarity

Part 2
🧠 Overview:
This project involved collaboratively extending a rogue-like Java game across Assignments 2 and 3, focusing on object-oriented design (OOD), design rationale, UML documentation, and implementation using Java. The system was continuously evolved using iterative design principles, while applying abstraction, inheritance, polymorphism, and encapsulation. Git and UML tools were used for version control and architecture modeling.

Assignments 2 and 3 were completed together as a group, with members responsible for different requirements.

✅ I was personally responsible for:
Assignment 2 – REQ4: The Wayward Seller of Wares
Assignment 3 – REQ1: Limveld & Creature Behavior Strategy

👨‍💻 My Contributions
✅ Assignment 2 – REQ4: The Wayward Seller of Wares
I implemented a merchant system where the player (Farmer) can purchase items like the Broadsword, Katana, and Dragonslayer Greatsword. Each weapon applied different effects depending on the seller (Sellen or Kale) such as altering max health, stamina, or spawning creatures. The design required:
Handling purchase actions within the existing action menu (not in a separate UI).
Weapon behavior to vary based on seller context.
Adherence to extensibility principles, allowing easy addition of new weapons or merchants.
Key OOP concepts applied:
Encapsulation of purchase effects
Use of interfaces for merchant behavior
Strategy-like design for weapon effects

✅ Assignment 3 – REQ1: Limveld Expansion & Behavior Strategy
I designed the teleportation system that enabled the player to move between Limveld and the Valley using portals. I also implemented a flexible behavior strategy for creatures:
Some creatures follow a priority-based behavior order.
Others select a random behavior each turn, executing it only if valid.

Key design focus:
Multi-map support with teleportation points (A)
Strategy pattern to allow configurable creature behavior logic
Modular design to add new behavior selection mechanisms in future

📌 Summary of All Requirements
📦 Assignment 2 – Requirements Overview:
REQ1: Life in the Valley
Introduced reproduction for Spirit Goats (near blessed items like Inheritree).

Omen Sheep lay eggs every 7 turns; hatch after 3 turns on ground.
Eggs can be consumed by the player for health boosts.
Encouraged code reusability for hatching and surrounding-entity checks.

REQ2: Be Wary of Dung (Beetle)
Added Golden Beetle with a lifecycle: lays golden eggs, immune to rot.
Eggs hatch near blight; can be consumed for stamina.
Beetles follow the player and interact based on turn priority.

REQ3: The People of the Valley
Implemented NPCs with monologues (Sellen, Kale, Guts).
Dialogue varies by player conditions (health, runes, inventory, etc.).
Dynamic monologue pools, triggered by in-game scenarios.

✅ REQ4 (My Task): Wayward Seller of Wares
Created merchants with varied pricing, weapons, and side effects.
Ensured merchant-specific logic and extensibility.

📦 Assignment 3 – Requirements Overview:
✅ REQ1 (My Task): Limveld & Creature Behavior Strategy
Created a second map (Limveld) with teleportation mechanics.
Creatures introduced with random vs. priority behavior selection.
Enhanced extensibility of AI behavior control per creature instance.

REQ2: Bed of Chaos (Boss Fight)
Introduced a boss ("T") that grows by adding branches/leaves.
Each growth phase increases its attack power.
Damage calculated recursively via tree structure.

REQ3 & REQ4: Creative Mode Requirements
Teams designed their own new gameplay mechanics.
Required 5+ new classes and use of game engine interfaces.
Justified with SOLID principles and tested with creative scenarios.

🛠 Technologies & Tools Used:
Java (OOP design)

IntelliJ IDEA (IDE)
Git & GitLab (Version Control)
UML tools: Draw.io
Game Engine Scaffold (restricted engine modification)

