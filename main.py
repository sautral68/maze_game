from tkinter import Tk
from game import MazeGame


if __name__ == "__main__":
    root = Tk()
    root.title("Maze Challenge")
    game = MazeGame(root)
    root.mainloop()
