from turtle import Screen, Turtle


class GameScreen:

    def __init__(self):
        self.new_screen = Screen()

    def create_screen(self):
        """Creates a game screen"""
        self.new_screen.setup(width=600, height=600)
        self.new_screen.bgcolor("black")
        self.new_screen.title("Welcome to this colourful snake game")
        self.new_screen.tracer(0)

    def control_screen(self, function, button):
        """control the output of the screen using user input"""
        self.new_screen.listen()
        self.new_screen.onkey(fun=function, key=button)

    def update_screen(self):
        """updates the screen to latest render"""
        self.new_screen.update()

    def click_exit(self):
        """exit the screen"""
        self.new_screen.exitonclick()
