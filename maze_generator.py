import random
from config import MAZE_ROWS, MAZE_COLS


def generate_maze():
    maze = [[1 for _ in range(MAZE_COLS)] for _ in range(MAZE_ROWS)]

    def carve_passages(cx, cy):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 0 <= nx < MAZE_ROWS and 0 <= ny < MAZE_COLS and maze[nx][ny] == 1:
                maze[cx + dx][cy + dy] = 0
                maze[nx][ny] = 0
                carve_passages(nx, ny)

    start_x, start_y = 1, 1
    maze[start_x][start_y] = 0
    carve_passages(start_x, start_y)

    # Exit (there will be red pixel)
    exit_x, exit_y = MAZE_ROWS - 2, MAZE_COLS - 2
    maze[exit_x][exit_y] = 0

    return maze, (exit_x, exit_y)


if __name__ == "__main__":
    from pprint import pprint

    m, exit_pos = generate_maze()
    print(m)
    print("Exit", exit_pos)
