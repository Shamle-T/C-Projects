📚 Introduction
The final project, NotMinecraft: Mining Horrors, simulates a strategic mining expedition set beneath Australia. Players take the role of "Steve," a miner who navigates complex cave systems, identifies valuable blocks, and makes calculated decisions on what to mine. To do this effectively, the assignment requires implementing and combining multiple concepts from the semester: abstract data types (ADTs), sorting algorithms, recursion, and tree structures.
The assignment emphasizes efficient computation and data representation. Students are challenged to develop a balanced Binary Search Tree, manage block checklists with optimal searching and insertion, and simulate a mining scenario using Depth-First Search and ratio-based filtering strategies.

⚠️ Restrictions Summary
To ensure the academic rigor and reinforce learning goals, the following constraints apply:
❌ No built-in Python types like list, dict, or set (only tuple is allowed).
✅ Use only scaffold-provided ADTs like ArrayList, ArrayR, LinkedList, and tree structures.
❌ No external libraries.
⚠️ Sorting must use only the provided algorithms.
🧠 Complexity requirements are enforced for approach marks.
👨‍🏫 AI-generated code is strictly prohibited.

🎮 How the Game Works
In NotMinecraft, Steve explores a procedurally connected cave system, where each node (chamber) may contain mineable blocks like gold, opal, or iron. These blocks have properties:
  Hardness (affects time to mine)
  Value (the worth of its contained item)

Steve receives a checklist of high-value blocks and uses it to guide his mining path. Movement through the cave is free (thanks to a speed potion), but mining consumes time relative to the block's hardness. Using a Depth-First Search (DFS) approach, Steve explores the cave, evaluates the blocks, filters the best candidates, and mines them in the optimal order—based on the value-to-hardness ratio.

Two scenarios are simulated:
  Objective Mining — Steve filters and sorts blocks before mining.
  Post-Chicken Jockey Attack — Blocks are shuffled, but still mined by optimal ratio.

The game relies on efficient data structures and algorithmic strategies to mimic real-time decision making.

✅ Task Summaries
🧩 Task 1: Inner Balance – Implementing a BetterBST
  This task focuses on building a balanced binary search tree (BST) from a given set of key-item pairs. A balanced tree helps maintain optimal performance (O(log n)) for search and insert operations.
  
  Key Methods:
  __sort_elements(...)Sorts key-item pairs by key using provided sorting algorithms.🕒 Complexity: O(n log n)
  __build_balanced_tree(...)Recursively builds a balanced BST from the sorted elements.🕒 Complexity: O(n log n)
  filter_keys(...)Returns key-item pairs that satisfy both lower and upper bound filters.🕒 Complexity: Best O(log n), Worst O(n)

📟 Task 2: The Mining Checklist – Storing & Evaluating Blocks
  This task focuses on maintaining a collection of valuable blocks and selecting which blocks are worth mining.
  Implementations:
  
  Miner class
  mine(block) — Adds an item to inventory in order mined.
  clear_inventory() — Returns all items in order and resets inventory.
  
  MinecraftChecklist class
  __contains__(block) — Checks if block is in checklist.
  add_block(block) / remove_block(block) — Inserts/removes a block efficiently.
  get_sorted_blocks() — Returns blocks sorted by value-to-hardness ratio.
  get_optimal_blocks(block1, block2) — Returns blocks strictly between two ratio thresholds.
  
  📈 Uses BetterBST from Task 1 for efficient filtering and searching.🕒 Emphasis on logarithmic performance in insertion/removal and range queries.

⛏️ Task 3: What We’ve Been Trained To Do – Exploring and Mining
  This task simulates the cave exploration and strategic mining logic, combining previous tasks with DFS traversal.
  
  Key Elements:
    CaveSystem and CaveNodeModels cave as a graph of chambers containing blocks. Steve traverses this with DFS.
    dfs_explore_cave()Implements DFS to find all blocks in the cave system.
  
  Mining Scenarios:
  objective_mining_filter(blocks, low, high)Filters blocks:
    Must be on the checklist
    Must fall strictly between two reference ratios
  
  objective_mining()
    Sorts filtered blocks by decreasing value-to-hardness ratio and mines them in that order.🕒 Complexity: O(n log n)

These methods simulate Steve's careful planning and execution of the mining strategy.
