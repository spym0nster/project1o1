import pygame
import random

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(5, 5)]
        self.direction = (1, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        while True:
            pos = (random.randint(0, WIDTH//CELL_SIZE - 1),
                   random.randint(0, HEIGHT//CELL_SIZE - 1))
            if pos not in self.snake:
                return pos

    def update(self):
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if (new_head in self.snake or
            not 0 <= new_head[0] < WIDTH//CELL_SIZE or
            not 0 <= new_head[1] < HEIGHT//CELL_SIZE):
            self.game_over = True
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def change_direction(self, new_dir):
        if (new_dir[0] == -self.direction[0] and new_dir[1] == -self.direction[1]):
            return
        self.direction = new_dir
