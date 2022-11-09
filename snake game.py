import time
from turtle import colormode
from snake import Snake
from Screen import GameScreen
from food import Food
from Scoreboard import ScoreBoard
colormode(255)
screen = GameScreen()
snake = Snake()
screen.create_screen()
snake.make_snake()
food = Food()
scoreboard = ScoreBoard()
score = 0
game_over = ScoreBoard()
screen.control_screen(snake.move_left, "a")
screen.control_screen(snake.move_right, "d")
screen.control_screen(snake.move_up, "w")
screen.control_screen(snake.move_down, "s")

game_on = True
while game_on:
    screen.update_screen()
    time.sleep(0.1)
    snake.move_forward()

    if snake.check_wall_hit() or snake.body_hit():
        game_over.game_over(score)
        scoreboard.clear()
        game_on = False

    if snake.check_distance(food) < 15:
        food.change_food_location()
        score += 1
        scoreboard.update_score(score)
        snake.add_tail()


screen.click_exit()


