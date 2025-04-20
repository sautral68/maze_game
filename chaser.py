import heapq
import random
import config


class Chaser:
    def __init__(self, canvas, maze, start_x, start_y, move_delay=50):
        self.canvas = canvas
        self.maze = maze
        self.x = start_x
        self.y = start_y
        self.move_delay = move_delay  # delay between steps
        # used in the game loop to control the frequency of movement
        self.last_move_time = 0
        self.cell_size = config.CELL_SIZE
        self.rect = self.canvas.create_rectangle(
            self.x * self.cell_size,
            self.y * self.cell_size,
            (self.x + 1) * self.cell_size,
            (self.y + 1) * self.cell_size,
            fill=config.CHASER_COLOR,
        )

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def is_walkable(self, x, y):
        rows = len(self.maze)
        cols = len(self.maze[0])
        return 0 <= x < cols and 0 <= y < rows and self.maze[y][x] == 0

    def get_neighbors(self, node):
        x, y = node
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.is_walkable(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def a_star(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(
                        neighbor, goal
                    )
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []

    def move_towards(self, player_x, player_y):
        # 70% chance that the chaser will think and take a step, and 30% that he will "slow down" and miss (you can chage the value if you want)
        if random.random() < 0.7:
            path = self.a_star((self.x, self.y), (player_x, player_y))
            if path:
                next_x, next_y = path[0]
                dx = (next_x - self.x) * self.cell_size
                dy = (next_y - self.y) * self.cell_size
                self.canvas.move(self.rect, dx, dy)
                self.x = next_x
                self.y = next_y
