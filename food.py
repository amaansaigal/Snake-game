from turtle import *
from random import randint
colormode(255)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.change_food_location()

    def change_food_location(self):
        self.goto(randint(-260, 260), randint(-260, 260))
        self.color(randint(0, 200), randint(0, 200), randint(0, 200))
