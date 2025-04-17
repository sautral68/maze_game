import tkinter as tk
import time
import config


class Timer:
    def __init__(self, root):
        self.root = root
        self.start_time = None
        self.label = tk.Label(root, text="Time: 0", font=("Arial", 16))
        self.label.pack()
        self.running = False

    def start(self):
        self.start_time = time.time()
        self.running = True
        self.update()

    def stop(self):
        self.running = False

    def update(self):
        if self.running:
            elapsed = int(time.time() - self.start_time)
            self.label.config(text=f"Time: {elapsed}")
            # Проверяем, не превышено ли время
            if elapsed >= config.TIME_LIMIT:
                self.stop()
            else:
                self.root.after(1000, self.update)

    def get_time(self):
        return int(time.time() - self.start_time) if self.start_time else 0
