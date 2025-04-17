import config


class Player:
    def __init__(self, canvas, maze):
        self.canvas = canvas
        self.maze = maze
        self.x, self.y = 1, 1
        self.rect = self.canvas.create_rectangle(
            self.x * config.CELL_SIZE,
            self.y * config.CELL_SIZE,
            (self.x + 1) * config.CELL_SIZE,
            (self.y + 1) * config.CELL_SIZE,
            fill=config.PLAYER_COLOR,
        )
        self.draw_maze()

    def draw_maze(self):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 1:
                    self.canvas.create_rectangle(
                        x * config.CELL_SIZE,
                        y * config.CELL_SIZE,
                        (x + 1) * config.CELL_SIZE,
                        (y + 1) * config.CELL_SIZE,
                        fill=config.WALL_COLOR,
                    )

    def move(self, event):
        dx, dy = 0, 0

        if event.keysym == "Up":
            dy = -1
        elif event.keysym == "Down":
            dy = 1
        elif event.keysym == "Left":
            dx = -1
        elif event.keysym == "Right":
            dx = 1

        new_x, new_y = self.x + dx, self.y + dy
        if self.maze[new_y][new_x] == 0:
            self.x, self.y = new_x, new_y
            self.canvas.coords(
                self.rect,
                self.x * config.CELL_SIZE,
                self.y * config.CELL_SIZE,
                (self.x + 1) * config.CELL_SIZE,
                (self.y + 1) * config.CELL_SIZE,
            )
