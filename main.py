from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to this fucking snake game")
snake = []
start_pos = [(0, 0), (-20, 0), (-40, 0)]
screen.tracer(0)

for position in start_pos:
    new_part = Turtle(shape="square")
    new_part.penup()
    new_part.color("blue")
    new_part.goto(position)
    snake.append(new_part)

game_on = True
# while game_on:
#     screen.update()
#     time.sleep(0.2)
#
#     for part in range(len(snake)-1, 0, -1):
#         new_x = snake[part - 1].xcor()
#         new_y = snake[part - 1].xcor()
#         snake[part].goto(new_x, new_y)
#     snake[0].forward(10)

while game_on:
    screen.update()
    time.sleep(0.1)

    # Get position of the head, and move it
    next_position = snake[0].position()
    snake[0].forward(20)


    # Move each segment of the snake to occupy the spot of the next segment
    for segment in snake[1:]:
        current_position = segment.position()
        segment.goto(next_position)
        next_position = current_position




screen.exitonclick()