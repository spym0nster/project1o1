import time
import socket
from snake_game import SnakeGame

HOST = 'localhost'
PORT = 5555

game = SnakeGame()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def get_action():
    head_x, head_y = game.snake[0]
    food_x, food_y = game.food
    if food_x > head_x:
        return (1, 0)
    elif food_x < head_x:
        return (-1, 0)
    elif food_y > head_y:
        return (0, 1)
    else:
        return (0, -1)

while not game.game_over:
    action = get_action()
    game.change_direction(action)
    game.update()
    time.sleep(0.1)

client.send(f"AI score: {game.score}".encode())
client.close()
print(f"AI finished with score: {game.score}")
