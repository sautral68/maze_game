import config


class ExitZone:
    def __init__(self, canvas, maze):
        self.canvas = canvas
        self.maze = maze
        self.x = len(maze[0]) - 2
        self.y = len(maze) - 2

        self.draw_exit()

    def draw_exit(self):
        x1 = self.x * config.CELL_SIZE
        y1 = self.y * config.CELL_SIZE
        x2 = (self.x + 1) * config.CELL_SIZE
        y2 = (self.y + 1) * config.CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=config.EXIT_COLOR)

    def is_player_at_exit(self, player_x, player_y):
        return player_x == self.x and player_y == self.y
