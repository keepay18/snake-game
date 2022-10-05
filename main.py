import turtle
import time
from food import *
from snake import *

window = turtle.Screen()
window.title("Snake Game")
width = 500
height = 500
window.setup(width=width, height=height)
window.bgcolor("green")

snake = Snake(0, 0)
window.listen()
window.onkey(snake.key_up, "Up")
window.onkey(snake.key_down, "Down")
window.onkey(snake.key_left, "Left")
window.onkey(snake.key_right, "Right")

window.onkey(snake.key_up, "w")
window.onkey(snake.key_down, "s")
window.onkey(snake.key_left, "a")
window.onkey(snake.key_right, "d")

food = Food()

while True:
    window.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()

    if snake.check_self_collision() or snake.check_walls_collision(width, height):
        food.refresh()
        snake.refresh()


window.mainloop()
