import pygame
import socket
from snake_game import SnakeGame, WIDTH, HEIGHT, CELL_SIZE

HOST = 'localhost'
PORT = 5555

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Human")

clock = pygame.time.Clock()

game = SnakeGame()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def draw_game():
    win.fill((0, 0, 0))
    for cell in game.snake:
        pygame.draw.rect(win, (0, 255, 0), (cell[0]*CELL_SIZE, cell[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(win, (255, 0, 0), (game.food[0]*CELL_SIZE, game.food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

while not game.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: game.change_direction((0, -1))
            elif event.key == pygame.K_DOWN: game.change_direction((0, 1))
            elif event.key == pygame.K_LEFT: game.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT: game.change_direction((1, 0))

    game.update()
    draw_game()
    clock.tick(10)

client.send(f"Human score: {game.score}".encode())
client.close()
pygame.quit()
