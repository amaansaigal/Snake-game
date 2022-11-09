from turtle import Turtle
from random import randint
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.parts = []

    def make_snake(self):
        """Returns a snake of 3 items"""

        for position in STARTING_POS:
            new_part = Turtle(shape="square")
            new_part.penup()
            new_part.color("blue")
            new_part.goto(position)
            self.parts.append(new_part)
        return self.parts

    def move_left(self):
        if self.parts[0].heading() != 0:
            self.parts[0].seth(180)

    def move_right(self):
        if self.parts[0].heading() != 180:
            self.parts[0].seth(0)

    def move_up(self):
        if self.parts[0].heading() != 270:
            self.parts[0].seth(90)

    def move_down(self):
        if self.parts[0].heading() != 90:
            self.parts[0].seth(270)

    def add_tail(self):
        snake_len = len(self.parts)
        cur_tail_posx = self.parts[snake_len-1].xcor()
        cur_tail_posy = self.parts[snake_len - 1].ycor()
        tail = Turtle(shape="square")
        tail.penup()
        tail.color(randint(0, 220), randint(0, 220), randint(0, 220))
        tail.speed("fastest")
        self.parts.append(tail)
        tail.goto(cur_tail_posx, cur_tail_posy)

    def check_wall_hit(self):
        """checks if the snake has hit the wall"""
        if self.parts[0].xcor() >= 280 or self.parts[0].xcor() <= -280:
            return True
        elif self.parts[0].ycor() >= 280 or self.parts[0].ycor() <= -280:
            return True

    def body_hit(self):
        """checks if the snake has hit own body, returns boolean"""
        for part in self.parts[1:]:
            body = part.position()
            if self.check_distance(body) < 10:
                return True

    def move_forward(self):
        """Moves the snake by MOVE_DISTANCE"""
        next_position = self.parts[0].position()
        self.parts[0].forward(MOVE_DISTANCE)

        # Move each segment of the snake to occupy the spot of the next segment
        for segment in self.parts[1:]:
            current_position = segment.position()
            segment.goto(next_position)
            next_position = current_position

    def check_distance(self, object):
        return self.parts[0].distance(object)

