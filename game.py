import tkinter as tk
from tkinter import messagebox
from maze_generator import generate_maze
from player import Player
from chaser import Chaser
from timer import Timer
from exit_zone import ExitZone
import config
import random


class MazeGame:
    def __init__(self, root):
        # creating maze and root
        self.root = root
        self.maze, self.exit_pos = generate_maze()
        self.rows, self.cols = config.MAZE_ROWS, config.MAZE_COLS
        self.canvas = tk.Canvas(
            root,
            width=self.cols * config.CELL_SIZE,
            height=self.rows * config.CELL_SIZE,
            bg=config.BACKGROUND_COLOR,
        )
        self.canvas.pack()

        # spawn player and chaser
        self.player = Player(self.canvas, self.maze)
        chaser_y, chaser_x = self.get_random_passable_cell(min_distance=7)
        self.chaser = Chaser(
            self.canvas,
            self.maze,
            start_x=chaser_x,
            start_y=chaser_y,
        )

        # chaser move delay
        self.chaser_move_delay = 90
        self.chaser_last_move_time = 0

        # spawn exit zone
        self.exit_zone = ExitZone(self.canvas, self.maze)

        # starting timer
        self.timer = Timer(root)
        self.timer.start()

        # binding arrow keys to move
        self.root.bind("<Key>", self.handle_key_press)

        self.game_loop()

    # function to spawn the chaser in random cell
    def get_random_passable_cell(self, min_distance=0):
        while True:
            x = random.randint(1, self.rows - 2)
            y = random.randint(1, self.cols - 2)
            if self.maze[x][y] == 0:
                if min_distance > 0:
                    dist = abs(self.player.x - y) + abs(self.player.y - x)
                    if dist < min_distance:
                        continue
                return (x, y)

    # moving function
    def handle_key_press(self, event):
        self.player.move(event)

    # checking if player win
    def check_win(self):
        if self.exit_zone.is_player_at_exit(self.player.x, self.player.y):
            self.timer.stop()
            messagebox.showinfo(
                "Win!", f"You passed the labyrinth in {self.timer.get_time()} seconds!"
            )
            self.root.quit()

    # checking if player loose
    def check_loss(self):
        if (self.player.x, self.player.y) == (self.chaser.x, self.chaser.y):
            self.timer.stop()
            messagebox.showinfo("You Loose!", "Chaser reached you!")
            self.root.quit()

    # checking if time out
    def game_loop(self):
        current_time = self.timer.get_time() * 1000

        self.check_win()
        self.check_loss()

        if self.timer.get_time() >= config.TIME_LIMIT:
            self.timer.stop()
            messagebox.showinfo("You Loose!", "Time is out!")
            self.root.quit()

        if current_time - self.chaser_last_move_time >= self.chaser_move_delay:
            self.chaser.move_towards(self.player.x, self.player.y)
            self.chaser_last_move_time = current_time

        self.root.after(100, self.game_loop)
