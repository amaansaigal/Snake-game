from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.pu()
        self.goto(-280, 280)
        self.pd()
        self.pensize(14)
        for _ in range(0, 4):
            self.forward(558)
            self.right(90)
        self.pu()
        self.hideturtle()
        self.goto(0, 240)

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", move=False, align="center", font=('Arial', 20, 'normal'))

    def game_over(self, score):
        self.goto(0, 0)
        self.write(f"GAME OVER! Your final Score is {score}", move=False, align="center", font=('Arial', 30, 'normal'))
