# Maze Challenge

**Maze Challenge** is an exciting maze game written in *Python* using the *Tkinter* library. The player must find the exit from the maze while avoidinga Chaser and finishing within the time limit


## Game Features 

- **Dynamic Maze Generation:** Mazes are generated dynamically using the Recursive Backtracking algorithm.
- **Player Controls:** Navigate the player using arrow keys.
- **Chaser AI:** The chaser moves toward the player using the A* pathfinding algorithm.
- **Timer:** Players have a limited time to find the exit.
- **Win/Loss Conditions:**
  - Win: The player reaches the exit.
  - Lose: The chaser catches the player or time runs out.



## Project Structure

<pre>
GAME/
├── config.py          # Constants for colors, sizes, and time
├── maze_generator.py  # Maze generation logic
├── player.py          # Player class
├── chaser.py          # Chaser class
├── timer.py           # Game timer
├── exit_zone.py       # Exit zone logic
├── game.py            # Main game logic
└── main.py            # Entry point for the game
</pre> 



## Installation and Running

**Requirements**
- Python 3.7 or higher
- Tkinter library (included in Python's standart library)

**Installation**

1. Clone the repository:
   ```bash
    git clone https://github.com/sautral68/waze_game.git
    cd waze_game
   ```

2. Ensure you have Python installed. Check the version:
   ```bash
    python --version
   ```

3. Run the game:
   ```bash
    python main.py
   ```


## How to Play

1. Use the arrow keys to control the player.
2. Find the exit (red cell) before the timer runs out.
3. Avoid the chaser, which moves toward you using the A* algorithm.
4. If you reach the exit, you win. If the chaser catches you or time expires, you lose.


## Customizing Parameters

You can customize the game by modifying contants in `config.py`:

```python
# Maze cells size
CELL_SIZE = 25
MAZE_ROWS = 21  # Must be odd
MAZE_COLS = 21  # Must be odd

# Time limit
TIME_LIMIT = 40

# Colors
PLAYER_COLOR = "blue"
EXIT_COLOR = "red"
CHASER_COLOR = "purple"
WALL_COLOR = "black"
BACKGROUND_COLOR = "white"

# Chasers count
CHASER_COUNT = 3
```

By chanching these values, you can adjust the maze size, element colors, and time limit.
